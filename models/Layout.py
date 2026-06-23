from dataclasses import dataclass, field
from models.MetalPlate import MetalPlate
from models.Rectangle import Rectangle

@dataclass
class Layout:
    plate: MetalPlate
    plates: list[Rectangle] = field(default_factory=list)

    def add_part(self, rectangle_plate):
        # 1. Make sure it actually fits inside the master plate first
        if not self.is_part_inside_plate(self.plate, rectangle_plate):
            print(f"Warning: Part {rectangle_plate} is outside the main plate bounds!")
            return
        
        # 2. Check if it overlaps with any existing pieces
        if not any(self.is_parts_overlapped(shape, rectangle_plate) for shape in self.plates):
            self.plates.append(rectangle_plate)

    def total_area(self):
        return self.plate.area

    def utilization(self):
        total_plate_area_available = self.plate.area
        total_plate_area_required = 0.0
        for shape in self.plates:
            if self.is_part_inside_plate(self.plate, shape):
                total_plate_area_required += shape.area

        utilization_percentage = total_plate_area_required * 100 / total_plate_area_available
        return round(utilization_percentage, 2)

    @staticmethod
    def get_rectangle_vertices(plt):
        x0 = plt.bottom_left_x_mm;
        y0 = plt.bottom_left_y_mm;

        x1 = x0 + plt.length_mm;
        y1 = y0 + plt.width_mm;

        return {
            "left-bottom-corner": (x0, y0),
            "left-top-corner": (x0, y1),
            "right-bottom-corner": (x1, y0),
            "right-top-corner": (x1, y1)
        }

    def is_part_inside_plate(self, plate, rectangle):
        if rectangle.bottom_left_x_mm < plate.bottom_left_x_mm or \
            rectangle.bottom_left_y_mm < plate.bottom_left_y_mm:
                return False
        
        plate_coordinates = self.get_rectangle_vertices(plate)
        rectangle_coordinates = self.get_rectangle_vertices(rectangle)

        return rectangle_coordinates["right-top-corner"][0] <= plate_coordinates["right-top-corner"][0] and \
                rectangle_coordinates["right-top-corner"][1] <= plate_coordinates["right-top-corner"][1]

    def is_parts_overlapped(self, plate1, plate2, cutting_allowance = 10):
        plate1_coordinates = self.get_rectangle_vertices(plate1)
        plate2_coordinates = self.get_rectangle_vertices(plate2)

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

    def display(self):
        print(self.plates)