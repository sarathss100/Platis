
def get_rectangle_vertices(plt) -> dict[str, tuple[float, float]]:
    x0 = plt.bottom_left_x_mm
    y0 = plt.bottom_left_y_mm

    x1 = x0 + plt.length_mm
    y1 = y0 + plt.width_mm

    return {
        "left-bottom-corner": (x0, y0),
        "left-top-corner": (x0, y1),
        "right-bottom-corner": (x1, y0),
        "right-top-corner": (x1, y1)
    }