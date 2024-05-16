def area_sum(rectangles):
    total_area = 0
    for r in rectangles:
        total_area += (r["height"] * r["width"])
    return total_area