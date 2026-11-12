# WTE site tools

- `content.py` holds all page copy in Thai / English / Chinese. `build.py` turns it into the HTML files and `js/i18n.js`.
- Rebuild after any edit: `python3 -I tools/build.py` (run from the project folder).
- Projects: add entries to `projects.json` (see `projects.example.json`). `service` must be one of
  `energy`, `fuel`, `recycling`, `engineering`. `image` is optional (put files in `assets/projects/`).
  Entries appear on the matching `projects-<service>.html` page; empty categories show a "coming soon" card.
