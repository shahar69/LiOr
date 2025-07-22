import unittest
from src.process_text import process_text

class ProcessTextTests(unittest.TestCase):
    def test_reverse_words(self):
        self.assertEqual(process_text("Hello, World!"), "world hello")

if __name__ == "__main__":
    unittest.main()
