# Nano-Banana Pro Prompting Guide

## Golden Rules of Prompting

Nano-Banana Pro is a "Thinking" model that understands intent, physics, and composition. Stop using "tag soups" and start acting like a Creative Director.

### 1. Edit, Don't Re-roll
The model excels at understanding conversational edits. If an image is 80% correct, don't regenerate—simply ask for the specific change.

**Example:** "That's great, but change the lighting to sunset and make the text neon blue."

### 2. Use Natural Language & Full Sentences
Talk to the model as if briefing a human artist. Use proper grammar and descriptive adjectives.

- ❌ Bad: "Cool car, neon, city, night, 8k."
- ✅ Good: "A cinematic wide shot of a futuristic sports car speeding through a rainy Tokyo street at night. The neon signs reflect off the wet pavement and the car's metallic chassis."

### 3. Be Specific and Descriptive
Define the subject, setting, lighting, and mood.

- **Subject:** Instead of "a woman," say "a sophisticated elderly woman wearing a vintage Chanel-style suit"
- **Materiality:** Describe textures like "matte finish," "brushed steel," "soft velvet," "crumpled paper"
- **Setting:** Specific locations and environmental details
- **Lighting:** Time of day, light quality, mood

### 4. Provide Context (The "Why" or "For Whom")
Because the model "thinks," giving it context helps it make logical artistic decisions.

**Example:** "Create an image of a sandwich for a Brazilian high-end gourmet cookbook."
(The model will infer professional plating, shallow depth of field, and perfect lighting)

---

## Text Rendering, Infographics & Visual Synthesis

Nano-Banana Pro has SOTA capabilities for rendering legible, stylized text and synthesizing complex information.

### Best Practices
- **Compression:** Ask the model to "compress" dense text or PDFs into visual aids
- **Style:** Specify if you want a "polished editorial," a "technical diagram," or a "hand-drawn whiteboard" look
- **Quotes:** Clearly specify the text you want in quotes

### Example Prompts

**Earnings Report Infographic:**
```
"Generate a clean, modern infographic summarizing the key financial highlights from this earnings report. Include charts for 'Revenue Growth' and 'Net Income', and highlight the CEO's key quote in a stylized pull-quote box."
```

**Technical Diagram:**
```
"Create an orthographic blueprint that describes this building in plan, elevation, and section. Label the 'North Elevation' and 'Main Entrance' clearly in technical architectural font. Format 16:9."
```

**Whiteboard Summary:**
```
"Summarize the concept of 'Transformer Neural Network Architecture' as a hand-drawn whiteboard diagram suitable for a university lecture. Use different colored markers for the Encoder and Decoder blocks, and include legible labels for 'Self-Attention' and 'Feed Forward'."
```

---

## Character Consistency & Viral Thumbnails

Supports up to 14 reference images (6 with high fidelity) for "Identity Locking"—placing a specific person or character into new scenarios without facial distortion.

### Best Practices
- **Identity Locking:** Explicitly state: "Keep the person's facial features exactly the same as Image 1"
- **Expression/Action:** Describe the change in emotion or pose while maintaining the identity
- **Viral Composition:** Combine subjects with bold graphics and text in a single pass

### Example Prompts

**Viral Thumbnail:**
```
"Design a viral video thumbnail using the person from Image 1. Face Consistency: Keep the person's facial features exactly the same as Image 1, but change their expression to look excited and surprised. Action: Pose the person on the left side, pointing their finger towards the right side of the frame. Subject: On the right side, place a high-quality image of a delicious avocado toast. Graphics: Add a bold yellow arrow connecting the person's finger to the toast. Text: Overlay massive, pop-style text in the middle: '3 分钟搞定!' (Done in 3 mins!). Use a thick white outline and drop shadow. Background: A blurred, bright kitchen background. High saturation and contrast."
```

**Multi-Part Story:**
```
"Create a funny 10-part story with these 3 fluffy friends going on a tropical vacation. The story is thrilling throughout with emotional highs and lows and ends in a happy moment. Keep the attire and identity consistent for all 3 characters, but their expressions and angles should vary throughout all 10 images. Make sure to only have one of each character in each image."
```

---

## Grounding with Google Search

Uses Google Search to generate imagery based on real-time data, current events, or factual verification.

