"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    X_COUNT=sum(row.count("X") for row in board)
    O_COUNT=sum(row.count("O") for row in board)
    if X_COUNT <= O_COUNT:
        return "X"
    else:
        return "O"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    #若action不是有效动作，则抛出异常
    if i<0 or i>2 or j<0 or j>2:
        raise Exception("Invalid input")
    if board[i][j] != EMPTY:
        raise Exception("Invalid input")

    deep_copy_board = [row.copy() for row in board]
    current_player = player(board)
    deep_copy_board[i][j] = current_player
    return deep_copy_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # 检查每一行
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]

    # 检查每一列
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not None:
            return board[0][j]

    # 检查对角线（左上到右下）
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]

    # 检查对角线（右上到左下）
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if not any(element == EMPTY for row in board for element in row):
        return True
    elif winner(board) is not None:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if(terminal(board)):
        final_winner=winner(board)
        if final_winner is X:
            return 1
        elif final_winner is O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    current_player = player(board)

    if current_player == X:

        _ , best_action=max_value(board,float('-inf'),float('inf'))
        return best_action
    else:
        _ , best_action=min_value(board,float('-inf'),float('inf'))
        return best_action

def max_value(board,alpha,beta):
    if terminal(board):
        return utility(board),None

    v=float('-inf')
    best_action=None

    for action in actions(board):
        min_val,_=min_value(result(board,action),alpha,beta)
        if min_val>v:
            v = min_val
            best_action=action
        alpha =max(alpha,v)
        if v>=beta:
            break;

    return v,best_action

def min_value(board,alpha,beta):
    if terminal(board):
        return utility(board),None

    v=float('inf')
    best_action=None
    for action in actions(board):
        max_val,_=max_value(result(board,action),alpha,beta)
        if max_val<v:
            v = max_val
            best_action=action
        beta=min(beta,v)
        if v<=alpha:
            break;

    return v,best_action