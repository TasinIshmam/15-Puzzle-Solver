

class Graph_State:

    def __init__(self, board, h_value, parent=None):
        self.board = board
        self.parent = parent
        self.f_value = h_value + len(self.generate_path()) - 1

    def generate_path(self):
       
        node = self
        path_list_full = []

        while node:
            path_list_full.append(node.board)
            node = node.parent

        return list(reversed(path_list_full))

    def __eq__(self, other):
        return self.board == other.board and self.f_value == other.f_value 

    def __lt__(self, other):
        return self.f_value < other.f_value
