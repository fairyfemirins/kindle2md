# kindle2md

Convert Kindle highlights (`My Clippings.txt`) to Markdown.

## Features
- Parses `My Clippings.txt` (Kindle's default export format).
- Outputs one Markdown file per book.
- Preserves metadata (location, date) as footnotes.
- Supports Obsidian/Logseq-friendly formatting.

## Usage

```bash
pip install kindle2md
kindle2md --input "My Clippings.txt" --output "highlights/"
```

## Installation

```bash
pip install git+https://github.com/femirins/kindle2md.git
```

## Example

**Input (`My Clippings.txt`)**:
```
The Pragmatic Programmer (Andrew Hunt)
- Your Highlight on Location 123-124 | Added on Friday, May 15, 2026 03:21 PM

Debugging is twice as hard as writing the code in the first place.
==========
```

**Output (`The Pragmatic Programmer.md`)**:
```markdown
# The Pragmatic Programmer

- Debugging is twice as hard as writing the code in the first place. [[1]](#fn1)

---

1. Location 123-124 | Added on Friday, May 15, 2026 03:21 PM [↩](#fnref1)
```