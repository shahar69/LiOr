import json
import os
import sys
import tempfile
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.store_manager import Store, Product

class StoreManagerTests(unittest.TestCase):
    def test_add_product(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            store_file = os.path.join(tmpdir, "store.json")
            store = Store(store_file)
            store.add_product(Product(id=1, name="Item", price=9.99))
            store.add_product(Product(id=2, name="Widget", price=4.50))

            with open(store_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            self.assertEqual(len(data), 2)
            self.assertEqual(data[0]["name"], "Item")
            self.assertEqual(data[1]["price"], 4.50)

if __name__ == "__main__":
    unittest.main()
