import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.process_text import process_text

class ProcessTextTests(unittest.TestCase):
    def test_reverse_words(self):
        self.assertEqual(process_text("Hello, World!"), "world hello")

if __name__ == "__main__":
    unittest.main()
