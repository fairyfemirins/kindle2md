# kindle2md

A CLI tool to convert Kindle highlights (`My Clippings.txt`) to Markdown.

![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.8+-green.svg)

## Features
- Parse Kindle's `My Clippings.txt` file.
- Convert highlights and notes to Markdown.
- Group highlights by book.
- Output to a file or stdout.

## Installation

```bash
pip install click
```

Clone the repository:

```bash
git clone https://github.com/Femirins/kindle2md.git
cd kindle2md
```

## Usage

### Basic Usage

```bash
python kindle2md.py /path/to/My\ Clippings.txt --output highlights.md
```

### Print to stdout

```bash
python kindle2md.py /path/to/My\ Clippings.txt
```

## Example

### Input (`My Clippings.txt`)

```
The Pragmatic Programmer: Your Journey to Mastery (Andrew Hunt)
- Your Highlight on Location 123-124 | Added on Friday, May 15, 2026 12:26:00 AM

Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it.
==========
```

### Output (`highlights.md`)

```markdown
# The Pragmatic Programmer: Your Journey to Mastery (Andrew Hunt)

> Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it.

*Location: 123-124 | Added on: Friday, May 15, 2026 12:26:00 AM*
```

## Technical Architecture

### Overview
- **Input**: `My Clippings.txt` (Kindle's default highlights file).
- **Output**: Markdown file or stdout.
- **Libraries**: `click` (CLI), `re` (parsing), `pathlib` (file handling).

### Parsing Logic
1. Split the input file into individual clippings using the `==========` separator.
2. Extract the book title, metadata (location, timestamp), and content for each clipping.
3. Convert each clipping to a `KindleHighlight` object.
4. Group highlights by book title.
5. Convert the grouped highlights to Markdown.

### Output Format
- Book titles are rendered as Markdown headings (`#`).
- Highlights are rendered as blockquotes (`>`).
- Metadata (location, timestamp) is rendered as italicized text.

## Reproducible Tutorial

### Step 1: Set Up

```bash
mkdir -p ~/kindle_highlights && cd ~/kindle_highlights
git clone https://github.com/Femirins/kindle2md.git
cd kindle2md
```

### Step 2: Create a Test File

```bash
cat > test_clippings.txt << 'EOF'
The Pragmatic Programmer: Your Journey to Mastery (Andrew Hunt)
- Your Highlight on Location 123-124 | Added on Friday, May 15, 2026 12:26:00 AM

Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it.
==========
EOF
```

### Step 3: Run the Tool

```bash
python kindle2md.py test_clippings.txt --output highlights.md
```

### Step 4: Verify the Output

```bash
cat highlights.md
```

Expected Output:

```markdown
# The Pragmatic Programmer: Your Journey to Mastery (Andrew Hunt)

> Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it.

*Location: 123-124 | Added on: Friday, May 15, 2026 12:26:00 AM*
```

## License

MIT License. See [LICENSE](LICENSE) for details.