#!/usr/bin/python3

# models/base.py
"""
Base module
"""

import turtle

class Base:
    """
    Base class for other classes
    """
    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Opens a window and draws all the Rectangles and Squares using Turtle graphics
        Args:
            list_rectangles (list): list of Rectangle instances
            list_squares (list): list of Square instances
        """
        screen = turtle.Screen()
        screen.title("Shapes Drawing")

        for rect in list_rectangles:
            t = turtle.Turtle()
            t.penup()
            t.setpos(rect.x, rect.y)
            t.pendown()
            for _ in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)

        for square in list_squares:
            t = turtle.Turtle()
            t.penup()
            t.setpos(square.x, square.y)
            t.pendown()
            for _ in range(4):
                t.forward(square.size)
                t.left(90)

        turtle.done()
