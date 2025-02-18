from window import Window, Line, Point

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