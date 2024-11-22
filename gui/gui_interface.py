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
        self.update_board()  # Draw the initial game pieces

    def draw_board(self):
        """Draw the 8x8 grid for the Othello board."""
        for i in range(1, 8): # Draw vertical lines
            x = i * CELL_SIZE
            self.canvas.create_line(x, 0, x, 480, fill="black")
        for i in range(1, 8): # Draw horizontal lines
            y = i * CELL_SIZE
            self.canvas.create_line(0, y, 480, y, fill="black")

    def update_board(self):
        """
        Update the board by drawing the game pieces according to the current GAMEBOARD state.
        """
        self.canvas.delete("piece")  # Clear all existing pieces from the canvas
        for (col, row), state in GAMEBOARD.items():  # Loop through all cells in the GAMEBOARD
            # Calculate the center coordinates for the current cell
            x = COLUMNS.index(col) * CELL_SIZE + CELL_SIZE // 2
            y = (row - 1) * CELL_SIZE + CELL_SIZE // 2

            # Draw a black piece if the cell state is 'black'
            if state == 'black':
                self.canvas.create_oval(
                    x - 20, y - 20, x + 20, y + 20, fill="black", tags="piece"
                )
            # Draw a white piece if the cell state is 'white'
            elif state == 'white':
                self.canvas.create_oval(
                    x - 20, y - 20, x + 20, y + 20, fill="white", tags="piece"
                )
