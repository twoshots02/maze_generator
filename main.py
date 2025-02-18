from window import Window, Point, Line
from maze import Cell

# Define color constants
BLACK = "black"

def main():
    """
    Main function to initialize and run the maze generator application.

    Creates a window with specified dimensions and waits for the user to close it.
    """
    win = Window(800, 600)
    cell = Cell(win)
    cell.has_left_wall = False
    cell.draw(50, 50, 100, 100)

    cell = Cell(win)
    cell.has_right_wall = False
    cell.draw(125, 125, 200, 200)

    cell = Cell(win)
    cell.has_bottom_wall = False
    cell.draw(225, 225, 250, 250)

    cell = Cell(win)
    cell.has_top_wall = False
    cell.draw(300, 300, 500, 500)

    win.wait_for_close()

if __name__ == "__main__":
    main()