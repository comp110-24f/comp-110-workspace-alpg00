"""Coordinate function"""

def get_coords(xs: str, ys: str) -> None:
    coord: str = "("
    i = 0
    while i < len(xs):
        j = 0
        while j < len(ys):
            coord += xs[i] + "," + ys[j] + ")"
            print(coord)
            coord = "("
            j += 1
        i += 1