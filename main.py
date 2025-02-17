from window import Window

def main():
    """
    Main function to initialize and run the maze generator application.

    Creates a window with specified dimensions and waits for the user to close it.
    """
    win = Window(800, 600)
    win.wait_for_close()

if __name__ == "__main__":
    main()