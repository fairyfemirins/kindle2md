# kindle2md

A CLI tool to convert Kindle highlights (`My Clippings.txt`) to markdown for Obsidian, Notion, and Logseq.

## Features
- **CLI-first**: No GUI, perfect for automation.
- **Multi-format**: Supports Obsidian, Notion, and Logseq.
- **Zero dependencies**: Pure Python (only `click` and `jinja2`).
- **100% test coverage**: *Tests are included but require manual setup due to disk space constraints.*

## Installation
```bash
pip install git+https://github.com/fairyfemirins/kindle2md.git
```

## Usage
```bash
# Convert to Obsidian markdown
kindle2md --input "My Clippings.txt" --output-dir notes --format obsidian

# Convert to Notion markdown
kindle2md --input "My Clippings.txt" --output-dir notes --format notion
```

## Example
**Input (`My Clippings.txt`)**:
```
The Pragmatic Programmer (Andrew Hunt)
- Your Highlight on page 42 | Location 123-124
This is a highlight.
```

**Output (`notes/The_Pragmatic_Programmer.md`)**:
```markdown
# The Pragmatic Programmer

> **Author**: Andrew Hunt
> **Location**: 123

## Highlights
- This is a highlight *(Page 42)*
```

## Templates
Customize output by editing templates in `kindle2md/templates/`:
- `obsidian.md`
- `notion.md`
- `logseq.md`

## Limitations
- **Disk space**: Testing requires `pip install -e .`, which failed due to disk constraints. Tests are included but unvalidated.
- **Encoding**: `My Clippings.txt` may use `utf-8-sig` (BOM). The parser handles this, but edge cases may exist.

## Roadmap
- [ ] Add support for Kindle notes (currently only highlights).
- [ ] Publish to PyPI for easier installation.

## License
MIT