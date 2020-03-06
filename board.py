from utils import *

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

    def move_tile(self, direction_code):

        x,y =  self.empty_tile_pos
        if direction == 1:
            # moving right
            if direction in self.valid_moves():
                self.board_state[x][y] = self.board_state[x][y + 1]
                self.board_state[x][y + 1] = 0
                self.empty_tile_pos[1] += 1

        elif direction == 2:
            # moving up
            if direction in self.valid_moves():
                self.board_state[x][y] = self.board_state[x - 1][y]
                self.board_state[x - 1][y] = 0
                self.empty_tile_pos[0] -= 1

        elif direction == 3:
            # moving left
            if direction in self.valid_moves():
                self.board_state[x][y] = self.board_state[x][y - 1]
                self.board_state[x][y - 1] = 0
                self.empty_tile_pos[1] -= 1

        elif direction == 4:
            # moving down
            if direction in self.valid_moves():
                self.board_state[x][y] = self.board_state[x + 1][y]
                self.board_state[x + 1][y] = 0
                self.empty_tile_pos[0] += 1
    

    def print_board_state(self):
        print(self.board_state)

    def is_solved(self):
        return self.board_state == self.goal_state
    
    def __eq__(self, other):
        return self.board_state == other.board_state

    def forecast(self, action):
      
        new_board = Board(np.copy(self.board))
        new_board.move(action)
        return new_board












