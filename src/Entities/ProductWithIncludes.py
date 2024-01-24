from __future__  import annotations
from dataclasses import dataclass
from datetime    import datetime
from typing      import Optional

from src.Entities.Entity import Entity

from src.Entities.Collections.PriceWithIncludesCollection import PriceWithIncludesCollection  # TODO

from src.Entities.Shared.CatalogType import CatalogType
from src.Entities.Shared.CustomData  import CustomData
from src.Entities.Shared.Status      import Status
from src.Entities.Shared.TaxCategory import TaxCategory


@dataclass
class ProductWithIncludes(Entity):
    id:           str
    name:         str
    description:  Optional[str]
    type:         CatalogType | None
    tax_category: TaxCategory
    image_url:    Optional[str]
    custom_data:  CustomData | None
    status:       Status
    created_at:   datetime | None
    prices:       PriceWithIncludesCollection


    @classmethod
    def from_dict(cls, data: dict) -> ProductWithIncludes:
        return ProductWithIncludes(
            id           = data['id'],
            name         = data['name'],
            description  = data.get('description'),
            type         = CatalogType(data['type']) if 'type' in data else None,
            tax_category = TaxCategory(data['tax_category']),
            image_url    = data.get('image_url'),
            custom_data  = CustomData(data['custom_data']) if 'custom_data' in data else None,
            status       = Status(data['status']),
            created_at   = datetime.fromisoformat(data['created_at']) if 'created_at' in data else None,
            prices       = PriceWithIncludesCollection.from_list(data['prices']),
        )
