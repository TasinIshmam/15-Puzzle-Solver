from board import Board
from utils import * 
from node import *
import heapq
import sys


def a_star(board, heuristic):

    frontier = []
    
    node = Node(board, heuristic(board.board_state, board.goal_state))
    heapq.heappush(frontier, node)

    explored = set()

    while len(frontier) != 0:
        node = heapq.heappop(frontier)

        # check if solved
        if node.board.is_solved():
            return node.path(), len(explored) + 1

        if(node.board in explored):
            continue 

        # add children to frontier
        for child_board in node.board.generate_all_moves():
            child = Node(child_board, heuristic(child_board.board_state, child_board.goal_state), node )
            # child must not have already been explored
            if (child not in frontier) and (child.board not in explored):
                 heapq.heappush(frontier, child)


        explored.add(node.board)

    return None, len(explored)


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
        
        print("Using Misplaced Tiles heuristic to solve input {}".format(Lines[i]))
        board = Board(starting_state, goal_state)
        path, expanded_nodes = a_star(board, h1_heuristic)
        print("Path: {}\nPath Length: {}\nExpanded Nodes: {}".format(path, len(path), expanded_nodes))

        print("Using Manhattan heuristic to solve input {}".format(Lines[i]))
        board = Board(starting_state, goal_state)
        path, expanded_nodes = a_star(board, h2_heuristic)
        print("Path: {}\nPath Length: {}\nExpanded Nodes: {}\n\n".format(path, len(path), expanded_nodes))




   



'''
TODO
Remove comments
Obfuscate variable names 
remove numpy library and function
read from input file 
'''