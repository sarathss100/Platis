from MetalPlate import MetalPlate
from Rectangle import Rectangle

plate = MetalPlate(1500, 6000, 0.0, 0.0)

plates = [
    Rectangle(500, 300, 0.0, 0.0),
    Rectangle(200, 400, 0.0, 310),
    Rectangle(400, 500, 0.0, 720),
    Rectangle(2000, 3000, 0.0, 1130)
]

def calculate_utilization(plate, plates):
    total_plate_area_available = plate.area
    total_plate_area_required = 0.0
    for shape in plates:
        total_plate_area_required += shape.area

    utilization_percentage = total_plate_area_required * 100 / total_plate_area_available
    return round(utilization_percentage, 2)

def is_part_inside_plate(plate, rectangle):
    plate_top_right_x_mm = plate.bottom_left_x_mm + plate.length_mm
    plate_top_right_y_mm = plate.bottom_left_y_mm + plate.width_mm
    rectangle_top_left_x_mm = rectangle.bottom_left_x_mm + rectangle.length_mm
    rectangle_top_left_y_mm = rectangle.bottom_left_y_mm + rectangle.width_mm
    return  rectangle_top_left_x_mm <= plate_top_right_x_mm and rectangle_top_left_y_mm <= plate_top_right_y_mm

print(is_part_inside_plate(plate, plates[2]))