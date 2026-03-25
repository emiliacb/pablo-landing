import mimetypes
import re
from pathlib import Path

mimetypes.add_type("text/css", ".css")
mimetypes.add_type("application/javascript", ".js")
mimetypes.add_type("image/svg+xml", ".svg")

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Pablo Lerner Portfolio")

BASE_DIR = Path(__file__).resolve().parent
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


def parse_content(filepath: Path) -> dict:
    """Parse content.md into structured sections."""
    text = filepath.read_text(encoding="utf-8")

    # Extract name from H1
    name_match = re.search(r"^# (.+)$", text, re.MULTILINE)
    name = name_match.group(1).strip() if name_match else "Pablo Lerner"

    # Split into sections by ## headers
    sections = {}
    parts = re.split(r"^## (\w+)\s*$", text, flags=re.MULTILINE)
    # parts = ['before first ##', 'hero', 'hero content', 'about', 'about content', ...]
    for i in range(1, len(parts) - 1, 2):
        key = parts[i].strip().lower()
        content = parts[i + 1].strip()
        sections[key] = content

    # Parse hero
    hero_lines = sections.get("hero", "").split("\n")
    hero_title = hero_lines[0].strip() if hero_lines else ""
    hero_tagline = hero_lines[2].strip() if len(hero_lines) > 2 else ""

    # Parse about - split into paragraphs
    about = [p.strip() for p in sections.get("about", "").split("\n\n") if p.strip()]

    # Parse skills - list items
    skills = []
    for line in sections.get("skills", "").split("\n"):
        line = line.strip()
        if line.startswith("- "):
            skills.append(line[2:].strip())

    # Parse projects - split by ### headers
    projects = []
    proj_text = sections.get("projects", "")
    proj_parts = re.split(r"^### (.+)$", proj_text, flags=re.MULTILINE)
    for i in range(1, len(proj_parts) - 1, 2):
        title = proj_parts[i].strip()
        body = proj_parts[i + 1].strip()
        # Extract links
        links = []
        links_match = re.search(r"\*\*Links\*\*:\s*(.+)$", body, re.MULTILINE)
        if links_match:
            for item in links_match.group(1).split(","):
                item = item.strip()
                if "|" in item:
                    label, url = item.split("|", 1)
                    links.append({"label": label.strip(), "url": url.strip()})
            body = body[: links_match.start()].strip()
        # Extract tags
        tags = []
        tags_match = re.search(r"\*\*Tags\*\*:\s*(.+)$", body, re.MULTILINE)
        if tags_match:
            tags = [t.strip() for t in tags_match.group(1).split(",")]
            body = body[: tags_match.start()].strip()
        projects.append({"title": title, "description": body, "tags": tags, "links": links})

    # Parse contact
    contact = {}
    for line in sections.get("contact", "").split("\n"):
        line = line.strip()
        if line.startswith("- "):
            line = line[2:]
            if ":" in line:
                key, val = line.split(":", 1)
                contact[key.strip()] = val.strip()

    return {
        "name": name,
        "hero_title": hero_title,
        "hero_tagline": hero_tagline,
        "about": about,
        "skills": skills,
        "projects": projects,
        "contact": contact,
    }


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    content = parse_content(BASE_DIR / "content" / "content.md")
    og_image_url = str(request.url_for("static", path="og-image.png"))
    content["og_image_url"] = og_image_url
    return templates.TemplateResponse(request, "index.html", content)
