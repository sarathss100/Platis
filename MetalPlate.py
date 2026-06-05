from dataclasses import dataclass

@dataclass
class MetalPlate:
    width_mm: float
    length_mm: float
    thickness_mm: float = 4.0
    # Default density of structural Steel: 7850 kg/m3
    density_kg_m3: float = 7850.0

    @property
    def area(self) -> float:
        return self.length_mm * self.width_mm
    
    @property
    def volume_mm3(self) -> float:
        return self.length_mm * self.width_mm * self.thickness_mm
    
    @property
    def volume_m3(self) -> float:
        return self.volume_mm3 / 1000000000.0
    
    @property
    def weight(self) -> float:
        return self.volume_m3 * self.density_kg_m3
