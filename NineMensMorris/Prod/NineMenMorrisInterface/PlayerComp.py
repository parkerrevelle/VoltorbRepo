class PlayerComp(Player):
    """Computer Player Actions https://jitpaul.blog/2017/07/18/ai-in-nine-men-s-morris-game/"""
    def __init__(self):
      super().__init__()

class Node:
  def __init__(self, miniMaxEstimate, board):
    self.miniMaxEstimate = miniMaxEstimate
    self.board = board

  def miniMaxOpeningPhase(board, flag, depth, alpha, beta):
    if depth == 0:
        return Node(evaluateOpeningPhase(board), board)

    # Minimizer
    if flag == 0:
        ret = 100000
        temp = None
        bestBoard = list(board)

        for i in range(len(board)):
            if board[i] == " ":
                board[i] = "B"
                temp = miniMaxOpeningPhase(board, 1, depth - 1, alpha, beta)
                if temp.miniMaxEstimate < ret:
                    bestBoard = list(board)
                    ret = temp.miniMaxEstimate
                if ret <= alpha:
                    return Node(ret, board)
                beta = min(beta, ret)
                board[i] = " "
    # Maximizer
    else:
        ret = -100000
        temp = None
        bestBoard = list(board)

        for i in range(len(board)):
            if board[i] == " ":
                board[i] = "x"
                temp = miniMaxOpeningPhase(board, 0, depth - 1, alpha, beta)
                if temp.miniMaxEstimate > ret:
                    bestBoard = list(board)
                    ret = temp.miniMaxEstimate
                if ret >= beta:
                    return Node(ret, board)
                alpha = max(alpha, ret)
                board[i] = " "

    return Node(ret, bestBoard)

  def evaluateOpeningPhase(board):
    totalEvaluated = 0
    whitePieces = 0
    blackPieces = 0

    for piece in board:
        if piece == "W":
            whitePieces += 1
        elif piece == "B":
            blackPieces += 1

    totalEvaluated += 1
    return whitePieces - blackPieces

  def miniMaxMidEndPhase(board, flag, depth, alpha, beta):
    temp = evaluateMidEndPhase(board)
    if depth == 0:
        return Node(temp, board)
    elif temp == 10000:
        return Node(10000, board)
    elif temp == -10000:
        return Node(-10000, board)
    else:
        # Minimizer
        if flag == 0:
            ret = 100000
            bCount = 0
            bestBoard = list(board)
            nb = []
            
            for i in range(len(board)):
                if board[i] == "B":
                    nb = neighbours(i)
                    for tp in nb:
                        if board[tp] == "x":
                            board[tp] = "B"
                            board[i] = "x"
                            if closeMill(board, tp):
                                for j in range(len(board)):
                                    if board[j] == "x":
                                        if not closeMill(board, j):
                                            ret = min(ret, tempEstimation(board))
                            else:
                                temp = miniMaxMidEndPhase(board, 1, depth - 1, alpha, beta)
                                if temp.miniMaxEstimate < ret:
                                    bestBoard = list(board)
                                    ret = temp.miniMaxEstimate
                                if ret <= alpha:
                                    return Node(ret, board)
                                beta = min(beta, ret)
                            board[tp] = "x"
                            board[i] = "B"
            if bCount == 3:
                for i in range(len(board)):
                    if board[i] == "B":
                        for tp in range(len(board)):
                            if board[tp] == " ":
                                board[tp] = "B"
                                board[i] = "x"
                                temp = miniMaxMidEndPhase(board, 1, depth - 1, alpha, beta)
                                if temp.miniMaxEstimate < ret:
                                    bestBoard = list(board)
                                    ret = temp.miniMaxEstimate
                                if ret <= alpha:
                                    return Node(ret, board)
                                beta = min(beta, ret)
                                board[tp] = " "
                                board[i] = "B"
            else:
                temp = miniMaxMidEndPhase(board, 0, depth - 1, alpha, beta)
                if temp.miniMaxEstimate < ret:
                    bestBoard = list(board)
                    ret = temp.miniMaxEstimate
                if ret <= alpha:
                    return Node(ret, board)
                beta = min(beta, ret)
        # Maximizer
        else:
            ret = -100000
            wCount = 0
            bestBoard = list(board)
            nb = []

            for i in range(len(board)):
                if board[i] == "W":
                    nb = neighbours(i)
                    for tp in nb:
                        if board[tp] == "x":
                            board[tp] = "W"
                            board[i] = "x"
                            if closeMill(board, tp):
                                for j in range(len(board)):
                                    if board[j] == "x":
                                        if not closeMill(board, j):
                                            ret = max(ret, tempEstimation(board))
                            else:
                                temp = miniMaxMidEndPhase(board, 0, depth - 1, alpha, beta)
                                if temp.miniMaxEstimate > ret:
                                    bestBoard = list(board)
                                    ret = temp.miniMaxEstimate
                                if ret >= beta:
                                    return Node(ret, board)
                                alpha = max(alpha, ret)
                            board[tp] = "x"
                            board[i] = "W"
            if wCount == 3:
                for i in range(len(board)):
                    if board[i] == "W":
                        for tp in range(len(board)):
                            if board[tp] == " ":
                                board[tp] = "W"
                                board[i] = "x"
                                temp = miniMaxMidEndPhase(board, 0, depth - 1, alpha, beta)

  def evaluateMidEndPhase(board):
    totalEvaluated = 0
    white = 0
    black = 0

    for piece in board:
        if piece == "W":
            white += 1
        elif piece == "B":
            black += 1

    totalEvaluated += 1

    if black <= 2:
        return 10000
    elif white <= 2:
        return -10000

    numBlackMoves = 0
    nb = []
    bCount = 0

    for i in range(len(board)):
        if black <= 2:
            return 10000
        elif white <= 2:
            return -10000

        if black <= 2:
            return 10000
        elif white <= 2:
            return -10000

        if bCount != 3:
            for i in range(len(board)):
                if board[i] == "B":
                    nb = neighbours(i)
                    for tp in nb:
                        if board[tp] == "x":
                            board[tp] = "B"
                            board[i] = "x"
                            if closeMill(board, tp):
                                for j in range(len(board)):
                                    if board[j] == "W" and not closeMill(board, j):
                                        numBlackMoves += 1
                            else:
                                numBlackMoves += 1
                            board[tp] = "x"
                            board[i] = "B"
        else:
            for i in range(len(board)):
                if board[i] == "B":
                    for tp in range(len(board)):
                        if board[tp] == "x":
                            board[tp] = "B"
                            board[i] = "x"
                            if closeMill(board, tp):
                                for j in range(len(board)):
                                    if board[j] == "W" and not closeMill(board, j):
                                        numBlackMoves += 1
                            else:
                                numBlackMoves += 1
                            board[tp] = "x"
                            board[i] = "B"

    if numBlackMoves == 0:
        return 10000
    else:
        return (1000 * (white - black)) - numBlackMoves

  def neighbours(i):
    switcher = {
        0: [1, 3, 8],
        1: [0, 2, 4],
        2: [1, 5, 13],
        3: [0, 4, 6, 9],
        4: [1, 3, 5],
        5: [2, 4, 7, 12],
        6: [3, 7, 10],
        7: [5, 6, 11],
        8: [0, 9, 20],
        9: [3, 8, 10, 17],
        10: [6, 9, 14],
        11: [7, 12, 16],
        12: [5, 11, 13, 19],
        13: [2, 12, 22],
        14: [10, 15, 17],
        15: [14, 16, 18],
        16: [11, 15, 19],
        17: [9, 14, 18, 20],
        18: [15, 17, 19, 21],
        19: [12, 16, 18, 22],
        20: [8, 17, 21],
        21: [18, 20, 22],
        22: [13, 19, 21],
    }

    return switcher.get(i, [])

  def closeMill(board, pos):
    switcher = {
        0: [(1, 3, 8), (3, 6, 0), (20, 8, 0)],
        1: [(0, 2, 1)],
        2: [(0, 1, 2), (5, 7, 13), (7, 5, 2), (13, 22, 2)],
        3: [(0, 6, 3), (4, 5, 3), (9, 17, 3)],
        4: [(3, 5, 4)],
        5: [(2, 7, 5), (3, 4, 5), (12, 19, 5)],
        6: [(0, 3, 6), (10, 14, 6)],
        7: [(2, 5, 7), (11, 16, 7)],
        8: [(0, 20, 8), (9, 10, 8)],
        9: [(8, 10, 9), (3, 17, 9)],
        10: [(8, 9, 10), (6, 14, 10)],
        11: [(7, 16, 11), (12, 13, 11)],
        12: [(11, 13, 12), (5, 19, 12)],
        13: [(11, 12, 13), (2, 22, 13)],
        14: [(6, 10, 14), (15, 16, 14), (17, 20, 14)],
        15: [(14, 16, 15), (18, 21, 15)],
        16: [(14, 15, 16), (19, 22, 16), (7, 11, 16)],
        17: [(3, 9, 17), (14, 20, 17), (18, 19, 17)],
        18: [(15, 21, 18), (17, 19, 18)],
        19: [(17, 18, 19), (5, 12, 19), (16, 22, 19)],
        20: [(0, 8, 20), (21, 22, 20), (14, 17, 20)],
        21: [(20, 22, 21), (15, 18, 21)],
        22: [(20, 21, 22), (16, 19, 22), (2, 13, 22)]
    }
    
    for positions in switcher.get(pos, []):
        if all(board[p] == board[pos] for p in positions):
            return True
    return False








    #endregion


