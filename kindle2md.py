"""
Kindle Highlights to Markdown Converter

Parses Kindle's 'My Clippings.txt' and converts highlights/notes to Markdown.
Usage:
    kindle2md --input "My Clippings.txt" --output "highlights/"
"""

import re
import argparse
from pathlib import Path
from typing import List, Dict


def parse_clippings(file_path: str) -> Dict[str, List[Dict]]:
    """Parse Kindle clippings file into structured data."""
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        content = file.read()
    
    # Split into entries (separated by "==========")
    entries = re.split(r'\r?\n==========\r?\n', content)
    books = {}
    
    for entry in entries:
        if not entry.strip():
            continue
        
        # Extract book title, metadata, and content
        lines = entry.strip().split('\n')
        if len(lines) < 3:
            continue
        
        title_author = lines[0].strip()
        metadata = lines[1].strip()
        content = '\n'.join(lines[2:]).strip()
        
        # Extract book title and author
        title_match = re.match(r'^(.*?)(?: \((.*?)\))?$', title_author)
        if not title_match:
            continue
        title = title_match.group(1).strip()
        author = title_match.group(2).strip() if title_match.group(2) else "Unknown"
        
        # Extract location and type (highlight/note)
        location_match = re.search(r'Location (\d+)(?:-(\d+))?', metadata)
        if not location_match:
            continue
        location = location_match.group(1)
        highlight_type = "note" if "Your Note" in metadata else "highlight"
        
        # Store in structured format
        if title not in books:
            books[title] = {
                "author": author,
                "highlights": []
            }
        
        books[title]["highlights"].append({
            "content": content,
            "location": location,
            "type": highlight_type
        })
    
    return books


def generate_markdown(books: Dict[str, Dict], output_dir: str) -> None:
    """Generate Markdown files from parsed clippings."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    for title, data in books.items():
        md_content = f"# {title}\n\n**Author:** {data['author']}\n\n## Highlights\n"
        for highlight in data["highlights"]:
            if highlight["type"] == "highlight":
                md_content += f"- \"{highlight['content']}\" (Location: {highlight['location']})\n"
            else:
                md_content += f"- **Note:** {highlight['content']} (Location: {highlight['location']})\n"
        
        # Write to file
        safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '-')).rstrip()
        file_path = output_path / f"{safe_title}.md"
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(md_content)


def main():
    parser = argparse.ArgumentParser(description='Convert Kindle highlights to Markdown.')
    parser.add_argument('--input', type=str, required=True, help='Path to My Clippings.txt')
    parser.add_argument('--output', type=str, required=True, help='Output directory for Markdown files')
    args = parser.parse_args()
    
    books = parse_clippings(args.input)
    generate_markdown(books, args.output)
    print(f"Generated {len(books)} Markdown files in {args.output}")


if __name__ == "__main__":
    main()