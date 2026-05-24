"""
CLI for Kindle Highlights to Markdown

Usage:
  kindle2md parse <input_file> [--output-dir <output_dir>]
"""

import click
from pathlib import Path

from .parser import parse_clippings
from .markdown_generator import generate_markdown


@click.group()
def cli():
    """Kindle Highlights to Markdown CLI"""
    pass


@cli.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--output-dir', default='output', help='Output directory for Markdown files')
def parse(input_file: str, output_dir: str):
    """Parse 'My Clippings.txt' and generate Markdown files."""
    books = parse_clippings(input_file)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for book in books:
        generate_markdown(book, output_dir)
        click.echo(f"Generated Markdown for: {book.title}")

    click.echo(f"Done! Generated {len(books)} Markdown files in {output_path.absolute()}")


if __name__ == '__main__':
    cli()