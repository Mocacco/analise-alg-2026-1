import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """Retorna qual jogador tem a vez (X começa)."""
    count_x = sum(row.count(X) for row in board)
    count_o = sum(row.count(O) for row in board)
    return O if count_x > count_o else X

def actions(board):
    """Retorna um conjunto de tuplas (i, j) com espaços vazios."""
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions

def result(board, action):
    """Retorna um novo tabuleiro com a jogada aplicada."""
    i, j = action
    if board[i][j] is not EMPTY:
        raise Exception("Ação inválida: posição já ocupada.")
    
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board

def winner(board):
    """Determina o vencedor (X, O ou None)."""
    # Checar linhas e colunas
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    
    # Checar diagonais
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    
    return None

def terminal(board):
    """O jogo acabou se houver um vencedor ou empate (tabuleiro cheio)."""
    if winner(board) is not None:
        return True
    if all(all(cell is not EMPTY for cell in row) for row in board):
        return True
    return False

def utility(board):
    """Retorna 1 para vitória de X, -1 para O e 0 para empate."""
    res = winner(board)
    if res == X: return 1
    elif res == O: return -1
    else: return 0

def minimax(board):
    """Retorna a melhor jogada usando o algoritmo Minimax."""
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        v = -math.inf
        best_move = None
        for action in actions(board):
            min_val = min_value(result(board, action))
            if min_val > v:
                v = min_val
                best_move = action
        return best_move
    else:
        v = math.inf
        best_move = None
        for action in actions(board):
            max_val = max_value(result(board, action))
            if max_val < v:
                v = max_val
                best_move = action
        return best_move

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v