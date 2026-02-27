#!/usr/bin/env python3
import argparse
import mimetypes
import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables from skill's own .env
skill_root = Path(__file__).parent.parent
load_dotenv(dotenv_path=skill_root / ".env", override=False)


def main():
    parser = argparse.ArgumentParser(
        description="Generate images using Google Gemini.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --prompt "A cat in space" --output cat.png
  %(prog)s --prompt "Same style but blue" --reference input.png --output blue.png
  %(prog)s --prompt "Use both references" --reference a.png --reference b.png --output out.png
  %(prog)s --prompt "Three variations" --output art.png --count 3
        """,
    )
    parser.add_argument(
        "--prompt", required=True, help="Text prompt describing the image to generate"
    )
    parser.add_argument(
        "--output", required=True, help="Output file path for the generated image"
    )
    parser.add_argument(
        "--reference",
        action="append",
        help="Optional reference image path for style/content guidance. Provide multiple times to include multiple images.",
    )
    parser.add_argument(
        "--size",
        default="2K",
        choices=["1K", "2K", "4K"],
        help="Output image size (default: 2K)",
    )
    parser.add_argument(
        "--model",
        default="gemini-3.1-flash-image-preview",
        choices=["gemini-3.1-flash-image-preview", "gemini-3-pro-image-preview"],
        help="Model to use (default: gemini-3.1-flash-image-preview). Use gemini-3-pro-image-preview for higher quality.",
    )
    parser.add_argument(
        "--count",
        type=int,
        default=1,
        help="Number of outputs to generate (default: 1)",
    )
    args = parser.parse_args()

    if args.count < 1:
        print("Error: --count must be >= 1.", file=sys.stderr)
        sys.exit(1)

    # Get API key from environment
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set.", file=sys.stderr)
        print(
            "Add it to ~/.claude/skills/gemini-image-generator/.env",
            file=sys.stderr,
        )
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    # Build content parts
    parts = [types.Part.from_text(text=args.prompt)]

    # Add reference image if provided
    if args.reference:
        if len(args.reference) > 14:
            print(
                "Error: Too many reference images. Provide at most 14 --reference arguments.",
                file=sys.stderr,
            )
            sys.exit(1)
        try:
            for reference_path in args.reference:
                with open(reference_path, "rb") as f:
                    image_data = f.read()
                mime_type = mimetypes.guess_type(reference_path)[0] or "image/png"
                parts.append(
                    types.Part.from_bytes(data=image_data, mime_type=mime_type)
                )
                print(f"Using reference image: {reference_path}")
        except FileNotFoundError:
            print("Error: One of the reference images was not found.", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Error loading reference image: {e}", file=sys.stderr)
            sys.exit(1)

    # Create content with proper structure
    contents = [
        types.Content(
            role="user",
            parts=parts,
        ),
    ]

    # Configure generation with image settings
    generate_content_config = types.GenerateContentConfig(
        response_modalities=["IMAGE", "TEXT"],
        candidate_count=args.count,
        image_config=types.ImageConfig(
            image_size=args.size,
        ),
    )

    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")

    print(f"Generating image with model: {args.model}, size: {args.size}...")

    try:
        response = client.models.generate_content(
            model=args.model,
            contents=contents,
            config=generate_content_config,
        )

        output_path = Path(args.output)
        output_dir = output_path.parent
        output_stem = output_path.stem
        output_suffix = output_path.suffix or ".png"

        if response.candidates is None:
            print(
                "Warning: No candidates were generated in the response.",
                file=sys.stderr,
            )
            sys.exit(1)

        images_saved = 0
        for candidate_index, candidate in enumerate(response.candidates, start=1):
            if candidate.content is None or candidate.content.parts is None:
                continue

            inline_data = None
            for part in candidate.content.parts:
                if getattr(part, "inline_data", None) and part.inline_data.data:
                    inline_data = part.inline_data
                    break

            if inline_data is None:
                continue

            if args.count == 1:
                candidate_output_path = output_path
            else:
                candidate_output_path = (
                    output_dir / f"{output_stem}_{candidate_index:02d}{output_suffix}"
                )

            with open(candidate_output_path, "wb") as f:
                f.write(inline_data.data)
            print(f"Image saved to: {candidate_output_path}")
            images_saved += 1

            if images_saved >= args.count:
                break

        if images_saved == 0:
            print("Warning: No image was generated in the response.", file=sys.stderr)
            if hasattr(response, "text") and response.text:
                print(f"Model response: {response.text}")
            sys.exit(1)

    except Exception as e:
        print(f"Error generating image: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
