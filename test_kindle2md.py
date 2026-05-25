#!/usr/bin/env python3
"""
Unit tests for Kindle2MD parser.
"""

import unittest
import os
import tempfile
from kindle2md import parse_clippings, generate_markdown


class TestKindle2MD(unittest.TestCase):
    def setUp(self):
        self.test_clippings = """The Pragmatic Programmer (Andrew Hunt, David Thomas)
- Your Highlight on Location 123-124 | Added on Monday, May 25, 2026, 10:00:00 AM

The most damaging phrase in the language is “We’ve always done it this way!”
==========

原子习惯 (James Clear)
- Your Highlight on 位置 456-457 | Added on Monday, May 25, 2026, 10:01:00 AM

You do not rise to the level of your goals. You fall to the level of your systems.
=========="""
        
        self.expected_clippings = [
            {
                'book_title': 'The Pragmatic Programmer',
                'author': 'Andrew Hunt, David Thomas',
                'location': '123-124',
                'date': 'Monday, May 25, 2026, 10:00:00 AM',
                'text': 'The most damaging phrase in the language is “We’ve always done it this way!”'
            },
            {
                'book_title': '原子习惯',
                'author': 'James Clear',
                'location': '456-457',
                'date': 'Monday, May 25, 2026, 10:01:00 AM',
                'text': 'You do not rise to the level of your goals. You fall to the level of your systems.'
            }
        ]

    def test_parse_clippings(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as f:
            f.write(self.test_clippings)
            f.flush()
            
            clippings = parse_clippings(f.name)
            self.assertEqual(len(clippings), 2)
            self.assertEqual(clippings[0]['book_title'], self.expected_clippings[0]['book_title'])
            self.assertEqual(clippings[0]['text'], self.expected_clippings[0]['text'])
            self.assertEqual(clippings[1]['book_title'], self.expected_clippings[1]['book_title'])
            self.assertEqual(clippings[1]['text'], self.expected_clippings[1]['text'])
            
            os.unlink(f.name)

    def test_generate_markdown(self):
        with tempfile.TemporaryDirectory() as output_dir:
            generate_markdown(self.expected_clippings, output_dir)
            
            # Check if files are created
            self.assertTrue(os.path.exists(os.path.join(output_dir, 'The Pragmatic Programmer.md')))
            self.assertTrue(os.path.exists(os.path.join(output_dir, '原子习惯.md')))


if __name__ == "__main__":
    unittest.main()