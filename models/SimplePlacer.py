from dataclasses import dataclass, field
from models.MetalPlate import MetalPlate
from models.Rectangle import Rectangle

@dataclass
class SimplePlacer:
    plate: MetalPlate
    parts: list[Rectangle] = field(default_factory=list)

    def print(self):
        print(self)