import tkinter as tk
from logic.game_logic import GAMEBOARD, is_legal_move, move, PLAYER_TO_MOVE, COLUMNS

CELL_SIZE = 60 # Size of each cell in pixels

class OthelloGUI:
    def __init__(self, root):
        """Initialize the GUI window and setup the canvas for drawing the Othello board."""
        self.root = root
        self.root.title("Othello") # Set the window title
        self.canvas = tk.Canvas(root,
                                width=480,
                                height=480,
                                bg="green") # Create a canvas for the board
        self.canvas.pack()
        self.draw_board() # Draw the grid for the board

    def draw_board(self):
        """Draw the 8x8 grid for the Othello board."""
        for i in range(1, 8): # Draw vertical lines
            x = i * CELL_SIZE
            self.canvas.create_line(x, 0, x, 480, fill="black")
        for i in range(1, 8): # Draw horizontal lines
            y = i * CELL_SIZE
            self.canvas.create_line(0, y, 480, y, fill="black")
