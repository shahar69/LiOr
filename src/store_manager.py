import json
import os
from dataclasses import dataclass, asdict
from typing import List

@dataclass
class Product:
    id: int
    name: str
    price: float

class Store:
    def __init__(self, path: str):
        self.path = path
        self.products: List[Product] = []
        self.load()

    def load(self) -> None:
        if os.path.exists(self.path):
            with open(self.path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            self.products = [Product(**p) for p in data]
        else:
            self.products = []

    def save(self) -> None:
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump([asdict(p) for p in self.products], f, indent=2)

    def add_product(self, product: Product) -> None:
        if any(p.id == product.id for p in self.products):
            raise ValueError(f"Product with id {product.id} already exists")
        self.products.append(product)
        self.save()

    def list_products(self) -> List[Product]:
        return list(self.products)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Manage simple store inventory")
    parser.add_argument("store_file", help="Path to store JSON file")
    parser.add_argument("--add", dest="product_file", help="JSON file with products to add")
    args = parser.parse_args()

    store = Store(args.store_file)

    if args.product_file:
        with open(args.product_file, 'r', encoding='utf-8') as f:
            products = json.load(f)
        for item in products:
            p = Product(**item)
            store.add_product(p)

    for p in store.list_products():
        print(f"{p.id}: {p.name} - ${p.price:.2f}")
