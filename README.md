# Personal Website

A simple one-page portfolio built with Python (Flask), exported to static HTML
and hosted free on GitHub Pages.

## Edit your content
Everything is in **`content.py`**. Change the text there and refresh the page.
- Add your resume as `static/resume.pdf` and a "Resume" button appears.
- Set any section to `[]` (or `{}` for skills) to hide it.
- Colors and fonts are in `static/style.css`.
- Each project in `PROJECTS` gets its own case-study page at `/projects/<slug>/`,
  built from its `problem`, `approach`, and `results`. To add a chart or screenshot,
  save it in `static/projects/` and set `"image": "projects/your-file.png"`
  (optionally `"image_caption"`).

## Run locally
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py          # open http://127.0.0.1:5000
```

## Deploy for free (GitHub Pages)
1. Create a new public repo on GitHub. Name it `<your-username>.github.io`
   for the cleanest URL, or any name (it'll be at `<your-username>.github.io/<repo>`).
2. Push this folder:
   ```bash
   git init && git add . && git commit -m "Initial site"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<repo>.git
   git push -u origin main
   ```
3. On GitHub: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
4. Every push to `main` rebuilds and redeploys automatically (see the **Actions** tab).

To check the static build locally: `python freeze.py`, then open `build/index.html`.
