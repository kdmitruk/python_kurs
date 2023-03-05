import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def translate(self, x, y):
        self.x += x
        self.y += y


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


class Shape:
    def __init__(self, style):
        self.style = style

class Polygon(Shape):
    def __init__(self, style):
        super().__init__(style)
        self.vertices = []
        

    def add(self, vertex):
        self.vertices.append(vertex)

    def __str__(self) -> str:
        vertices_str = ""
        for vertex in self.vertices:
            vertices_str += str(vertex) + ", "
        return f"Polygon({vertices_str[:-2]})"

    def svg(self):
        # <polygon points = "200,10 250,190 160,210" / >
        vertices_str = ""
        for vertex in self.vertices:
            vertices_str += f'{vertex.x},{vertex.y} '
        return f'<polygon points = "{vertices_str[:-1]}" {self.style.svg()} />'

    def area(self):
        result = 0
        for i in range(len(self.vertices)):
            pa = self.vertices[i]
            pn = self.vertices[(i + 1) % len(self.vertices)]
            det = (pa.x * pn.y) - (pa.y * pn.x)
            result += det
        return abs(result / 2)

    def bottom_right(self):
        max_x = 0
        max_y = 0
        for vertex in self.vertices:
            max_x = max(max_x, vertex.x)
            max_y = max(max_y, vertex.y)
        return Point(max_x, max_y)

    @staticmethod
    def regular_pentagon(radius, style):
        polygon = Polygon(style)
        for i in range(5):
            x = radius * math.cos(math.radians(72 * i))
            y = radius * math.sin(math.radians(72 * i))
            polygon.add(Point(x, y))
        return polygon

    def translate(self, x, y):
        for vertex in self.vertices:
            vertex.translate(x, y)


class Style:
    def __init__(self, fill_color="transparent", stroke_color="black", stroke_width=1):
        self.fill_color = fill_color
        self.stroke_color = stroke_color
        self.stroke_width = stroke_width
        # style="fill:lime;stroke:purple;stroke-width:1"

    def svg(self):
        return f'style="fill:{self.fill_color};stroke:{self.stroke_color};stroke-width:{self.stroke_width}"'


class Scene:
    def __init__(self):
        self.shapes = []

    def add(self, shape):
        self.shapes.append(shape)

    def bottom_right(self):
        max_x = 0
        max_y = 0
        for shape in self.shapes:
            br = shape.bottom_right()
            max_x = max(max_x, br.x)
            max_y = max(max_y, br.y)
        return Point(max_x, max_y)

    def save(self, path):
        rb = self.bottom_right()
        file = open(path, "w")
        file.write("<html>\n<body>\n")
        file.write(f'<svg height="{rb.y}" width="{rb.x}">\n')
        for shape in self.shapes:
            file.write(shape.svg() + '\n')
        file.write("</svg>\n</body>\n</html>")
        file.close()




def main():
    p = Point(300, 0)
    q = Point(0, 400)

    polygon = Polygon(Style(fill_color="red"))
    polygon.add(p)
    polygon.add(q)
    polygon.add(Point(300, 400))

    # print(polygon.svg())
    # print(polygon.area())

    pentagon = Polygon.regular_pentagon(150, Style(fill_color="green", stroke_color="red"))
    pentagon.translate(200, 300)
    # print(pentagon.svg())
    scene = Scene()
    scene.add(polygon)
    scene.add(pentagon)
    scene.save("plik.html")


main()
