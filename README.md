# Kindle Highlights to Markdown

Convert your Kindle `My Clippings.txt` file into searchable Markdown notebooks — one file per book, with highlights, notes, and metadata.

## Features
- ✅ **Parses Kindle's proprietary format** (`My Clippings.txt`).
- ✅ **Generates clean Markdown** with frontmatter (title, author).
- ✅ **Supports highlights and notes** with timestamps and locations.
- ✅ **Offline-first** — no external APIs or dependencies.
- ✅ **Searchable** — use `ripgrep` or `fzf` to search your highlights.

## Installation
```bash
pip install questionary
git clone https://github.com/femirins/kindle-highlights-to-markdown.git
cd kindle-highlights-to-markdown
```

## Usage
```bash
python3 kindle_highlights_to_markdown.py "My Clippings.txt" output_directory
```

## Example Output
```markdown
---
title: 'The Pragmatic Programmer'
author: 'Andrew Hunt, David Thomas'
---

## Highlight (Location 563-564)
*Saturday, May 23, 2026 10:00:00 AM*

Debugging is twice as hard as writing the code in the first place. So if you're as clever as you can be when you write it, how will you ever debug it?

## Note (Location 564)
*Saturday, May 23, 2026 10:01:00 AM*

This reminds me of the KISS principle. Keep code simple to avoid debugging nightmares.
```

## License
MIT
## Note
This repository was published under \(fairyfemirins\) due to GitHub namespace restrictions. A transfer to femirins is pending.
