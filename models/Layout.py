from dataclasses import dataclass, field
from models.MetalPlate import MetalPlate
from models.Rectangle import Rectangle
from utils.geometry_utils import get_rectangle_vertices

@dataclass
class Layout:
    plate: MetalPlate
    plates: list[Rectangle] = field(default_factory=list)

    @property
    def add_part(self, rectangle_plate) -> None:
        # 1. Make sure it actually fits inside the master plate first
        if not self.is_part_inside_plate(self.plate, rectangle_plate):
            print(f"Warning: Part {rectangle_plate} is outside the main plate bounds!")
            return
        
        # 2. Check if it overlaps with any existing pieces
        if not any(self.is_parts_overlapped(shape, rectangle_plate) for shape in self.plates):
            self.plates.append(rectangle_plate)

    @property
    def total_area(self) -> float:
        return self.plate.area

    @property
    def utilization(self) -> float:
        total_plate_area_available = self.plate.area
        total_plate_area_required = 0.0
        for shape in self.plates:
            if self.is_part_inside_plate(self.plate, shape):
                total_plate_area_required += shape.area

        utilization_percentage = total_plate_area_required * 100 / total_plate_area_available
        return round(utilization_percentage, 2)

    @property
    def is_part_inside_plate(self, plate, rectangle) -> bool:
        if rectangle.bottom_left_x_mm < plate.bottom_left_x_mm or \
            rectangle.bottom_left_y_mm < plate.bottom_left_y_mm:
                return False
        
        plate_coordinates = get_rectangle_vertices(plate)
        rectangle_coordinates = get_rectangle_vertices(rectangle)

        return rectangle_coordinates["right-top-corner"][0] <= plate_coordinates["right-top-corner"][0] and \
                rectangle_coordinates["right-top-corner"][1] <= plate_coordinates["right-top-corner"][1]

    @property
    def is_parts_overlapped(self, plate1, plate2, cutting_allowance = 10) -> bool:
        plate1_coordinates = get_rectangle_vertices(plate1)
        plate2_coordinates = get_rectangle_vertices(plate2)

        print(plate1_coordinates)
        print(plate2_coordinates)

        # Check for separation on the x-axis
        # If plate1 is completely to the left of plate2 (with allowance)
        if ((plate1_coordinates["right-bottom-corner"][0] + cutting_allowance) <= plate2_coordinates["left-bottom-corner"][0]):
            return False
        
        # If plate1 is completely to the right of plate2 (with allowance)
        if ((plate1_coordinates["left-bottom-corner"][0] - cutting_allowance) >= plate2_coordinates["right-bottom-corner"][0]):
            return False
        
        # Check for separation on the y-axis
        # If plate1 is completely below plate2 (with allowance)
        if ((plate1_coordinates["left-top-corner"][1] + cutting_allowance) <= plate2_coordinates["left-bottom-corner"][1]): 
            return False

        # If plate1 is completely above plate2 (with allowance)
        if ((plate1_coordinates["left-bottom-corner"][1] - cutting_allowance) >= plate2_coordinates["left-top-corner"][1]):
            return False

        return True