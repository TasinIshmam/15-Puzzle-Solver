

class Node:

    def __init__(self, board, parent=None, f_value):
        self.board = board
        self.parent = parent

    #TODO probably don't need this function.
    def child(self, board):
        return Node(board, self)

    def path(self):
       
        node = self
        path_to_head = []

        while node:
            path_to_head.append(node.board)
            node = node.parent

        return list(reversed(path_to_head))

    def __eq__(self, other):
        return self.board == other.board and self.f_value == other.f_value 

    def __lt__(self, other):
        return self.f_value < other.f_value