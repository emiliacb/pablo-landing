# Agent Instructions - Pablo Lerner Portfolio

## Project Overview
Minimalist single-page portfolio for Pablo Lerner (Data Analyst & AI Engineer). Built with FastAPI + Jinja2 + plain CSS. Content is maintained in `content.md` and rendered dynamically.

## File Map
| File | Purpose |
|------|---------|
| `main.py` | FastAPI app, markdown parser, single route |
| `content.md` | All portfolio content in structured markdown |
| `templates/index.html` | Jinja2 HTML template |
| `static/style.css` | All CSS styling |
| `requirements.txt` | Python dependencies |

## Common Tasks

### Add a New Project
Edit `content.md`. Under `## projects`, add:
```markdown
### Project Title

Description of the project.

**Tags**: Tag1, Tag2, Tag3
```

### Add a New Skill
Edit `content.md`. Under `## skills`, add a new bullet:
```markdown
- New Skill
```

### Add a New Section
1. Add `## sectionname` to `content.md`
2. Update the parser in `main.py` to extract the new section
3. Add the section HTML to `templates/index.html`
4. Add styling to `static/style.css` if needed

### Update Contact Info
Edit `content.md` under `## contact`. Format: `- key: value`

## Conventions
- **Theme**: Dark background (#0a0a0a), light text (#e5e5e5), indigo accent (#6366f1)
- **CSS**: Pure CSS with variables in `:root`. No frameworks.
- **HTML**: Semantic HTML5. Minimal, clean markup.
- **Content**: English language.
- **Dependencies**: Keep minimal. No frontend build tools.

## Running Locally
```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```
