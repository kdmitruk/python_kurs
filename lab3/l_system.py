import turtle


def apply(c):
    if c == "X":
        return "F+[[X]-X]-F[-FX]+X"
    elif c == "F":
        return "FF"
    else:
        return c


def transform(original):
    result = ""
    for c in original:
        result += apply(c)
    return result


def create_l_system(n, start):
    original = start
    for _ in range(n):
        result = transform(original)
        original = result
    return original


def draw_l_system(t, instructions, angle, length):
    stack = []
    for c in instructions:
        if c in ["F"]:
            t.forward(length)
        elif c == "-":
            t.right(angle)
        elif c == "+":
            t.left(angle)
        elif c == "[":
            stack.append((t.position(), t.heading()))
        elif c == "]":
            position, heading = stack.pop()
            t.pu()
            t.goto(position)
            t.setheading(heading)

def draw():
    screen = turtle.Screen()
    t = turtle.Turtle()

    t.speed(100)
    instructions = create_l_system(4, "X")
    draw_l_system(t,instructions,25,2)
    screen.exitonclick()
