import pytest
from kindle2md.parser import parse_clippings, Book, Highlight
import tempfile
import os

def test_parse_clippings():
    sample = """The Pragmatic Programmer (Andrew Hunt)
- Your Highlight on page 42 | Location 123-124
This is a highlight.

==========
Clean Code (Robert Martin)
- Your Highlight on page 100 | Location 456-457
Another highlight.
"""
    with tempfile.NamedTemporaryFile(mode="w", delete=False, encoding="utf-8") as f:
        f.write(sample)
        f.flush()

    books = parse_clippings(f.name)
    os.unlink(f.name)

    assert len(books) == 2
    assert books[0].title == "The Pragmatic Programmer"
    assert books[0].author == "Andrew Hunt"
    assert len(books[0].highlights) == 1
    assert books[0].highlights[0].text == "This is a highlight."
    assert books[0].highlights[0].page == "42"
    assert books[0].highlights[0].location == "123"

    assert books[1].title == "Clean Code"
    assert books[1].author == "Robert Martin"
    assert len(books[1].highlights) == 1
    assert books[1].highlights[0].text == "Another highlight."