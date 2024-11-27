import tkinter as tk
from logic.game_logic import GAMEBOARD, computer_move, get_opponent, is_legal_move, move, PLAYER_TO_MOVE, COLUMNS

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
        self.turn_label = tk.Label(root, text=f"Turn: {PLAYER_TO_MOVE.capitalize()}", font=("Arial", 14)) # Label to display the current player's turn
        self.turn_label.pack()
        self.canvas.bind("<Button-1>", self.on_click)  # Bind left mouse click to the on_click method
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
    
    def update_turn_display(self):
        """Function to update the turn label to reflect the current player."""
        self.turn_label.config(text=f"Turn: {PLAYER_TO_MOVE.capitalize()}")

    def on_click(self, event):
        """
        Handle a left mouse click on the board.
        Determine the cell clicked and make a move if it's a legal move.
        """
        global PLAYER_TO_MOVE

        # Determine the column and row based on the click position
        col = COLUMNS[event.x // CELL_SIZE]
        row = (event.y // CELL_SIZE) + 1
        position = (col, row)

        # Check if the clicked position is a legal move
        if is_legal_move(position):
            move(position)  # Update the game state
            self.update_board()  # Redraw the board to reflect the changes

            # Switch to the next player
            PLAYER_TO_MOVE = get_opponent(PLAYER_TO_MOVE)
            self.update_turn_display()  # Update the turn label

            # Let the computer play its turn if it's white's turn
            self.root.after(1000, self.computer_turn)  # Add a delay for better user experience

    def computer_turn(self):
        """Function to handle the computer's move."""
        computer_move()  # Let the computer play
        self.update_board()  # Update the GUI