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

def getOpponent():
    return 'white' if PLAYER_TO_MOVE == 'black' else 'black'

def getCapturedPieces(position):
    opponent = getOpponent()
    captured_pieces = []
    for dx, dy in DIRECTIONS:
        x, y = position[0], position[1]
        captured = False
        path = []

        # Move in the direction (dx, dy) while capturing opponent pieces
        while True:
            x = chr(ord(x) + dx)
            y += dy
            if (x, y) not in GAMEBOARD or GAMEBOARD[(x, y)] == 'empty':
                break  # Quit the loop if next position is empty or out of gameboard
            if GAMEBOARD[(x, y)] == opponent:
                path.append((x, y))  # Add captured pieces to path
                captured_pieces.append((x, y))
            elif GAMEBOARD[(x, y)] == PLAYER_TO_MOVE:
                if path:
                    captured = True
                break
            else:
                break

# Function to find all the legal moves that the current player can do
def findLegalMoves():
    opponent = getOpponent()
    legal_moves = []

    # Iterate through all positions on the game board
    for n, l in GAMEBOARD:
        # Check only empty cells for potential moves
        if GAMEBOARD[(n, l)] == 'empty':
            for dx, dy in DIRECTIONS:
                x, y = n, l
                captured = False
                path = []

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
                            captured = True
                        break
                    else:
                        break

                if captured:
                    legal_moves.append((n, l))
                    break  # Stop checking other directions if this move is legal

    return legal_moves

# Function to find if a move is legal
def isLegalMove(move):
    legal_moves = findLegalMoves()
    if move in legal_moves:
        return True
    return False

# Function to filp the captured pieces after a move
#def flip_captured_pieces(move):
    
