# Pablo Lerner Portfolio

## Quick Start
```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

## Architecture
- **main.py** - FastAPI app. Reads `content/content.md`, parses it into sections, renders `templates/index.html` via Jinja2.
- **content/content.md** - All portfolio content in structured markdown. Edit this to update text, add projects, or change skills.
- **templates/index.html** - HTML template with Jinja2 placeholders. Edit to change page structure.
- **static/style.css** - All styling. Dark theme with indigo accent. Pure CSS, no frameworks.

## How to Update Content
Edit `content/content.md`. The markdown structure is:
- `# Name` - H1 for the portfolio owner name
- `## hero` - First line is title, third line is tagline
- `## about` - Paragraphs separated by blank lines
- `## skills` - Bullet list (`- Skill Name`)
- `## projects` - Each project is `### Title` followed by description and `**Tags**: tag1, tag2`
- `## contact` - Bullet list with `- key: value` format (email, linkedin, github)

## How to Change Styling
Edit `static/style.css`. CSS variables are defined in `:root` for colors and border radius.

## Content Language
English.
