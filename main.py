from window import Window, Point, Line
from maze import Cell, Maze
import sys

# Define color constants
BLACK = "black"

def main():
    """
    Main function to initialize and run the maze generator application.

    Creates a window with specified dimensions and waits for the user to close it.
    """
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) // num_cols
    cell_size_y = (screen_y - 2 * margin) // num_rows
    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)
    print("maze created")
    is_solvable = maze.solve()
    if not is_solvable:
        print("maze can not be solved!")
    else:
        print("maze solved!")

    win.wait_for_close()

if __name__ == "__main__":
    main()