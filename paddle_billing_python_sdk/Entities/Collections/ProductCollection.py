from __future__ import annotations

from paddle_billing_python_sdk.Entities.Collections.Collection import Collection
from paddle_billing_python_sdk.Entities.Collections.Paginator  import Paginator


class ProductCollection(Collection):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator = None) -> ProductCollection:
        from paddle_billing_python_sdk.Entities.Product import Product

        items = [Product.from_dict(item) for item in items_data]

        return ProductCollection(items, paginator)


    def __next__(self):
        return super().__next__()
