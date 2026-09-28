from datetime import date
from pathlib import Path

from flask import Flask, abort, render_template

import content

app = Flask(__name__)


def static_exists(filename):
    return bool(filename) and (Path(app.static_folder) / filename).exists()


def site_context():
    """Everything the templates need, built from content.py."""
    # Only list sections that have content, so numbering stays in order
    sections = [("about", "About")]
    if content.EXPERIENCE:
        sections.append(("experience", "Experience"))
    if content.PROJECTS:
        sections.append(("projects", "Projects"))
    if content.EDUCATION:
        sections.append(("education", "Education"))
    if content.SKILLS:
        sections.append(("skills", "Skills"))
    sections.append(("contact", "Contact"))
    ids = [s[0] for s in sections]

    # Project categories in first-seen order, with counts for the filter buttons
    categories = {}
    for p in content.PROJECTS:
        if p.get("category"):
            categories[p["category"]] = categories.get(p["category"], 0) + 1

    initials = "".join(w[0] for w in content.SITE["name"].split()[:2]).upper()

    return dict(
        site=content.SITE,
        has_resume=static_exists(content.SITE.get("resume")),
        links=content.LINKS,
        about=content.ABOUT.strip(),
        experience=content.EXPERIENCE,
        projects=content.PROJECTS,
        education=content.EDUCATION,
        skills=content.SKILLS,
        stats=getattr(content, "STATS", []),
        categories=categories,
        sections=sections,
        num=lambda section_id: ids.index(section_id) + 1,
        initials=initials,
        year=date.today().year,
    )


@app.route("/")
def index():
    return render_template("index.html", **site_context())


@app.route("/projects/<slug>/")
def project_page(slug):
    projects = [p for p in content.PROJECTS if p.get("slug")]
    for i, p in enumerate(projects):
        if p["slug"] == slug:
            break
    else:
        abort(404)
    return render_template(
        "project.html",
        **site_context(),
        project=p,
        has_image=static_exists(p.get("image")),
        prev_project=projects[i - 1] if i > 0 else None,
        next_project=projects[i + 1] if i + 1 < len(projects) else None,
    )


if __name__ == "__main__":
    app.run(debug=True)
