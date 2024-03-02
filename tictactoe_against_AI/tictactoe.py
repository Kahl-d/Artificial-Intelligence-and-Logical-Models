import math
import copy

# Use these constants to fill in the game board
X = "X"
O = "O"
EMPTY = None


def start_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns which player (either X or O) who has the next turn on a board.

    In the initial game state, X gets the first move. Subsequently, the player alternates with each additional move.
    Any return value is acceptable if a terminal board is provided as input (i.e., the game is already over).
    """
    # check if the game has ended
    # the terminal function automatically checks for
    # winner X or Winner Y
    # also checks for a tie state
    if terminal(board):
        return None  # Return None for terminal board

    # if game is still on
    countX = 0
    countO = 0
    for row in board:
        for cell in row:
            if cell == X:
                countX += 1
            elif cell == O:
                countO += 1

    # as X has the first chance
    # return X if both counts are equal
    if countX == countO:
        return X
    else:
        return O


def actions(board):
    """
    Returns the set of all possible actions (i, j) available on the board.

    The actions function should return a set of all the possible actions that can be taken on a given board.
    Each action should be represented as a tuple (i, j) where i corresponds to the row of the move (0, 1, or 2)
    and j corresponds to the column of the move (also 0, 1, or 2).

    Possible moves are any cells on the board that do not already have an X or an O in them.

    Any return value is acceptable if a terminal board is provided as input.
    """
    act = set()
    # check for all EMPTY values on the board
    # record their locations
    # and return these locations
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                act.add((i, j))

    return act


def succ(board, action):
    """
    Returns the board that results from making move (i, j) on the board, without modifying the original board.

    If `action` is not a valid action for the board, you  should raise an exception.

    The returned board state should be the board that would result from taking the original input board, and letting
    the player whose turn it is make their move at the cell indicated by the input action.

    Importantly, the original board should be left unmodified. This means that simply updating a cell in `board` itself
    is not a correct implementation of this function. You’ll likely want to make a deep copy of the board first before
    making any changes.
    """
    # checking if cell is empty
    if board[action[0]][action[1]] != EMPTY:
        raise ValueError("Invalid - cell is not empty")

    # cheking for turn using the player function
    turn = player(board)
    # creating the new state
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = turn
    # marking the cell with the symbol of the player

    return new_board


# Custom function to check for winner X or Y
# To add modularity
def check_winner(board, str):

    # checking for all 8 possible win pattern in a tictactoe game
    if board[0][0] == board[1][1] == board[2][2] == str or \
            board[0][2] == board[1][1] == board[2][0] == str or \
            board[0][0] == board[0][1] == board[0][2] == str or \
            board[1][0] == board[1][1] == board[1][2] == str or \
            board[2][0] == board[2][1] == board[2][2] == str or \
            board[0][0] == board[1][0] == board[2][0] == str or \
            board[0][1] == board[1][1] == board[2][1] == str or \
            board[0][2] == board[1][2] == board[2][2] == str:
        return True



# winner fucntion
def winner(board):
    """
    Returns the winner of the game, if there is one.

    - If the X player has won the game, the function should return X.
    - If the O player has won the game, the function should return O.
    - If there is no winner of the game (either because the game is in progress, or because it ended in a tie), the
      function should return None.

    You may assume that there will be at most one winner (that is, no board will ever have both players with
    three-in-a-row, since that would be an invalid board state).
    """
    # check if X has won the game
    if check_winner(board, X):
        return X

    # check if y has won the game
    if check_winner(board, O):
        return O

    # return None if no nobody won
    # in cases of tie or the game is still going on
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.

    If the game is over, either because someone has won the game or because all cells have been filled without anyone
    winning, the function should return True.

    Otherwise, the function should return False if the game is still in progress.
    """

    # Check if the state is a winning state for X or O
    # return Ture if the game has ended in a win
    if winner(board) == X or winner(board) == O:
        return True

    # if not a win
    # check if there are empty cells on the board
    count = 0
    for row in board:
        for cell in row:
            if cell == EMPTY:
                count += 1

    # if no empty cells
    # return True as the game has termianted in a tie

    if count == 0:
        return True


    # in all other conditions return False
    # as the game can still go on
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.

    You may assume utility will only be called on a board if terminal(board) is True.
    """
    result = winner(board)
    if result == X:
        return 1
    elif result == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.

    The move returned should be the optimal action (i, j) that is one of the allowable actions on the board.

    If multiple moves are equally optimal, any of those moves is acceptable.

    If the board is a terminal board, the minimax function should return None.
    """
    # check if board is terminal
    if terminal(board):
        return None

    # check for turn
    turn = player(board)

    # X will try to find the max utility
    if turn == X:
        util, action = max_game(board)
    # ) will try to minimize the utility
    else:
        util, action = min_game(board)

    return action

def max_game(board):
    # when the recursion reaches an end state
    # return the utility as the total utility and action as None
    if terminal(board):
        return utility(board), None


    # if not an end state
    # assume max value1 as - infinity
    max_value1 = -math.inf
    move = None

    # for all possible actions on the board
    # record the maximum of all the min the next player will chosse
    act = actions(board)
    for a in act:
        min_max, _ = min_game(succ(board, a))
        if min_max > max_value1:
            max_value1 = min_max
            move = a
    # return the actions for the highest possible value from the next action
    return max_value1, move


def min_game(board):
    if terminal(board):
        return utility(board), None

    # Assume min value to be infinty
    # This serves as a utility from the max node

    min_value1 = math.inf
    move = None

    # for all possible actions
    # we find the value that is least from actions from max
    act = actions(board)
    for a in act:
        max_min, _ = max_game(succ(board, a))
        if max_min < min_value1:
            min_value1 = max_min
            move = a

    return min_value1, move
