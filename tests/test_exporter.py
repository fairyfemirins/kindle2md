import pytest
from kindle2md.exporter import export_to_markdown
from kindle2md.parser import Book, Highlight
import tempfile
import os

def test_export_to_markdown():
    books = [
        Book(
            title="Test Book",
            author="Test Author",
            highlights=[Highlight(text="Test highlight", page="42", location="123")],
        )
    ]
    with tempfile.TemporaryDirectory() as tmpdir:
        output_dir = os.path.join(tmpdir, "output")
        export_to_markdown(books, "obsidian.md", output_dir)
        output_path = os.path.join(output_dir, "Test_Book.md")
        assert os.path.exists(output_path)
        content = open(output_path, "r", encoding="utf-8").read()
        assert "# Test Book" in content
        assert "Test highlight" in content
        assert "Page 42" in content