from models.MetalPlate import MetalPlate
from models.Rectangle import Rectangle
from models.SimplePlacer import SimplePlacer
# from models.Layout import Layout

plate = MetalPlate(1500, 6000)

# val = Layout(plate)
# val.add_part(Rectangle(500, 300, 0.0, 0.0))
# val.add_part(Rectangle(200, 400, 0.0, 510))
# val.add_part(Rectangle(400, 500, -10.0, 710))
# val.add_part(Rectangle(2000, 3000, 0.0, 1120))
# val.display()

rectangle_plate = Rectangle(1000, 500)

var = SimplePlacer(plate, rectangle_plate)
var.print()