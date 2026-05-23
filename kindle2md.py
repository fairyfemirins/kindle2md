#!/usr/bin/env python3
"""
Kindle Highlights to Markdown Converter

Parses Kindle's "My Clippings.txt" and exports highlights/notes to Markdown files.
Each book gets its own file with highlights grouped by chapter (if available).

Usage:
  python3 kindle2md.py /path/to/My\ Clippings.txt
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple


def parse_clippings(file_path: str) -> Dict[str, List[Tuple[str, str, str]]]:
    """Parse Kindle clippings into a structured format.
    
    Args:
        file_path: Path to "My Clippings.txt".
    
    Returns:
        Dict[book_title, List[(location, highlight_text, note_text)]]
    """
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    
    # Split into entries (separated by "==========")
    entries = re.split(r'==========\s*', content)
    entries = [e.strip() for e in entries if e.strip()]
    
    books = {}
    for entry in entries:
        lines = entry.split('\n')
        if len(lines) < 3:
            continue
        
        # Extract book title and metadata
        book_title = lines[0].strip()
        metadata = lines[1].strip()
        
        # Extract location (e.g., "Location 123-124")
        location_match = re.search(r'Location (\d+)(?:-(\d+))?', metadata)
        if not location_match:
            continue
        location = location_match.group(0)
        
        # Extract highlight/note text
        text = '\n'.join(lines[3:]).strip()
        
        # Separate highlights and notes
        highlight_text = text if "Your Note" not in metadata else ""
        note_text = text if "Your Note" in metadata else ""
        
        if book_title not in books:
            books[book_title] = []
        books[book_title].append((location, highlight_text, note_text))
    
    return books


def export_to_markdown(books: Dict[str, List[Tuple[str, str, str]]], output_dir: str = ".") -> None:
    """Export parsed clippings to Markdown files.
    
    Args:
        books: Parsed clippings from parse_clippings().
        output_dir: Directory to save Markdown files.
    """
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    for book_title, clippings in books.items():
        # Sanitize filename
        safe_title = re.sub(r'[\\/*?:"<>|]', "_", book_title)
        md_file = output_path / f"{safe_title}.md"
        
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(f"# {book_title}\n\n")
            
            for location, highlight, note in clippings:
                if highlight:
                    f.write(f"## Highlight ({location})\n\n{highlight}\n\n")
                if note:
                    f.write(f"## Note ({location})\n\n{note}\n\n")
                f.write("---\n")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 kindle2md.py /path/to/My\\ Clippings.txt")
        sys.exit(1)
    
    clippings_file = sys.argv[1]
    if not Path(clippings_file).exists():
        print(f"Error: File not found: {clippings_file}")
        sys.exit(1)
    
    books = parse_clippings(clippings_file)
    export_to_markdown(books)
    print(f"Exported {len(books)} books to Markdown.")


if __name__ == "__main__":
    main()