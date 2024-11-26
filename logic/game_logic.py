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

def get_opponent(player):
    """Function to get the current opponent"""
    return 'white' if player == 'black' else 'black'

def get_captured_pieces(position):
    """Function to get all the captured pieces by a move"""
    opponent = get_opponent(PLAYER_TO_MOVE)
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
                    captured_pieces.extend(path)
                break
            else:
                break
    return captured_pieces

def find_legal_moves():
    """Function to find all the legal moves that the current player can do"""
    legal_moves = []

    # Iterate through all positions on the game board
    for position, state in GAMEBOARD.items():
        # Check only empty cells for potential moves
        if state == 'empty' and get_captured_pieces(position):
            legal_moves.append(position)
    return legal_moves

def is_legal_move(position):
    """Function to find if a move is legal"""
    return position in find_legal_moves()

def flip_captured_pieces(position):
    """Function to flip the captured pieces after a move"""
    for piece in get_captured_pieces(position):
        GAMEBOARD[piece] = PLAYER_TO_MOVE
    return None

def move(position):
    """Function to make a move"""
    global PLAYER_TO_MOVE
    if is_legal_move(position):
        GAMEBOARD[position] = PLAYER_TO_MOVE
        flip_captured_pieces(position)
        PLAYER_TO_MOVE = get_opponent(PLAYER_TO_MOVE)  # Switch to the opponent
        print(PLAYER_TO_MOVE)
    return None

def computer_move():
    """Function for the computer to decide and play its move."""
    global PLAYER_TO_MOVE

    # Find all legal moves
    legal_moves = find_legal_moves()

    if legal_moves:
        # Choose the move that captures the most pieces
        best_move = max(legal_moves, key=lambda pos: len(get_captured_pieces(pos)))
        move(best_move)  # Make the move
    
    
    return None