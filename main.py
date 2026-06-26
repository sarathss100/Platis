from models.MetalPlate import MetalPlate
from models.Rectangle import Rectangle
from models.SimplePlacer import SimplePlacer
from models.Layout import Layout

nesting_plate = MetalPlate(1500, 6000)
rectangle_plate = Rectangle(1000, 500)

var = SimplePlacer(nesting_plate, rectangle_plate)