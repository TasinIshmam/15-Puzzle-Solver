from utils import *
import copy
from random import randrange, randint
import numpy as np 

class Board:

    def __init__(self, board_state, goal_state):
        self.board_state = board_state
        self.goal_state = goal_state
        self.empty_tile_pos = index_2d(board_state, 0)


    def valid_moves(self):
       #Moves are: 1 = right, 2 = up, 3 = left, 4 = down
        moves = []
        if self.empty_tile_pos[1] != 3:
            moves.append(1)
        if self.empty_tile_pos[0] != 0:
            moves.append(2)
        if self.empty_tile_pos[1] != 0:
            moves.append(3)
        if self.empty_tile_pos[0] != 3:
            moves.append(4)

        return moves    

    def move_tile(self, direction):

        x,y =  self.empty_tile_pos
        if direction == 1:
            # moving right
            if direction in self.valid_moves():
                self.board_state[x][y] = self.board_state[x][y + 1]
                self.board_state[x][y + 1] = 0
                self.empty_tile_pos = self.empty_tile_pos[0] , self.empty_tile_pos[1] + 1

        elif direction == 2:
            # moving up
            if direction in self.valid_moves():
                self.board_state[x][y] = self.board_state[x - 1][y]
                self.board_state[x - 1][y] = 0
                self.empty_tile_pos = self.empty_tile_pos[0] - 1, self.empty_tile_pos[1]

        elif direction == 3:
            # moving left
            if direction in self.valid_moves():
                self.board_state[x][y] = self.board_state[x][y - 1]
                self.board_state[x][y - 1] = 0
                self.empty_tile_pos = self.empty_tile_pos[0], self.empty_tile_pos[1] - 1


        elif direction == 4:
            # moving down
            if direction in self.valid_moves():
                self.board_state[x][y] = self.board_state[x + 1][y]
                self.board_state[x + 1][y] = 0
                self.empty_tile_pos = self.empty_tile_pos[0] + 1, self.empty_tile_pos[1] 

    def print_board_state(self):
        print(self.board_state)

    def print(self):
        print(self.board_state)

    def __repr__(self):
        return "Board:\n[{}\n{}\n{}\n{}]\n\n".format(self.board_state[0], self.board_state[1], self.board_state[2], self.board_state[3])

    def is_solved(self):
        return self.board_state == self.goal_state
    
    def __eq__(self, other):
        return self.board_state == other.board_state and self.goal_state == other.goal_state

    def __str__(self):
        return self.board_state

    def __hash__(self):
        return hash(  tuple(map(tuple, self.board_state))   )

    def generate_all_moves(self):
        child_boards = []

        for move in self.valid_moves():

            child_board = Board( copy.deepcopy(self.board_state), self.goal_state)
            child_board.move_tile(move)
            child_boards.append(child_board)
        
        return child_boards

    def scramble(self, n=1000):
        """
        scrambles the board by moving in a random (legal) direction (no inverses) n times

        n: (int) number of random moves
        """
        def inverse(x):
            """
            finds the inverse action of x
            1 -> 3
            2 -> 4
            3 -> 1
            4 -> 2
            """
            return ((x + 5) % 4) + 1
        last_inverse = 0
        for _ in range(n):
            move = np.random.choice([action for action in self.valid_moves() if action != last_inverse])
            self.move_tile(move)
            last_inverse = inverse(move)











