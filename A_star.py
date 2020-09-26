from board import Board
from utils import * 
from graph_state import *
import heapq


def a_star_search(board, heuristic):

    priortiy_queue = []
    state = Graph_State(board, heuristic(board.board_state, board.goal_state))
    heapq.heappush(priortiy_queue, state)

    closed_set = set()

    while len(priortiy_queue) != 0:
        state = heapq.heappop(priortiy_queue)

        if state.board.check_solved():
            return state.generate_path(), len(closed_set) + 1

        if(state.board in closed_set):
            continue 

        for child_board in state.board.generate_all_moves():
            child = Graph_State(child_board, heuristic(child_board.board_state, child_board.goal_state), state)

            if (child not in priortiy_queue) and (child.board not in closed_set):
                heapq.heappush(priortiy_queue, child)

        closed_set.add(state.board)

    print("Failed to solve")
    return None, 0
