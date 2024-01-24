from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Shared.CountryCode import CountryCode
from src.Entities.Shared.Money       import Money


@dataclass
class UnitPriceOverride:
    country_codes: list[CountryCode]
    unit_price:    Money


    @staticmethod
    def from_dict(data: dict) -> UnitPriceOverride:
        return UnitPriceOverride(
            country_codes = [CountryCode(code) for code in data['country_codes']],
            unit_price    = Money.from_dict(data['unit_price'])
        )
