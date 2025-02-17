from tkinter import Tk, BOTH, Canvas

class window:

    def __init__(self, width, height):
        """
        Initializes the window with the specified width and height.

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
        #The constructor should take a width and height
        self.width = width
        self.height = height
        #It should create a new root widget using Tk() and save it as a data member
        self.__root = Tk() 
        #Set the title property of the root widget
        self.__root.title("Maze Generator")

        self.is_running = False
        self.canvas = Canvas(self.__root, width=self.width, height=self.height)
        self.canvas.pack()

    