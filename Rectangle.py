from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Rectangle:
    width_mm: Decimal
    length_mm: Decimal

    @property
    def area(self) -> Decimal:
        return self.width_mm * self.length_mm
