from board import Board
from utils import * 
from A_star import *
import sys


if __name__ == '__main__':

    if len(sys.argv) != 1:
        input_file = open(sys.argv[1], 'r')
    else:
        input_file = open('input.txt', 'r')

    Lines = input_file.readlines()
    print(type(Lines))
    no_of_input_cases = int(Lines[0].strip())
    goal_state = convert_input_line_to_2d_arr(Lines[1])

    for i in range(2, len(Lines)):
        
        if Lines[i].isspace():
            continue

        starting_state = convert_input_line_to_2d_arr(Lines[i].strip())

        if not find_solvability(starting_state):
            print("Input case {} not solvable. Skipping.\n\n".format(Lines[i]))
            continue
    
        print("Using Manhattan heuristic to solve input {}".format(Lines[i]))
        board = Board(starting_state, goal_state)
        path, expanded_nodes = a_star_search(board, h2_heuristic)
        print("Path: {}\nCost: {}\nExpanded Nodes: {}\n\n".format(path, len(path) - 1, expanded_nodes))

        print("Using Misplaced Tiles heuristic to solve input {}".format(Lines[i]))
        board = Board(starting_state, goal_state)
        path, expanded_nodes = a_star_search(board, h1_heuristic)
        print("Path: {}\nCost: {}\nExpanded Nodes: {}".format(path , len(path) - 1, expanded_nodes))
    exit()
        


