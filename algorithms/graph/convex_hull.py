import math


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def is_counterclockwise(a, b, c):
        """
        Returns True if three Point objects a,b and c form a counterclockwise
        turn, or False if they are colinear or form a clockwise turn.
        """
        det = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)
        return det > 0

    @staticmethod
    def distance(a, b):
        return ((b.x - a.x)**2 + (b.y - a.y)**2)**(1.0 / 2)


def find_convex_hull(points):
    """
    Finds the convex hull of a list of points and returns the points on the
    convex hull in a list. Uses Graham scan method.
    """
    convex_hull = []

    # First sort by y-coordinate so first point has lowest y coordinate.
    points.sort(key=lambda pt: pt.y)

    # Next sort by polar angle wrt to first point.
    first_pt = points[0]
    points.sort(key=lambda pt: polar_angle(first_pt, pt))

    # First two points are definitely on hull.
    convex_hull.append(points[0])
    convex_hull.append(points[1])

    for point in points[2:]:
        while not Point.is_counterclockwise(convex_hull[-2], convex_hull[-1], point):
            convex_hull.pop()
        convex_hull.append(point)

    return convex_hull


def calculate_area(convex_hull):
    area = 0
    c = convex_hull[0]
    for a, b in zip(convex_hull[1:], convex_hull[2:]):
        area += Point.distance(c, a) * Point.distance(c, b) * math.sin(polar_angle(c, b) - polar_angle(c, a)) / 2.0
    return area


def polar_angle(a, b):
    """Returns the polar angle between b and a and the positive x direction from a."""
    if a.x == b.x and a.y == b.y:
        return 0
    elif a.x == b.x and b.y > a.y:
        return math.pi / 2
    else:
        return math.atan2(b.y - a.y, b.x - a.x)
