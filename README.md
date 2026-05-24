# kindle2md

Convert Kindle "My Clippings.txt" to structured Markdown with metadata.

## Features
- **Batch processing**: Convert all highlights in one run.
- **Metadata**: Preserve location and timestamp for each highlight.
- **Extensible**: Output is compatible with Obsidian, Notion, and Anki.
- **CLI-based**: Automate Kindle highlight conversion.

## Installation
```bash
pip install -r requirements.txt  # None required for basic usage
```

## Usage
```bash
python3 kindle2md.py /path/to/My\ Clippings.txt output.md
```

## Example Output
```markdown
# The Pragmatic Programmer (Andrew Hunt, David Thomas)

> The most damaging phrase in the language is “We’ve always done it this way!”
- Location: 123 | Added: 2026-05-23 09:30:21

# Atomic Habits (James Clear)

> You do not rise to the level of your goals. You fall to the level of your systems.
- Location: 456 | Added: 2026-05-24 10:15:47
```

## Technical Architecture
1. **Parser**: Splits `My Clippings.txt` into entries using `==========` separators.
2. **Extractor**: Uses regex to extract book title, author, location, and timestamp.
3. **Formatter**: Converts highlights to Markdown with metadata.
4. **Writer**: Groups highlights by book and writes to a single Markdown file.

## License
MIT