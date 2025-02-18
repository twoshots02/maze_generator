from tkinter import Tk, BOTH, Canvas

class Window:

    def __init__(self, width, height):
        """
        Initializes the Window with the specified width and height.

        Args:
            width (int): The width of the window.
            height (int): The height of the window.

        Attributes:
            width (int): The width of the window.
            height (int): The height of the window.
            __root (Tk): The root widget of the window.
            is_running (bool): A flag indicating whether the window is running.
            canvas (Canvas): The canvas widget for drawing in the window.
        """
        # The constructor should take a width and height.
        self.width = width
        self.height = height
        # It should create a new root widget using Tk() and save it as a data member.
        self.__root = Tk() 
        # Set the title property of the root widget.
        self.__root.title("Maze Generator")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__is_running = False
        self.__canvas = Canvas(self.__root, bg="white", width=self.width, height=self.height)
        self.__canvas.pack(fill=BOTH, expand=1)
    def redraw(self):
        """
        Redraws the window by updating the idle tasks and the window itself.
        """
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        """
        Waits for the window to close by continuously redrawing it.
        """
        self.__is_running = True
        while self.__is_running:
            self.redraw()
    
    def draw_line(self, line: 'Line', fill_color="black"):
        """
        Draws a line on the canvas.

        Args:
            line (Line): An object with a draw method that takes a canvas and a fill color.
            fill_color (str): The color to fill the line with.
        """
        line.draw(self.__canvas, fill_color)

    def close(self):
        """
        Closes the window by setting the is_running flag to False.
        """
        self.__is_running = False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    
    def draw(self, canvas, fill_color):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2)

