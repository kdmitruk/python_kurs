import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"


class Segment:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self) -> str:
        return f"Segment({self.p1}, {self.p2})"

    def distance(self):
        return math.hypot(self.p1.x - self.p2.x, self.p1.y - self.p2.y)

    def svg(self):
        return f'<line x1="{self.p1.x}" y1="{self.p1.y}" x2="{self.p2.x}" y2="{self.p2.y}" style="stroke:black" />'


def main():
    p = Point(300, 0)
    q = Point(0, 400)
    f = Segment(p, q)
    print(f)
    print(f.distance())
    print(f.svg())


main()
