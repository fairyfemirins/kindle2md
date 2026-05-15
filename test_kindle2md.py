import pytest
from kindle2md import parse_clippings, generate_markdown
from pathlib import Path
import shutil


def test_parse_clippings():
    # Create a test clippings file
    test_content = """The Pragmatic Programmer (Andrew Hunt)
- Your Highlight on Location 123-124 | Added on Monday, January 1, 2024 12:00:00 PM

This is a highlight.\n==========\nThe Pragmatic Programmer (Andrew Hunt)
- Your Note on Location 123 | Added on Monday, January 1, 2024 12:00:00 PM

This is a note.\n==========\n"""
    
    test_file = "test_clippings.txt"
    with open(test_file, 'w', encoding='utf-8-sig') as file:
        file.write(test_content)
    
    books = parse_clippings(test_file)
    assert len(books) == 1
    assert "The Pragmatic Programmer" in books
    assert books["The Pragmatic Programmer"]["author"] == "Andrew Hunt"
    assert len(books["The Pragmatic Programmer"]["highlights"]) == 2
    
    # Clean up
    Path(test_file).unlink()


def test_generate_markdown():
    books = {
        "Test Book": {
            "author": "Test Author",
            "highlights": [
                {"content": "Test highlight", "location": "123", "type": "highlight"},
                {"content": "Test note", "location": "123", "type": "note"}
            ]
        }
    }
    
    output_dir = "test_output"
    generate_markdown(books, output_dir)
    
    # Check if file was created
    output_file = Path(output_dir) / "Test Book.md"
    assert output_file.exists()
    
    # Check content
    with open(output_file, 'r', encoding='utf-8') as file:
        content = file.read()
    assert "# Test Book" in content
    assert "Test highlight" in content
    assert "Test note" in content
    
    # Clean up
    shutil.rmtree(output_dir)


if __name__ == "__main__":
    pytest.main(["-v"])