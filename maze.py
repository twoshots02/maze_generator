from window import Window, Line, Point
from cell import Cell
import time
import random

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
    
    def __init__(self, x1, y1, num_rows, num_col, cell_size_x, cell_size_y, window:'Window'=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_col = num_col
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window
        self._cells = []
        self._seed = random.seed(seed) if seed is not None else None

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

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

    def _break_entrance_and_exit(self):
        """
        Breaks the entrance and exit of the maze.

        This method modifies the maze by removing the top wall of the cell at the 
        starting position (0, 0) to create an entrance, and removing the bottom wall 
        of the cell at the ending position (last row, last column) to create an exit. 
        It also updates the visual representation of these cells.
        """
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self._num_rows - 1][self._num_col - 1].has_bottom_wall = False
        self._draw_cell(self._num_rows - 1, self._num_col - 1)
    
    def _break_walls_r(self, row, col):
        self._cells[row][col].visited = True
        while True:
            next_index_list = []

            # determine which cell(s) to visit next
            # left
            if col > 0 and not self._cells[row][col - 1].visited:
                next_index_list.append((row, col - 1))
            # right
            if col < self._num_col - 1 and not self._cells[row][col + 1].visited:
                next_index_list.append((row, col + 1))
            # up
            if row > 0 and not self._cells[row - 1][col].visited:
                next_index_list.append((row - 1, col))
            # down
            if row < self._num_rows - 1 and not self._cells[row + 1][col].visited:
                next_index_list.append((row + 1, col))

            # if there is nowhere to go from here
            # just break out
            if len(next_index_list) == 0:
                self._draw_cell(row, col)
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            # right
            if next_index[1] == col + 1:
                self._cells[row][col].has_right_wall = False
                self._cells[row][col + 1].has_left_wall = False
            # left
            if next_index[1] == col - 1:
                self._cells[row][col].has_left_wall = False
                self._cells[row][col - 1].has_right_wall = False
            # down
            if next_index[0] == row + 1:
                self._cells[row][col].has_bottom_wall = False
                self._cells[row + 1][col].has_top_wall = False
            # up
            if next_index[0] == row - 1:
                self._cells[row][col].has_top_wall = False
                self._cells[row - 1][col].has_bottom_wall = False

            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])
    
    def _reset_cells_visited(self):
        """
        Resets the visited status of all cells in the maze.

        Iterates through each column and each cell within the column,
        setting the `visited` attribute of each cell to `False`.
        """
        for col in self._cells:
            for cell in col:
                cell.visited = False