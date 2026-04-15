---
name: gemini-image-generator
description: Generate images using Google Gemini Nano-Banana Pro with three modes - (1) Skylar Brand mode for marketing materials, social media, and brand visuals, (2) Free-Flowing mode for unrestricted creative work, (3) Graph/Data Visualization mode for Skylar dashboard components and metrics using consistent visual DNA. Use when creating marketing graphics, social posts, data visualizations, infographics, or any image generation task.
---

# gemini-image-generator

Generate high-quality images using Google Gemini's Nano-Banana Pro model with support for three operational modes, each optimized for different use cases.

## Command Reference

### Basic Usage

```bash
~/.claude/skills/gemini-image-generator/.venv/bin/python ~/.claude/skills/gemini-image-generator/scripts/generate.py \
  --prompt "Your detailed prompt here" \
  --output path/to/output.png
```

### Parameters

- `--prompt` (required): Detailed text description of the image to generate
- `--output` (required): Output file path for the generated image (if `--count > 1`, outputs are saved as `name_01.png`, `name_02.png`, etc.)
- `--model` (optional): Model to use (default: `gemini-3.1-flash-image-preview`). Use `--model gemini-3-pro-image-preview` for higher quality when needed.
- `--reference` (optional): Reference image(s) for style/content guidance (up to 14 images, 6 with high fidelity)
- `--size` (optional): Image size - "1K", "2K", or "4K" (default: 2K)
- `--count` (optional): Number of outputs to generate (default: 1). Note: some models may reject `--count > 1`; if so, run multiple separate commands instead.

### Model Selection

| Model | Use When |
|-------|----------|
| `gemini-3.1-flash-image-preview` (default) | Most requests - faster and cheaper |
| `gemini-3-pro-image-preview` | Higher quality needed, complex scenes, or when flash results aren't good enough |

### With Reference Image

```bash
~/.claude/skills/gemini-image-generator/.venv/bin/python ~/.claude/skills/gemini-image-generator/scripts/generate.py \
  --prompt "Same dashboard layout but with updated metrics and Success Green accents" \
  --reference previous-dashboard.png \
  --output updated-dashboard.png
```

### High Resolution / Pro Model

```bash
~/.claude/skills/gemini-image-generator/.venv/bin/python ~/.claude/skills/gemini-image-generator/scripts/generate.py \
  --prompt "Your detailed prompt" \
  --output large-format.png \
  --size 4K \
  --model gemini-3-pro-image-preview
```

### Multiple Variations

The current model used by `scripts/generate.py` may not support multiple candidates in a single request. If `--count > 1` fails, generate variations by running multiple commands with different output names:

```bash
~/.claude/skills/gemini-image-generator/.venv/bin/python ~/.claude/skills/gemini-image-generator/scripts/generate.py \
  --prompt "Variation 1: ..." \
  --output variations_01.png \
  --size 2K

~/.claude/skills/gemini-image-generator/.venv/bin/python ~/.claude/skills/gemini-image-generator/scripts/generate.py \
  --prompt "Variation 2: ..." \
  --output variations_02.png \
  --size 2K

~/.claude/skills/gemini-image-generator/.venv/bin/python ~/.claude/skills/gemini-image-generator/scripts/generate.py \
  --prompt "Variation 3: ..." \
  --output variations_03.png \
  --size 2K
```

---

## Operational Modes

### Mode Selection Guide

Choose your mode based on the task:

| Mode               | Use When                                                                                                 | Read This Reference                                                                                                                                         |
| ------------------ | -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Skylar Brand**   | Marketing materials, social media graphics, website visuals, presentations, any branded content          | [skylar-brand.md](references/skylar-brand.md) - Complete brand guidelines (use [prompting-guide.md](references/prompting-guide.md) sections as needed)      |
| **Free-Flowing**   | Unrestricted creative work, testing concepts, non-branded content, personal projects                     | [prompting-guide.md](references/prompting-guide.md) - Full capabilities guide                                                                               |
| **Graph/Data Viz** | Creating dashboard cards, charts, metrics, or any data visualization that needs Skylar brand consistency | [skylar-brand.md](references/skylar-brand.md) - Data Visualization DNA section (use [prompting-guide.md](references/prompting-guide.md) sections as needed) |

### 1. Skylar Brand Mode

Generate branded visuals that embody Skylar's identity across all content types.

**Key Requirements:**

