import click
from .parser import parse_clippings
from .exporter import export_to_markdown
import os

@click.command()
@click.option("--input", type=click.Path(exists=True), required=True, help="Path to My Clippings.txt")
@click.option("--output-dir", type=click.Path(), required=True, help="Output directory for markdown files")
@click.option("--format", type=click.Choice(["obsidian", "notion", "logseq"]), default="obsidian", help="Output format")
def cli(input, output_dir, format):
    books = parse_clippings(input)
    export_to_markdown(books, f"{format}.md", output_dir)
    click.echo(f"Exported {len(books)} books to {output_dir}")

if __name__ == "__main__":
    cli()