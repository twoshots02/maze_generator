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
        self.is_running = False
        self.canvas = Canvas(self.__root, width=self.width, height=self.height)
        self.canvas.pack()
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
        self.is_running = True
        while self.is_running:
            self.redraw()
    
    def close(self):
        """
        Closes the window by setting the is_running flag to False.
        """
        self.is_running = False
