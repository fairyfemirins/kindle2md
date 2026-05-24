#!/usr/bin/env python3
"""
kindle2md: Convert Kindle "My Clippings.txt" to structured Markdown.

Usage:
  python3 kindle2md.py /path/to/My\ Clippings.txt output.md

Output Format:
  # Book Title (Author)
  > Highlight text
  - Location: 123 | Added: YYYY-MM-DD HH:MM:SS
"""

import re
import sys
from datetime import datetime
from pathlib import Path


class KindleHighlight:
    """Represents a single Kindle highlight or note."""

    def __init__(self, book_title, author, text, location, timestamp):
        self.book_title = book_title.strip()
        self.author = author.strip()
        self.text = text.strip()
        self.location = location.strip()
        self.timestamp = timestamp.strip()

    def to_markdown(self):
        """Convert the highlight to Markdown format."""
        timestamp = datetime.strptime(self.timestamp, "%A, %B %d, %Y, %I:%M:%S %p").strftime("%Y-%m-%d %H:%M:%S")
        return (
            f"## {self.book_title} ({self.author})\n"
            f"> {self.text}\n"
            f"- Location: {self.location} | Added: {timestamp}\n"
        )


def parse_clippings(file_path):
    """Parse Kindle "My Clippings.txt" file into a list of KindleHighlight objects."""
    with open(file_path, "r", encoding="utf-8-sig") as file:
        content = file.read()

    # Split into entries (separated by "==========")
    entries = re.split(r"\n=+\n", content)
    highlights = []

    for entry in entries:
        if not entry.strip():
            continue

        # Extract book title, author, metadata, and text
        lines = entry.strip().split("\n")
        if len(lines) < 4:
            continue

        book_title, author = lines[0].rsplit(" (", 1)
        author = author.rstrip(")")
        metadata = lines[1].strip()
        text = "\n".join(lines[3:])

        # Extract location and timestamp
        location_match = re.search(r"Location (\d+)", metadata)
        timestamp_match = re.search(r"Added on (.+)", metadata)

        if not location_match or not timestamp_match:
            continue

        location = location_match.group(1)
        timestamp = timestamp_match.group(1)

        highlights.append(KindleHighlight(book_title, author, text, location, timestamp))

    return highlights


def write_markdown(highlights, output_path):
    """Write highlights to a Markdown file, grouped by book."""
    books = {}
    for highlight in highlights:
        if highlight.book_title not in books:
            books[highlight.book_title] = []
        books[highlight.book_title].append(highlight)

    with open(output_path, "w", encoding="utf-8") as file:
        for book_title, book_highlights in books.items():
            file.write(f"# {book_title} ({book_highlights[0].author})\n\n")
            for highlight in book_highlights:
                file.write(highlight.to_markdown().split("\n")[1] + "\n\n")


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 kindle2md.py /path/to/My\\ Clippings.txt output.md")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    if not input_path.exists():
        print(f"Error: Input file '{input_path}' not found.")
        sys.exit(1)

    highlights = parse_clippings(input_path)
    write_markdown(highlights, output_path)
    print(f"Successfully converted {len(highlights)} highlights to '{output_path}'.")


if __name__ == "__main__":
    main()