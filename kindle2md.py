#!/usr/bin/env python3
"""
kindle2md: A CLI tool to convert Kindle highlights to Markdown.

Usage:
    python kindle2md.py /path/to/My\ Clippings.txt --output highlights.md
"""

import re
import click
from pathlib import Path
from typing import List, Dict, Optional


class KindleHighlight:
    """Represents a single Kindle highlight or note."""
    
    def __init__(self, book_title: str, content: str, location: str, timestamp: str):
        self.book_title = book_title
        self.content = content
        self.location = location
        self.timestamp = timestamp
    
    def to_markdown(self) -> str:
        """Convert the highlight to Markdown."""
        return f"> {self.content}\n\n*Location: {self.location} | Added on: {self.timestamp}*\n"


def parse_clippings(file_path: Path) -> Dict[str, List[KindleHighlight]]:
    """Parse Kindle's 'My Clippings.txt' file into a dictionary of highlights."""
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        content = file.read()
    
    # Split into individual clippings
    clippings = re.split(r'==========\n', content)
    clippings = [c.strip() for c in clippings if c.strip()]
    
    highlights = {}
    
    for clipping in clippings:
        # Parse book title, content, location, and timestamp
        lines = clipping.split('\n')
        if len(lines) < 4:
            continue
        
        book_title = lines[0].strip()
        metadata = lines[1].strip()
        content = '\n'.join(lines[3:]).strip().replace('==========', '').strip()
        
        # Extract location and timestamp
        location_match = re.search(r'Location (\d+-\d+|\d+)', metadata)
        timestamp_match = re.search(r'Added on (.+)', metadata)
        
        location = location_match.group(1) if location_match else "Unknown"
        timestamp = timestamp_match.group(1) if timestamp_match else "Unknown"
        
        # Add to dictionary
        if book_title not in highlights:
            highlights[book_title] = []
        highlights[book_title].append(KindleHighlight(book_title, content, location, timestamp))
    
    return highlights


def highlights_to_markdown(highlights: Dict[str, List[KindleHighlight]]) -> str:
    """Convert highlights dictionary to Markdown."""
    markdown = ""
    
    for book_title, book_highlights in highlights.items():
        markdown += f"# {book_title}\n\n"
        for highlight in book_highlights:
            markdown += highlight.to_markdown() + "\n"
    
    return markdown


@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--output', '-o', type=click.Path(), help='Output Markdown file. If not provided, prints to stdout.')
def cli(input_file: str, output: Optional[str]):
    """Convert Kindle highlights to Markdown."""
    input_path = Path(input_file)
    highlights = parse_clippings(input_path)
    markdown = highlights_to_markdown(highlights)
    
    if output:
        output_path = Path(output)
        output_path.write_text(markdown, encoding='utf-8')
        click.echo(f"Successfully wrote highlights to {output_path}")
    else:
        click.echo(markdown)


if __name__ == '__main__':
    cli()