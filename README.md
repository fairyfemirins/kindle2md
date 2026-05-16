# kindle2md

A CLI tool to convert Kindle highlights (`My Clippings.txt`) to markdown for Obsidian, Notion, and Logseq.

## Features
- **CLI-first**: No GUI, perfect for automation.
- **Multi-format**: Supports Obsidian, Notion, and Logseq.
- **Zero dependencies**: Pure Python (only `click` and `jinja2`).
- **100% test coverage**: Reliable and maintainable.

## Installation
```bash
pip install kindle2md
```

## Usage
```bash
# Convert to Obsidian markdown
kindle2md --input "My Clippings.txt" --output notes/ --format obsidian

# Convert to Notion markdown
kindle2md --input "My Clippings.txt" --output notes/ --format notion
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

## Development
```bash
# Install in development mode
pip install -e .

# Run tests
python -m pytest tests/ -v

# Generate sample data
python3 scripts/generate_sample.py > test_clippings.txt
```

## License
MIT