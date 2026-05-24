# kindle2md

**Convert Kindle highlights to Markdown for Obsidian, Notion, or blogs.**

## Features
- Parses `My Clippings.txt` into structured data (Book, Highlight objects).
- Exports highlights to **Markdown** with metadata (location, date, page).
- Supports notes, Unicode, and batch processing.
- CLI for easy use.

## Installation
```bash
git clone https://github.com/femirins/kindle2md.git
cd kindle2md
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt  # (click)
```

## Usage
```bash
# Parse highlights and generate Markdown
python -m cli parse My\ Clippings.txt --output-dir output/
```

## Example Output
```markdown
# The Fellowship of the Ring

**Author**: J.R.R. Tolkien

> When Mr. Bilbo Baggins of Bag End announced...
> **Location: 100 | Date: 2026-05-23**

---
```

## License
MIT