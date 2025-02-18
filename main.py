from window import Window, Point, Line

# Define color constants
BLACK = "black"

def main():
    """
    Main function to initialize and run the maze generator application.

    Creates a window with specified dimensions and waits for the user to close it.
    """
    win = Window(800, 600)
    line = Line(Point(50, 50), Point(400, 400))
    win.draw_line(line, BLACK)
    win.wait_for_close()

if __name__ == "__main__":
    main()