from MetalPlate import MetalPlate
from Rectangle import Rectangle

plate = MetalPlate(1500, 6000, 0.0, 0.0)

plates = [
    Rectangle(500, 300, 0.0, 0.0),
    Rectangle(200, 400, 0.0, 510),
    Rectangle(400, 500, -10.0, 710),
    Rectangle(2000, 3000, 0.0, 1120)
]

def calculate_utilization(plate, plates):
    total_plate_area_available = plate.area
    total_plate_area_required = 0.0
    for shape in plates:
        total_plate_area_required += shape.area

    utilization_percentage = total_plate_area_required * 100 / total_plate_area_available
    return round(utilization_percentage, 2)

def is_part_inside_plate(plate, rectangle):
    if rectangle.bottom_left_x_mm < plate.bottom_left_x_mm or \
        rectangle.bottom_left_y_mm < plate.bottom_left_y_mm:
            return False
    
    plate_coordinates = get_rectangle_vertices(plate)
    rectangle_coordinates = get_rectangle_vertices(rectangle)

    return rectangle_coordinates["right-top-corner"][0] <= plate_coordinates["right-top-corner"][0] and \
            rectangle_coordinates["right-top-corner"][1] <= plate_coordinates["right-top-corner"][1]

def is_parts_overlapped(plate1, plate2, cutting_allowance = 10):
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

