from dataclasses import dataclass

@dataclass
class Rectangle:
    width_mm: float
    length_mm: float
    x: float = 0.0
    y: float = 0.0

    @property
    def area(self) -> float:
        return self.width_mm * self.length_mm
