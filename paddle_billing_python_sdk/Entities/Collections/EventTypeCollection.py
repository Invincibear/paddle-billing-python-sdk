from __future__ import annotations

from paddle_billing_python_sdk.Entities.Collections.Collection import Collection
from paddle_billing_python_sdk.Entities.Collections.Paginator  import Paginator


class EventTypeCollection(Collection):
    @classmethod
    def from_list(cls, items_data: list, paginator: Paginator = None) -> EventTypeCollection:
        from paddle_billing_python_sdk.Entities.EventType import EventType

        items = [EventType.from_dict(item) for item in items_data]

        return EventTypeCollection(items, paginator)


    def __next__(self):
        return super().__next__()
