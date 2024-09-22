"""
Tic Tac Toe Player
"""

import math
import copy

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
    num_x=sum(i.count("X") for i in board)
    num_o=sum(i.count("O") for i in board)
    if(board==initial_state()): return X
    elif(terminal(board)): return 
    else:
        if(num_x>num_o): return O
        else: return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if(terminal(board)):return 
    action=set()
    for i in range(3):
        for j in range(3):
            if(board[i][j]==EMPTY): action.add((i,j))
    return action

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if(board[action[0]][action[1]]!=EMPTY): raise ValueError("Action is not valid")
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]]=player(board)
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #vertical search
    i,j=0,0
    symbol=board[i][j]
    while(i<3 and j<3):
        if(board[i][j]!=symbol or symbol==EMPTY):
            i=0
            j+=1
            if(j<3):symbol=board[i][j]
            
        elif(board[i][j]==symbol): 
            if(i==2): return symbol
            i+=1
    #horizontal search
    for i in board:
        if(i==["X","X","X"]): return X
        elif(i==["O","O","O"]): return O
    #diagonal search
    symbol=board[1][1]
    if(symbol==EMPTY): return None
    elif(board[1][1]==board[0][0]==board[2][2]): return symbol
    elif(board[1][1]==board[0][2]==board[2][0]): return symbol
    else: return None
        


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if(winner(board)==X or winner(board)==O): return True
    for i in board:
        for j in i:
            if(j==EMPTY): return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    temp=winner(board)
    if(temp==X): return 1
    elif(temp==O): return -1
    else: return 0

def Max_Value(state,final_action=()):
    v,temp = -2,-2
    if (terminal(state)):
        return (utility(state),final_action)
    for action in actions(state):
        temp=v
        v = max(v, Min_Value(result(state, action),final_action)[0])
        if(v!=temp): final_action=action
    return (v,final_action)

def Min_Value(state,final_action=()):
    v,temp = 2,2
    if (terminal(state)):
        return (utility(state),final_action)
    for action in actions(state):
        temp=v
        v= min(v, Max_Value(result(state, action),final_action)[0])
        if(v!=temp): final_action=action
    return (v,final_action)

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    play=player(board)
    action=tuple()
    if(terminal(board)): return None
    if(board==initial_state()): return (1,1)
    elif(play==X):action=Max_Value(board)[1]
    else:action=Min_Value(board)[1]
    return action
