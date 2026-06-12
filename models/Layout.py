from dataclasses import dataclass, field
from models.MetalPlate import MetalPlate
from models.Rectangle import Rectangle

@dataclass
class Layout:
    plate: MetalPlate
    plates: list[Rectangle] = field(default_factory=list)

    def display(self):
        