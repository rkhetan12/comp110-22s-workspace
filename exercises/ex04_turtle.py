"""The program will draw a mountain, sun, and river landscape. For the fun part, I created a sun using the circle imported function on line 86. I wanted to see if I could make a circle without using a while loop. I have a total of four functions with one helper function. Complex functions are getting broken up in both the curve_river functions on line 26 and 49."""


__author__ = "730476155"
from turtle import Turtle, colormode, done
colormode(255)


def mountain_triangles(emily: Turtle, x: float, y: float, width: float) -> None:
    """Draw four triangles of the given dimensions located at the top of the screen in a horizontal manner located at x,y."""
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


def curve_river_down(emily: Turtle, x: float, y: float) -> None:
    """Draws a curvy line from top to bottom."""
    make_a_straight_line(emily, 235, 140, -385)
    emily.setheading(180.0)  # which direction is the turtle pointing
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


def curve_river_up(emily: Turtle, x: float, y: float) -> None:
    """Draw a curvy line from bottom to top."""
    emily.setheading(0.0)
    emily.goto(x, y)
    emily.pendown()
    make_a_straight_line(emily, -496, -459, 455)
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


def make_a_straight_line(emily: Turtle, x: float, y: float, width: float) -> None:
    """Makes two straight lines connecting the two curvy lines."""
    emily.setheading(0.0)
    emily.goto(x, y)
    emily.pendown()
    emily.forward(width)
    # emily.penup()


def sun_created_from_circle(emily: Turtle, x: float, y: float, radius: float) -> None:
    """Makes a sun by calling the circle function."""
    emily.setheading(0.0)
    emily.goto(x, y)
    emily.pendown()
    emily.begin_fill()
    emily.circle(radius)
    emily.penup()
    emily.end_fill()


def main() -> None:
    """Main Function, this is where all the functions get executed."""
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
    curve_river_down(emily, -150, 140)
    curve_river_up(emily, -41, -459)
    emily.end_fill()

    emily.hideturtle()
    

if __name__ == "__main__":
    main()
done()