from __future__ import annotations

from paddle_billing_python_sdk.Entities.Collections.Collection import Collection
from paddle_billing_python_sdk.Entities.Collections.Paginator  import Paginator


class SubscriptionPreviewCollection(Collection):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator = None) -> SubscriptionPreviewCollection:
        from paddle_billing_python_sdk.Entities.SubscriptionPreview import SubscriptionPreview

        items = [SubscriptionPreview.from_dict(item) for item in items_data]

        return SubscriptionPreviewCollection(items, paginator)


    def __next__(self):
        return super().__next__()
