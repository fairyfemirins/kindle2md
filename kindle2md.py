#!/usr/bin/env python3
"""
Kindle2MD: Autonomous Kindle Clippings to Markdown Converter

Parses Kindle "My Clippings.txt" into structured Markdown notes.
"""

import re
import sys
import os
from datetime import datetime
from typing import List, Dict, Optional


def parse_clippings(file_path: str) -> List[Dict]:
    """Parse Kindle "My Clippings.txt" into structured data."""
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    
    # Split clippings by separator
    entries = content.split('==========')
    clippings = []
    
    for entry in entries:
        entry = entry.strip()
        if not entry:
            continue
        
        # Parse book title and author
        title_author_line = entry.split('\n')[0].strip()
        title_author_match = re.match(r'^(.+) \((.+)\)$', title_author_line)
        if not title_author_match:
            title_author_match = re.match(r'^(.+)$', title_author_line)
            if not title_author_match:
                continue
            book_title = title_author_match.group(1)
            author = "Unknown Author"
        else:
            book_title, author = title_author_match.groups()
        
        # Parse metadata (location, date)
        meta_line = entry.split('\n')[1].strip()
        meta_match = re.match(
            r'^- Your (?:Highlight|Note|Bookmark) on (?:Location|位置|Page) ([^|]+)(?: \| Added on (.*))?$',
            meta_line
        )
        if not meta_match:
            continue
        location = meta_match.group(1).strip()
        date = meta_match.group(2).strip() if meta_match.group(2) else "Unknown Date"
        
        # Parse highlight text
        text_lines = entry.split('\n')[2:]
        text = '\n'.join([line.strip() for line in text_lines if line.strip()])
        
        clippings.append({
            'book_title': book_title,
            'author': author,
            'location': location,
            'date': date,
            'text': text
        })
    
    return clippings


def generate_markdown(clippings: List[Dict], output_dir: str) -> None:
    """Generate Markdown files from parsed clippings."""
    os.makedirs(output_dir, exist_ok=True)
    
    # Group clippings by book
    books = {}
    for clipping in clippings:
        book_key = (clipping['book_title'], clipping['author'])
        if book_key not in books:
            books[book_key] = []
        books[book_key].append(clipping)
    
    # Write one Markdown file per book
    for (book_title, author), book_clippings in books.items():
        # Sanitize filename (preserve non-ASCII characters)
        safe_title = "".join(c if c.isalnum() or c in (' ', '_', '-') else '_' for c in book_title).strip('_')
        output_path = os.path.join(output_dir, f"{safe_title}.md")
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(f"# {book_title}\n")
            f.write(f"**Author**: {author}\n\n")
            f.write("---\n\n")
            
            for clipping in book_clippings:
                f.write(f"> {clipping['text']}\n\n")
                f.write(f"- *Location*: {clipping['location']} | *Added on*: {clipping['date']}\n\n")


def main():
    if len(sys.argv) != 3:
        print("Usage: python kindle2md.py <input_file> <output_dir>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_dir = sys.argv[2]
    
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
    
    clippings = parse_clippings(input_file)
    generate_markdown(clippings, output_dir)
    print(f"Successfully converted {len(clippings)} clippings to Markdown in '{output_dir}'.")


if __name__ == "__main__":
    main()