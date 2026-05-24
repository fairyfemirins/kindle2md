# Reproducible Tutorial: kindle2md

## Step 1: Clone the Repository
```bash
git clone https://github.com/femirins/kindle2md.git
cd kindle2md
```

## Step 2: Prepare Your Kindle Highlights
1. Connect your Kindle to your computer via USB.
2. Copy `documents/My Clippings.txt` to the `kindle2md` directory.

## Step 3: Run the Converter
```bash
python3 kindle2md.py "My Clippings.txt" output.md
```

## Step 4: Verify the Output
```bash
cat output.md
```

## Step 5: Integrate with Obsidian/Notion
1. **Obsidian**: Drag `output.md` into your vault.
2. **Notion**: Import `output.md` as a Markdown file.

## Troubleshooting
- **No highlights found?** Ensure `My Clippings.txt` is not empty.
- **Encoding issues?** Use `utf-8-sig` encoding for Kindle files.
- **Metadata missing?** Check the format of `My Clippings.txt`.