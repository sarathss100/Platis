from MetalPlate import MetalPlate
from Rectangle import Rectangle

plate = MetalPlate(1500.0, 6000.0, 0.0, 0.0)

plates = [
    Rectangle(500.0, 300.0, 0.0, 0.0),
    Rectangle(200.0, 400.0, 0.0, 310.0),
    Rectangle(400.0, 500.0, 0.0, 720.0)
]

def calculate_utilization(plate, plates):
    total_plate_area_available = plate.area
    total_plate_area_required = 0.0
    for shape in plates:
        total_plate_area_required += shape.area

    utilization_percentage = total_plate_area_required * 100 / total_plate_area_available
    return utilization_percentage

print(round(calculate_utilization(plate, plates), 2))