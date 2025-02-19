from window import Window, Line, Point
import time

class Cell:
    """
    Represents a single cell in a maze with walls on all sides.
    Attributes:
        has_left_wall (bool): Indicates if the cell has a left wall.
        has_right_wall (bool): Indicates if the cell has a right wall.
        has_top_wall (bool): Indicates if the cell has a top wall.
        has_bottom_wall (bool): Indicates if the cell has a bottom wall.
        _x1 (int or None): The x-coordinate of the top-left corner of the cell.
        _x2 (int or None): The x-coordinate of the bottom-right corner of the cell.
        _y1 (int or None): The y-coordinate of the top-left corner of the cell.
        _y2 (int or None): The y-coordinate of the bottom-right corner of the cell.
        _window (Window): The window object where the maze will be displayed.
    Methods:
        __init__(window: 'Window'):
        draw(x1, y1, x2, y2):
            Draws the cell on the window with the specified coordinates.
    """
    def __init__(self,window: 'Window'):
        """
        Initializes a new cell in the maze with walls on all sides.

        Args:
            window (Window): The window object where the maze will be displayed.
        """
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._window = window
    
    def draw(self, x1, y1, x2, y2):
        """
        Draws the walls of the maze cell based on the given coordinates.

        Parameters:
        x1 (int): The x-coordinate of the top-left corner of the cell.
        y1 (int): The y-coordinate of the top-left corner of the cell.
        x2 (int): The x-coordinate of the bottom-right corner of the cell.
        y2 (int): The y-coordinate of the bottom-right corner of the cell.

        The method draws lines for the walls of the cell if they exist:
        - Left wall: from (x1, y1) to (x1, y2)
        - Top wall: from (x1, y1) to (x2, y1)
        - Right wall: from (x2, y1) to (x2, y2)
        - Bottom wall: from (x1, y2) to (x2, y2)
        """
        if self._window is None:
            return

        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._window.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._window.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._window.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._window.draw_line(line)
            
    def draw_move(self, to_cell, undo=False):
        """
        Draws a move from the current cell to the specified cell.

        This method draws a line between the center points of the current cell and the target cell.
        The line is drawn in red by default, or in gray if the move is being undone.

        Args:
            to_cell (Cell): The target cell to which the move is being drawn.
            undo (bool, optional): If True, the move is being undone and the line is drawn in gray. Defaults to False.
        """
        half_point = abs((self._x2 - self._x1) // 2)
        self.center_point = Point(self._x1 + half_point, self._y1 + half_point)

        half_point = abs((to_cell._x2 - to_cell._x1) // 2)
        to_cell.center_point = Point(to_cell._x1 + half_point, to_cell._y1 + half_point)

        line = Line(self.center_point, to_cell.center_point)
        self._window.draw_line(line, "gray" if undo else "red")

class Maze:
    """
    A class to represent a maze.
    Attributes:
    -----------
    _x1 : int
        The x-coordinate of the top-left corner of the maze.
    _y1 : int
        The y-coordinate of the top-left corner of the maze.
    _num_rows : int
        The number of rows in the maze.
    _num_col : int
        The number of columns in the maze.
    _cell_size_x : int
        The width of each cell in the maze.
    _cell_size_y : int
        The height of each cell in the maze.
    _window : Window
        The window object where the maze will be drawn.
    _cells : list
        A 2D list to store the cells of the maze.
    Methods:
    --------
    __init__(x1, y1, num_rows, num_col, cell_size_x, cell_size_y, window):
        Initializes the maze with the given parameters and creates the cells.
    _create_cells():
        Creates the cells of the maze and draws them.
    _draw_cell(row, col):
        Draws a single cell at the specified row and column.
    _animate():
        Redraws the window and pauses for a short duration to create an animation effect.
    """
    
    def __init__(self, x1, y1, num_rows, num_col, cell_size_x, cell_size_y, window:'Window'):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_col = num_col
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window
        self._cells = []

        self._create_cells()

    def _create_cells(self):
        for i in range(self._num_rows):
            row_cells = []
            for j in range(self._num_col):
                row_cells.append(Cell(self._window))
            self._cells.append(row_cells)
        
        for i in range(self._num_rows):
            for j in range(self._num_col):
                self._draw_cell(i, j)
        
    def _draw_cell(self, row, col):
        if self._window is None:
            return
        x1 = self._x1 + col * self._cell_size_x
        y1 = self._y1 + row * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[row][col].draw(x1, y1, x2, y2)
        self._animate()
    
    def _animate(self):
        if self._window is None:
            return
        self._window.redraw()
        time.sleep(0.05)