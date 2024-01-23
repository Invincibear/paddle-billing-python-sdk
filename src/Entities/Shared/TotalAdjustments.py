from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Shared.CurrencyCode import CurrencyCode


@dataclass
class TotalAdjustments:
    subtotal:     str
    tax:          str
    total:        str
    fee:          str
    earnings:     str
    currencyCode: CurrencyCode


    @staticmethod
    def from_dict(data: dict) -> TotalAdjustments:
        return TotalAdjustments(
            subtotal     = data['subtotal'],
            tax          = data['tax'],
            total        = data['total'],
            fee          = data['fee'],
            earnings     = data['earnings'],
            currencyCode = CurrencyCode(data['currency_code']),
        )
