from board import Board
from utils import * 


def h1_heuristic(board):
    misplaced = 0
    for i in range(4):
        for j in range(4):
            if(board.board_state[i][j] != board.goal_state[i][j] and board.board_state[i][j] != 0):
                misplaced += 1

    
    return misplaced

def h2_heuristic(board):
    """
    Manhattan distance
    """  
    distance = 0
     

    for i in range(4):
        for j in range(4):
            if board.board_state[i][j] == 0: continue
            i2,j2 = index_2d(board.goal_state,  board.board_state[i][j] )
            distance += abs(i2 - i) + abs(j2 - j)
                
    return distance

if __name__ == '__main__':

    board = Board([[10, 7,2,5], [1, 3, 4, 6] , [12,9, 15,11] , [13, 14, 8, 0]], 
                    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])

    print(h1_heuristic(board))
    print(h2_heuristic(board))

