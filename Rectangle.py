from dataclasses import dataclass

@dataclass
class Rectangle:
    # Dimensions
    width_mm: float = 0.0
    length_mm: float = 0.0

    # Position (Origin at bottom left)
    bottom_left_x_mm: float = 0.0
    bottom_left_y_mm: float = 0.0

    @property
    def area(self) -> float:
        return self.width_mm * self.length_mm
