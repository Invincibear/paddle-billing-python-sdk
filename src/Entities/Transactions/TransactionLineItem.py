from __future__  import annotations
from dataclasses import dataclass

from src.Entities.ProductWithIncludes import ProductWithIncludes

from src.Entities.Transactions.TransactionProration import TransactionProration

from src.Entities.Shared.Totals     import Totals
from src.Entities.Shared.UnitTotals import UnitTotals


@dataclass
class TransactionLineItem:
    id:          str
    price_id:    str
    quantity:    int
    proration:   TransactionProration | None
    tax_rate:    str
    unit_totals: UnitTotals
    totals:      Totals
    product:     ProductWithIncludes


    @staticmethod
    def from_dict(data: dict) -> TransactionLineItem:
        return TransactionLineItem(
            id          = data['id'],
            price_id    = data['price_id'],
            quantity    = data['quantity'],
            proration   = TransactionProration.from_dict(data['proration']) if 'proration' in data else None,
            tax_rate    = data['tax_rate'],
            unit_totals = UnitTotals.from_dict(data['unit_totals']),
            totals      = Totals.from_dict(data['totals']),
            product     = ProductWithIncludes.from_dict(data['product']),
        )
