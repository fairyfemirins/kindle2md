import re
from dataclasses import dataclass
from typing import List

@dataclass
class Highlight:
    text: str
    page: str
    location: str

@dataclass
class Book:
    title: str
    author: str
    highlights: List[Highlight]

def parse_clippings(file_path: str) -> List[Book]:
    with open(file_path, "r", encoding="utf-8-sig") as f:
        content = f.read()

    books = []
    entries = re.split(r"==========\n", content)
    for entry in entries:
        if not entry.strip():
            continue
        lines = entry.split("\n")
        if len(lines) < 4:
            continue
        title_author = lines[0].strip()
        metadata = lines[1].strip()
        highlight_text = lines[2].strip()  # Third line is the highlight

        # Skip malformed entries
        if title_author.startswith("#") or title_author.startswith("-"):
            continue

        # Extract title/author
        match = re.match(r"^(.*?)(?:\s\((.*?)\))?$", title_author)
        if not match:
            print(f"Skipping malformed title: {title_author}")
            continue
        title, author = match.groups()
        title = title.strip()
        author = author.strip() if author else "Unknown"

        # Extract page/location
        page = re.search(r"page (\d+)", metadata, re.IGNORECASE)
        page = page.group(1) if page else "?"
        location = re.search(r"location (\d+)", metadata, re.IGNORECASE)
        location = location.group(1) if location else "?"

        book = next((b for b in books if b.title == title and b.author == author), None)
        if not book:
            book = Book(title=title, author=author, highlights=[])
            books.append(book)
        book.highlights.append(Highlight(text=highlight_text, page=page, location=location))
    return books