from __future__    import annotations
from .CurrencyCode import CurrencyCode
from dataclasses   import dataclass
from typing        import Optional


@dataclass
class TransactionTotalsAdjusted:
    subtotal:      str
    tax:           str
    total:         str
    grand_total:   str
    fee:           Optional[str]
    earnings:      Optional[str]
    currency_code: CurrencyCode


    @staticmethod
    def from_dict(data: dict) -> TransactionTotalsAdjusted:
        return TransactionTotalsAdjusted(
            subtotal      = data['subtotal'],
            tax           = data['tax'],
            total         = data['total'],
            grand_total   = data['grand_total'],
            fee           = data.get('fee'),
            earnings      = data.get('earnings'),
            currency_code = CurrencyCode(data['currency_code']),
        )
