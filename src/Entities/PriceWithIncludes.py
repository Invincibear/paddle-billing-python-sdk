from __future__ import annotations
from dataclasses import dataclass

from src.Entities.Entity              import Entity
from src.Entities.ProductWithIncludes import ProductWithIncludes

from src.Entities.Shared.CatalogType       import CatalogType
from src.Entities.Shared.CustomData        import CustomData
from src.Entities.Shared.Money             import Money
from src.Entities.Shared.PriceQuantity     import PriceQuantity
from src.Entities.Shared.Status            import Status
from src.Entities.Shared.TaxMode           import TaxMode
from src.Entities.Shared.TimePeriod        import TimePeriod
from src.Entities.Shared.UnitPriceOverride import UnitPriceOverride


@dataclass
class PriceWithIncludes(Entity):
    id:                   str
    product_id:           str
    name:                 str | None
    description:          str
    type:                 CatalogType | None
    billing_cycle:        TimePeriod | None
    trial_period:         TimePeriod | None
    tax_mode:              TaxMode | None
    unit_price:           Money
    unit_price_overrides: list[UnitPriceOverride]
    quantity:             PriceQuantity
    status:               Status
    custom_data:          CustomData | None
    product:              ProductWithIncludes | None


    @classmethod
    def from_dict(cls, data: dict) -> PriceWithIncludes:
        return PriceWithIncludes(
            id                   = data['id'],
            product_id           = data['product_id'],
            name                 = data.get('name'),
            description          = data['description'],
            type                 = CatalogType(data['type'])                   if 'type'          in data else None,
            billing_cycle        = TimePeriod.from_dict(data['billing_cycle']) if 'billing_cycle' in data else None,
            trial_period         = TimePeriod.from_dict(data['trial_period'])  if 'trial_period'  in data else None,
            tax_mode              = TaxMode(data['tax_mode'])                   if 'tax_mode'      in data else None,
            unit_price           = Money.from_dict(data['unit_price']),
            unit_price_overrides = [UnitPriceOverride.from_dict(override) for override in data.get('unit_price_overrides', [])],
            quantity             = PriceQuantity.from_dict(data['quantity']),
            status               = Status(data['status']),
            custom_data          = CustomData(data['custom_data'])                if 'custom_data' in data else None,
            product              = ProductWithIncludes.from_dict(data['product']) if 'product'     in data else None,
        )