### Example Prompt
```
"Generate an infographic of the best times to visit the U.S. National Parks in 2025 based on current travel trends."
```

---

## Advanced Editing, Restoration & Colorization

Excels at complex edits via conversational prompting: in-painting, restoration, colorization, and style swapping.

### Best Practices
- **Semantic Instructions:** You don't need to manually mask; simply tell the model what to change naturally
- **Physics Understanding:** Ask for complex changes like "fill this glass with liquid"

### Example Prompts

**Object Removal:**
```
"Remove the tourists from the background of this photo and fill the space with logical textures (cobblestones and storefronts) that match the surrounding environment."
```

**Manga Colorization:**
```
"Colorize this manga panel. Use a vibrant anime style palette. Ensure the lighting effects on the energy beams are glowing neon blue and the character's outfit is consistent with their official colors."
```

**Localization:**
```
"Take this concept and localize it to a Tokyo setting, including translating the tagline into Japanese. Change the background to a bustling Shibuya street at night."
```

**Lighting/Seasonal Control:**
```
"Turn this scene into winter time. Keep the house architecture exactly the same, but add snow to the roof and yard, and change the lighting to a cold, overcast afternoon."
```

---

## Dimensional Translation (2D ↔ 3D)

Translate 2D schematics into 3D visualizations, or vice versa.

### Example Prompts

**2D Floor Plan to 3D Interior:**
```
"Based on the uploaded 2D floor plan, generate a professional interior design presentation board in a single image. Layout: A collage with one large main image at the top (wide-angle perspective of the living area), and three smaller images below (Master Bedroom, Home Office, and a 3D top-down floor plan). Style: Apply a Modern Minimalist style with warm oak wood flooring and off-white walls across ALL images. Quality: Photorealistic rendering, soft natural lighting."
```

---

## High-Resolution & Textures

Supports native 1K to 4K image generation.

### Best Practices
- Request high resolutions (2K or 4K) only when extra fidelity is specifically required
- Describe high-fidelity details (imperfections, surface textures)

### Example Prompt
```
"Harness native high-fidelity output to craft a breathtaking, atmospheric environment of a mossy forest floor. Command complex lighting effects and delicate textures, ensuring every strand of moss and beam of light is rendered in pixel-perfect resolution suitable for a 4K wallpaper."
```

---

## Thinking & Reasoning

Defaults to a "Thinking" process where it generates interim thought images (not charged) to refine composition.

### Example Prompts

**Solve Equations:**
```
"Solve log_{x^2+1}(x^4-1)=2 in C on a white board. Show the steps clearly."
```

**Visual Reasoning:**
```
"Analyze this image of a room and generate a 'before' image that shows what the room might have looked like during construction, showing the framing and unfinished drywall."
```

---

## One-Shot Storyboarding & Concept Art

Generate sequential art or storyboards ensuring a cohesive narrative flow in a single session.

### Example Prompt
```
"Create an addictively intriguing 9-part story with 9 images featuring a woman and man in an award-winning luxury luggage commercial. The story should have emotional highs and lows, ending on an elegant shot of the woman with the logo. The identity of the woman and man and their attire must stay consistent throughout but they can and should be seen from different angles and distances. Please generate images one at a time. Make sure every image is in a 16:9 landscape format."
```

---

## Structural Control & Layout Guidance

Use input images to strictly control composition and layout.

### Best Practices
- **Drafts & Sketches:** Upload a hand-drawn sketch to define exactly where text and objects should sit
- **Wireframes:** Use screenshots of existing layouts or wireframes to generate high-fidelity UI mockups
- **Grids:** Use grid images to force the model to generate assets for tile-based games or LED displays

### Example Prompts

**Sketch to Final Ad:**
```
"Create an ad for a [product] following this sketch."
```

**UI Mockup from Wireframe:**
```
"Create a mock-up for a [product] following these guidelines."
```

**Pixel Art & LED Displays:**
```
"Generate a pixel art sprite of a unicorn that fits perfectly into this 64x64 grid image. Use high contrast colors."
```

**Sprites:**
```
"Sprite sheet of a woman doing a backflip on a drone, 3x3 grid, sequence, frame by frame animation, square aspect ratio. Follow the structure of the attached reference image exactly."
```
