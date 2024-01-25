from __future__ import annotations

from paddle_billing_python_sdk.Entities.Collections.Collection import Collection
from paddle_billing_python_sdk.Entities.Collections.Paginator  import Paginator


class AdjustmentsAdjustmentCollection(Collection):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator = None) -> AdjustmentsAdjustmentCollection:
        from paddle_billing_python_sdk.Entities.Adjustment import Adjustment

        items = [Adjustment.from_dict(item) for item in items_data]

        return AdjustmentsAdjustmentCollection(items, paginator)


    def __next__(self):
        return super().__next__()
