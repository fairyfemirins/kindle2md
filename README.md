# Kindle Highlights to Markdown Converter

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight CLI tool to convert Kindle highlights and notes (`My Clippings.txt`) into clean Markdown files for seamless integration with knowledge bases like Obsidian, Notion, or Logseq.

## Features
- Parses Kindle's `My Clippings.txt` into structured data.
- Generates a Markdown file per book with highlights and notes.
- Supports both highlights and personal notes.
- Simple CLI interface for bulk conversion.

## Installation
```bash
pip install kindle2md
```

## Usage
```bash
kindle2md --input "My Clippings.txt" --output "highlights/"
```

### Example Output
```markdown
# The Pragmatic Programmer

**Author:** Andrew Hunt

## Highlights
- "This is a highlight" (Location: 123)
- **Note:** This is a note (Location: 123)
```

## Technical Architecture
1. **Input Parsing:**
   - Reads `My Clippings.txt` and splits entries by `==========`.
   - Uses regex to extract book title, author, location, and content.
2. **Data Structuring:**
   - Organizes highlights/notes into a dictionary with book titles as keys.
3. **Markdown Generation:**
   - Creates a Markdown file per book with a standardized format.

## Limitations
- Only supports Kindle's default `My Clippings.txt` format.
- Does not handle non-English characters in book titles/authors.

## Future Work
- Add support for Notion/Roam Research/Anki integration.
- Implement a GUI for non-technical users.
- Support for other e-reader formats (Kobo, etc.).

## License
MIT