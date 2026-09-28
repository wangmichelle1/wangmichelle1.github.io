"""Build the site into static HTML in ./build (this is what gets hosted)."""
from flask_frozen import Freezer

import content
from app import app

app.config["FREEZER_DESTINATION"] = "build"
app.config["FREEZER_RELATIVE_URLS"] = True  # works at user.github.io/repo-name/

freezer = Freezer(app)


@freezer.register_generator
def project_page():
    for p in content.PROJECTS:
        if p.get("slug"):
            yield {"slug": p["slug"]}


if __name__ == "__main__":
    freezer.freeze()
    print("Built site into ./build")
