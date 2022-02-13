"""The program will draw a mountain and river landscape with fish in the river."""


__author__ = "730476155"

from turtle import Turtle, colormode, done, penup

colormode(255)


def mountain_triangles(emily: Turtle, x: float, y: float, width: float) -> None:
    """Draw five triangles of the given dimensions located at the top of the screen in a horizontal manner located at x,y."""
    emily.goto(x, y)
    emily.setheading(0.0)
    emily.pendown()
    emily.begin_fill()
    i: int = 0
    while (i < 3):
        emily.forward(width)
        emily.left(120)
        i = i + 1
    emily.end_fill()
    emily.penup()


def zig_zag_river_down(emily: Turtle, x: float, y: float) -> None:
    """Draws a zigzag line."""
    emily.setheading(180.0)  # which direction is the turtle pointing
    emily.goto(x, y)
    emily.pendown()
    i: int = 0
    counter: int = 0
    while (i < 6):
        counter = 0
        while (counter < 10):
            emily.forward(7)
            emily.left(12)
            counter += 1
        counter = 0
        while (counter < 10):
            emily.forward(7)
            emily.right(12)
            counter += 1
        i += 1
    
    emily.penup()


def zig_zag_river_up(emily: Turtle, x: float, y: float) -> None:
    """Draws a zigzag line."""
    emily.setheading(0.0)
    emily.goto(x, y)
    emily.pendown()
    i: int = 0
    counter: int = 0
    while (i < 6):
        counter = 0
        while (counter < 10):
            emily.forward(7)
            emily.left(12)
            counter += 1
        counter = 0
        while (counter < 10):
            emily.forward(7)
            emily.right(12)
            counter += 1
        i += 1
    emily.penup()


def make_a_straight_line(emily: Turtle, x: float, y: float, width: float):
    emily.setheading(0.0)
    emily.goto(x, y)
    emily.pendown()
    emily.forward(width)
    emily.penup()


def sun_created_from_circle(emily: Turtle, x: float, y: float, radius):
    emily.setheading(0.0)
    emily.goto(x, y)
    emily.pendown()
    emily.begin_fill()
    emily.circle(radius)
    emily.penup()
    emily.end_fill()


def main() -> None:
    emily: Turtle = Turtle()
    emily.speed(5)
    emily.penup()
    emily.color(232, 241, 80)
    sun_created_from_circle(emily, 350, 275, 50)
    emily.color(49, 2, 28)
    mountain_triangles(emily, -715, 140, 355.0)  
    emily.color(26, 1, 15)
    mountain_triangles(emily, -360, 140, 355.0)
    emily.color(49, 2, 28)
    mountain_triangles(emily, -5, 140, 355.0)
    emily.color(26, 1, 15)
    mountain_triangles(emily, 350, 140, 355.0)

    emily.begin_fill()
    emily.color(32, 177, 217)
    emily.pensize(5)
    # Right to Left
    make_a_straight_line(emily, 235, 140, -385)
    # Top to bottom (Left)
    zig_zag_river_down(emily, -150, 140)
    # Left to Right
    make_a_straight_line(emily, -496, -459, 455)
    print(emily.xcor())
    print(emily.ycor())
    # Bottom to Top (Right)
    zig_zag_river_up(emily, -41, -459)
    emily.end_fill()

    emily.hideturtle()
    

if __name__ == "__main__":
    main()
done()