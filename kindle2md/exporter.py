from jinja2 import Environment, FileSystemLoader
from typing import List
import os
from pathlib import Path
from .parser import Book

def export_to_markdown(books: List[Book], template_name: str, output_dir: str):
    env = Environment(loader=FileSystemLoader(str(Path(__file__).parent / "templates")))
    template = env.get_template(template_name)
    os.makedirs(output_dir, exist_ok=True)

    for book in books:
        output_file = os.path.join(output_dir, f"{book.title.replace('/', '_').replace(' ', '_')}.md")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(template.render(title=book.title, author=book.author, highlights=book.highlights))
        print(f"Exported: {output_file}")