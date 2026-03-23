My academic website
===================

Visit it at [academia.skadge.org](https://academia.skadge.org)

## Zola Migration

This branch (`ssg/zola`) contains the port of the website to the [Zola](https://www.getzola.org/) static site generator.

### Building the site

1. Install Zola (single binary).
2. Run `zola build` to generate the static site in `public/`.
3. Run `zola serve` to start a local development server with live reload.

### Content Management

- **News**: Add new markdown files in `content/news/`. Use the format `YYYY-MM-slug.md`.
  ```toml
  +++
  title = "My News Title"
  date = 2021-07-01
  [extra]
  image = "my-image.jpg" # located in static/images/
  position = "left" # or "right"
  +++
  Content here...
  ```
- **Pages**: Edit markdown files in `content/` (e.g., `aboutme.md`, `research.md`).
- **Publications**: Generated from `static/publications.json`. To add a paper, use the helper script (it fetches metadata from Crossref):
  ```bash
  python3 add_paper.py 10.1007/s12369-025-01330-6 --pdf publis/myfile.pdf
  ```
- **Talks**: Generated from `static/talks.json`. Drop your presentation PDF into `static/talks/` and run the helper script (it auto-generates a poster thumbnail):
  ```bash
  python3 add_talk.py --pdf static/talks/mypres.pdf --title "My Talk" --date 2026-03-04 --venue "HRI 2026" --summary "Quick summary"
  ```

### Directory Structure

- `content/`: Markdown content.
- `templates/`: HTML templates (Tera engine).
- `static/`: Static assets (images, CSS, JS, publications.json).
- `sass/`: SASS stylesheets (compiled by Zola).
- `config.toml`: Site configuration.
