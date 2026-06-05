from MetalPlate import MetalPlate
from Rectangle import Rectangle

plate = MetalPlate(1500, 6000)

plates = [
    Rectangle(500, 300),
    Rectangle(200, 400)
]

def calculate_utilization(plate, plates):
    total_plate_area_available = plate.area
    total_plate_area_required = 0.0
    for shape in plates:
        total_plate_area_required += shape.area

    utilization_percentage = total_plate_area_required * 100 / total_plate_area_available
    return utilization_percentage

print(round(calculate_utilization(plate, plates), 2))