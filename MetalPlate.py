from dataclasses import dataclass
from decimal import Decimal

@dataclass
class MetalPlate:
    width_mm: Decimal
    length_mm: Decimal
    thickness_mm: Decimal
    # Default density of structural Steel: 7850 kg/m3
    density_kg_m3: Decimal = Decimal("7850")

    @property
    def area(self):
        return self.length_mm * self.width_mm
    
    @property
    def volume_mm3(self):
        return self.length_mm * self.width_mm * self.thickness_mm
    
    @property
    def volume_m3(self):
        return self.volume_mm3 / Decimal("1000_000_000")
    
    @property
    def weight(self):
        return self.volume_m3 * self.density_kg_m3
    
plate = MetalPlate(
    length_mm=Decimal("2500"),
    width_mm=Decimal("1200"),
    thickness_mm=Decimal("20")
)

print(plate.weight)