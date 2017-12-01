"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Matthew De Clerck.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()


def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """

    window = rg.RoseWindow()

    center1 = rg.Point(100, 200)
    rad1 = 70
    center2 = rg.Point(200, 150)
    rad2 = 25

    circle1 = rg.Circle(center1, rad1)
    circle1.fill_color = 'green'
    circle2 = rg.Circle(center2, rad2)
    circle1.attach_to(window)
    circle2.attach_to(window)

    window.render()
    window.close_on_mouse_click()

    # ------------------------------------------------------------------
    # Done: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """

    window2 = rg.RoseWindow()

    circlepoint = rg.Point(50, 50)
    circlerad = 25
    circleblue = rg.Circle(circlepoint, circlerad)
    circleblue.fill_color = 'blue'
    circleblue.attach_to(window2)

    rectpoint1 = rg.Point(100, 150)
    rectpoint2 = rg.Point(250, 20)
    rectangle = rg.Rectangle(rectpoint1, rectpoint2)
    rectangle.pen = rg.Pen('black', 15)
    rectangle.attach_to(window2)

    print('The circle outline thickness is 1.')
    print('1')
    print('blue')
    print('Center = (50,50)')
    print('50')
    print('50')
    print('3')
    print('none')
    print('center = (60,20)')
    print('60')
    print('20')

    window2.render()
    window2.close_on_mouse_click()

    # ------------------------------------------------------------------
    # Done: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """

    window3 = rg.RoseWindow()

    point1 = rg.Point(150, 200)
    point2 = rg.Point(50, 200)
    line1 = rg.Line(point1, point2)

    point3 = rg.Point(100, 200)
    point4 = rg.Point(100, 100)
    line2 = rg.Line(point3, point4)
    line2.pen = rg.Pen('orange', 5)

    line1.attach_to(window3)
    line2.attach_to(window3)

    print('Point(100,200')
    print('100')
    print('200')

    window3.render()
    window3.close_on_mouse_click()

    # ------------------------------------------------------------------
    # Done: 4. Implement and test this function.
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