- **Skylar logo:** Always use `~/.claude/skills/gemini-image-generator/references/skylar-clean-logo.png` as `--reference` when the Skylar logo needs to appear in the image
- Brand colors: Primary Blue (#37bcd9), Skylar Cyan (#8ee6f7), Dark Navy (#0e2e3e)
- Ubuntu typography
- Professional yet approachable style
- Liquid wave backgrounds, matte finishes, soft depth

**Before generating:** Read [skylar-brand.md](references/skylar-brand.md) for:

- Complete color palette (primary, semantic, gradients)
- Typography rules and hierarchy
- Brand voice and design principles
- Component styles (buttons, cards, info boxes)

**Always also read these sections in [prompting-guide.md](references/prompting-guide.md):**

- Golden Rules (edit vs. re-roll, natural language, specificity)
- Text Rendering, Infographics & Visual Synthesis (for legible copy and layout)
- Advanced Editing, Restoration & Colorization (for iterative edits)
- Structural Control & Layout Guidance (for wireframes/sketches/layout locking)
- Character Consistency & Viral Thumbnails (if you’re identity-locking a person/character)

**Quick Example:**

```bash
~/.claude/skills/gemini-image-generator/.venv/bin/python ~/.claude/skills/gemini-image-generator/scripts/generate.py \
  --prompt "Professional LinkedIn post header for a SaaS company. Background: Premium flowing liquid waves in Skylar Cyan (#8EE6F7) and Deep Teal (#37BCD9) creating an abstract, elegant pattern. Foreground: Subtle overlay of geometric elements suggesting technology. Typography: Large heading 'Transform Your Sales Training' in Ubuntu font, Dark Navy (#0E2E3E), left-aligned. Style: Modern, professional, approachable. Matte finish, soft depth, no harsh gradients. 16:9 aspect ratio." \
  --output linkedin-header.png \
  --size 2K
```

### 2. Free-Flowing Mode

Unrestricted creative image generation using Nano-Banana Pro's full capabilities.

**Key Principles:**

- Use natural language and full sentences (not tag soups)
- Be specific about subject, setting, lighting, mood
- Provide context to help the model make logical decisions
- Edit conversationally rather than regenerating

**Before generating:** Read [prompting-guide.md](references/prompting-guide.md) for:

- Golden Rules (edit don't re-roll, natural language, specificity, context)
- Advanced capabilities (text rendering, character consistency, structural control)
- Thinking & reasoning mode
- All specialized techniques

**Quick Example:**

```bash
~/.claude/skills/gemini-image-generator/.venv/bin/python ~/.claude/skills/gemini-image-generator/scripts/generate.py \
  --prompt "A cinematic wide shot of a modern minimalist office space bathed in golden hour sunlight. Floor-to-ceiling windows reveal a city skyline. In the foreground, a sleek wooden desk holds a single laptop displaying charts. The atmosphere conveys productivity and calm. Photorealistic, shallow depth of field, professional architectural photography style." \
  --output office-hero.png \
  --size 2K
```

### 3. Graph/Data Viz Mode

Create consistent, professional data visualizations following Skylar's visual DNA.

**Key Requirements:**

- Liquid wave backgrounds in Skylar Cyan (#8EE6F7) and Deep Teal (#37BCD9)
- Matte white cards with subtle borders
- Ubuntu font, Dark Navy (#0E2E3E) headings
- Flat design with soft depth, no neon effects

**Before generating:** Read [skylar-brand.md](references/skylar-brand.md) for:

- Core DNA template (required for all graphs)
- Component recipes (comparisons, percentages, increases)
- Vocabulary cheat sheet (approved vs. forbidden terms)
- Full color palette and design principles

**When Graph/Data Viz work needs advanced prompting techniques:** Read relevant sections in [prompting-guide.md](references/prompting-guide.md), especially:

- Text Rendering, Infographics & Visual Synthesis (for crisp UI and layout)
- Structural Control & Layout Guidance (for wireframes/sketches/layout locking)

**Quick Example:**

```bash
~/.claude/skills/gemini-image-generator/.venv/bin/python ~/.claude/skills/gemini-image-generator/scripts/generate.py \
  --prompt "Three high-fidelity SaaS dashboard cards on premium liquid wave background in Skylar Cyan (#8EE6F7) and Deep Teal (#37BCD9). Clean matte white cards with subtle borders and teal drop shadows. Ubuntu font, Dark Navy (#0E2E3E) headings. Card 1: Vertical bar chart showing 8.4 vs 9.0, main bar in Teal. Card 2: Circular progress ring 39% in Teal. Card 3: '+17%' in Success Green (#2A7D5F) with upward arrow. Clean UI, flat design, no neon effects." \
  --output dashboard.png \
  --size 2K
```

---

## Best Practices

### For All Modes

1. **Always use multiple references:** The script supports `--reference` multiple times. Always include all relevant references — the Skylar logo (`~/.claude/skills/gemini-image-generator/references/skylar-clean-logo.png`), wave/ribbon style references, and any other brand assets needed. More references = more consistent output. Don't be lazy about this.
2. **Always start with flash:** Use the default `gemini-3.1-flash-image-preview` for all initial generations and iterations. Only switch to `gemini-3-pro-image-preview` for final production-quality output or when flash results aren't good enough.
3. **Edit, don't re-roll:** If an image is 80% correct, use it as a reference and request specific changes rather than regenerating from scratch.
4. **Limit reference chains:** After 2-3 rounds of using previous outputs as `--reference`, quality drifts. If you're past that point, start fresh with an improved prompt instead of chaining more edits.
5. **Be specific:** Define subject, setting, lighting, mood, materials, textures
6. **Use natural language:** Full sentences and proper grammar, not keyword lists
7. **Provide context:** Tell the model why or for whom you're creating the image

### For Skylar Brand Mode

1. **Read skylar-brand.md for complete guidelines** - Colors, typography, design principles
2. **Use "liquid waves" for backgrounds** - Premium, flowing silk waves
3. **Specify "matte" finishes** - Not glass, transparent, or glowing
4. **Include brand voice** - Professional yet approachable, confident, encouraging
5. **Use prompting-guide.md sections as needed** - Text rendering, layout control, iterative edits

### For Free-Flowing Mode

1. **Read prompting-guide.md for advanced techniques** - Character consistency, structural control, thinking mode
2. **Describe textures and materials** - "matte finish," "brushed steel," "soft velvet"
3. **Specify lighting** - Time of day, light quality, mood
4. **Use reference images** - For identity locking, style guidance, layout control

### For Graph/Data Viz Mode

1. **Always read skylar-brand.md first** - Use the Core DNA template
2. **Use exact hex codes** - #8EE6F7, #37BCD9, #0E2E3E
3. **Mention "Ubuntu font" explicitly**
4. **Include "no neon effects"** to avoid generic looks
5. **Use vocabulary cheat sheet** - Say "Functional Beauty" not "Sci-fi"
6. **Use prompting-guide.md sections as needed** - Text rendering and layout control for crisp UI

---

## Reference Files

Detailed guides for each mode:

- **[prompting-guide.md](references/prompting-guide.md)** - Complete Nano-Banana Pro capabilities and techniques
- **[skylar-brand.md](references/skylar-brand.md)** - Skylar brand guidelines and visual DNA
- **[visualisations.md](references/visualisations.md)** - Original visualization guide (legacy reference)

---

## Setup

### Dependencies

One-time setup - creates a venv inside the skill folder:

```bash
python3 -m venv ~/.claude/skills/gemini-image-generator/.venv
~/.claude/skills/gemini-image-generator/.venv/bin/pip install python-dotenv google-genai
```

### API Key

Set your Gemini API key in the skill's own `.env`:

```bash
# ~/.claude/skills/gemini-image-generator/.env
GEMINI_API_KEY="your-api-key-here"
```

The script also respects `GEMINI_API_KEY` from your shell environment as a fallback.

---

## Common Workflows

### Create Branded Marketing Visual

1. Read [skylar-brand.md](references/skylar-brand.md) - Complete brand guidelines
2. Choose appropriate colors from the palette
3. Specify Ubuntu typography and liquid wave backgrounds
4. Include "professional yet approachable" in your prompt

### Create Unrestricted Creative Image

1. Read [prompting-guide.md](references/prompting-guide.md) - Golden Rules
2. Write a detailed, natural language prompt
3. Be specific about subject, setting, lighting, mood
4. Use reference images if needed for style/composition control

### Create a Dashboard Metric Card

1. Read [skylar-brand.md](references/skylar-brand.md) - Data Visualization DNA section
2. Use the Core DNA template as your prompt foundation
3. Add specific metric details using Component Recipes
4. Generate at default 2K, and only add `--size 4K` if you specifically need extra fidelity

### Iterate on an Existing Image

1. Use the previous image as `--reference`
2. Request only the specific changes needed
3. Keep the working elements, modify what needs adjustment
4. Don't regenerate from scratch if 80%+ is correct
