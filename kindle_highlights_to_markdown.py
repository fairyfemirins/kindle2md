#!/usr/bin/env python3
import re
import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

@dataclass
class Highlight:
    book_title: str
    author: str
    text: str
    location: str
    timestamp: str
    note: Optional[str] = None

def parse_clippings(file_path: str) -> List[Highlight]:
    with open(file_path, "r", encoding="utf-8-sig") as f:
        content = f.read()

    entries = re.split(r"==========\n", content)
    highlights = []

    for entry in entries:
        if not entry.strip():
            continue
        lines = entry.strip().split("\n")
        if len(lines) < 3:
            continue

        book_line = lines[0]
        book_match = re.match(r"^(.*?)\s*\((.*?)\)$", book_line)
        if not book_match:
            continue
        book_title, author = book_match.groups()

        meta_line = lines[1]
        meta_match = re.match(
            r"- Your (Highlight|Note) (?:on page \d+ \| )?Location (\d+-\d+|\d+) \| Added on (.*)",
            meta_line,
        )
        if not meta_match:
            continue
        highlight_type, location, timestamp = meta_match.groups()

        text = "\n".join(lines[2:]).strip()

        if highlight_type == "Note":
            highlights.append(Highlight(book_title, author, "", location, timestamp, text))
        else:
            highlights.append(Highlight(book_title, author, text, location, timestamp))

    return highlights

def generate_markdown(highlights: List[Highlight], output_dir: str) -> None:
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    books = {}
    for highlight in highlights:
        if highlight.book_title not in books:
            books[highlight.book_title] = []
        books[highlight.book_title].append(highlight)

    for book_title, book_highlights in books.items():
        safe_title = "".join(c if c.isalnum() else "_" for c in book_title)
        md_path = Path(output_dir) / f"{safe_title}.md"

        with open(md_path, "w", encoding="utf-8") as f:
            f.write("---\n")
            f.write(f"title: '{book_title}'\n")
            f.write(f"author: '{book_highlights[0].author}'\n")
            f.write("---\n\n")

            for highlight in book_highlights:
                if highlight.text:
                    f.write(f"## Highlight (Location {highlight.location})\n")
                    f.write(f"*{highlight.timestamp}*\n\n")
                    f.write(f"{highlight.text}\n\n")
                if highlight.note:
                    f.write(f"## Note (Location {highlight.location})\n")
                    f.write(f"*{highlight.timestamp}*\n\n")
                    f.write(f"{highlight.note}\n\n")

def main():
    parser = argparse.ArgumentParser(description="Convert Kindle 'My Clippings.txt' to Markdown.")
    parser.add_argument("clippings_file", help="Path to 'My Clippings.txt'")
    parser.add_argument("output_dir", help="Directory to save Markdown files")
    args = parser.parse_args()

    print("Parsing clippings...")
    highlights = parse_clippings(args.clippings_file)
    print(f"Found {len(highlights)} highlights/notes.")

    print("Generating Markdown...")
    generate_markdown(highlights, args.output_dir)
    print(f"Done! Files saved to {args.output_dir}")

if __name__ == "__main__":
    main()