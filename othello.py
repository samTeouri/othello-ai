# GAMEBOARD initialization
COLUMNS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
LINES = [i for i in range(1,9)]
GAMEBOARD = {(n, l): 'empty' for n in COLUMNS for l in LINES}
GAMEBOARD['d', 5] = 'black'
GAMEBOARD['e', 4] = 'black'
GAMEBOARD['d', 4] = 'white'
GAMEBOARD['e', 5] = 'white'

DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

PLAYER_TO_MOVE = 'black'

def get_opponent():
    return 'white' if PLAYER_TO_MOVE == 'black' else 'black'

# Function to get all the captured pieces by a move
def get_captured_pieces(position):
    opponent = get_opponent()
    captured_pieces = []
    for dx, dy in DIRECTIONS:
        path = []
        x, y = position[0], position[1]
        # Move in the direction (dx, dy) while capturing opponent pieces
        while True:
            x = chr(ord(x) + dx)
            y += dy
            if (x, y) not in GAMEBOARD or GAMEBOARD[(x, y)] == 'empty':
                break  # Quit the loop if next position is empty or out of gameboard
            if GAMEBOARD[(x, y)] == opponent:
                path.append((x, y))  # Add captured pieces to path
            elif GAMEBOARD[(x, y)] == PLAYER_TO_MOVE:
                if path:
                    captured_pieces.append(path)
                break
            else:
                break
    return captured_pieces

# Function to find all the legal moves that the current player can do
def find_legal_moves():
    legal_moves = []

    # Iterate through all positions on the game board
    for n, l in GAMEBOARD:
        # Check only empty cells for potential moves
        if GAMEBOARD[(n, l)] == 'empty':
            if get_captured_pieces((n,l)):
                legal_moves.append((n, l))
    return legal_moves

# Function to find if a move is legal
def is_legal_move(position):
    legal_moves = find_legal_moves()
    if position in legal_moves:
        return True
    return False

# Function to filp the captured pieces after a move
#def flip_captured_pieces(position):
#    captured_pieces = get_captured_pieces(position)
