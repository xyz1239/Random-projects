import turtle


def draw_traffic_light() -> None:
    # Initialize Turtle
    screen = turtle.Screen()
    screen.title("Traffic Light")
    screen.bgcolor("white")
    pen = turtle.Turtle()
    pen.speed(2)
    pen.width(4)

    # Draw outer black box (250 units wide)
    pen.color("black")
    pen.penup()
    pen.goto(-40, -250)
    pen.pendown()
    pen.begin_fill()
    for _ in range(2):
        pen.forward(250)
        pen.left(90)
        pen.forward(500)
        pen.left(90)
    pen.end_fill()

    # Draw thicker white border
    pen.color("white")
    pen.width(8)
    pen.penup()
    pen.goto(-30, -240)
    pen.pendown()
    for _ in range(2):
        pen.forward(230)
        pen.left(90)
        pen.forward(480)
        pen.left(90)
    pen.width(4)

    # Draw centered circles
    colors = ["red", "yellow", "green"]
    vertical_spacing = 160
    y_positions = [vertical_spacing, 0, -vertical_spacing]
    center_x = 85

    for color, y in zip(colors, y_positions):
        pen.penup()
        pen.goto(center_x, y)
        pen.pendown()
        pen.color(color)
        pen.begin_fill()
        pen.circle(20)
        pen.end_fill()

    pen.hideturtle()
    turtle.done()


draw_traffic_light()
