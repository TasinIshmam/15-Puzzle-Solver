from board import Board
from utils import * 
from node import *
import heapq


def a_star(board, heuristic):

    priortiy_queue = []
    node = Graph_State(board, heuristic(board.board_state, board.goal_state))
    heapq.heappush(priortiy_queue, node)

    closed_set = set()

    while len(priortiy_queue) != 0:
        node = heapq.heappop(priortiy_queue)

        if node.board.check_solved():
            return node.generate_path(), len(closed_set) + 1

        if(node.board in closed_set):
            continue 

        for child_board in node.board.generate_all_moves():
            child = Graph_State(child_board, heuristic(child_board.board_state, child_board.goal_state), node)

            if (child not in priortiy_queue) and (child.board not in closed_set):
                heapq.heappush(priortiy_queue, child)

        closed_set.add(node.board)

    return None, len(closed_set)
