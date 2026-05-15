import re
import click
from pathlib import Path
from typing import Dict, List

def parse_clippings(input_path: str) -> Dict[str, List[str]]:
    """Parse My Clippings.txt into a dict of {book_title: [highlights]}."""
    with open(input_path, "r", encoding="utf-8-sig") as f:
        content = f.read()

    entries = re.split(r"==========\n", content)
    books = {}

    for entry in entries:
        if not entry.strip():
            continue
        lines = entry.strip().split("\n")
        if len(lines) < 3:
            continue
        title = lines[0].strip()
        metadata = lines[1].strip()
        highlight = "\n".join(lines[2:]).strip().replace("==========", "").strip()
        if title not in books:
            books[title] = []
        books[title].append((metadata, highlight))

    return books

def generate_markdown(books: Dict[str, List[str]], output_dir: str) -> None:
    """Generate Markdown files from parsed highlights."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for title, highlights in books.items():
        md_content = f"# {title}\n\n"
        footnotes = []
        for i, (metadata, highlight) in enumerate(highlights, 1):
            md_content += f"- {highlight} [[{i}]](#fn{i})\n\n"
            footnotes.append(f"{i}. {metadata} [↩](#fnref{i})")

        md_content += "---\n\n" + "\n".join(footnotes)
        safe_title = re.sub(r'[\\/*?:"<>|]', "", title)
        with open(output_path / f"{safe_title}.md", "w", encoding="utf-8") as f:
            f.write(md_content)

@click.command()
@click.option("--input", required=True, help="Path to My Clippings.txt")
@click.option("--output", required=True, help="Output directory for Markdown files")
def cli(input: str, output: str) -> None:
    """Convert Kindle highlights to Markdown."""
    books = parse_clippings(input)
    generate_markdown(books, output)
    click.echo(f"Generated {len(books)} Markdown files in {output}/")

if __name__ == "__main__":
    cli()