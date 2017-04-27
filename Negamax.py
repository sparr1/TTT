from Board import BoardFactory
import sys
class Negamax:
    def __init__(self, initial_board = None):
        self._bf = BoardFactory()
        self._current_state = self._bf.new_board(board = [], player = 'X')\
            if initial_board is None else initial_board

    def make_move(self):
        color = 1 if self._current_state.get_turn() == 'X' else -1
        new_state = self.tree_search(self._current_state, 100, color)[1]
        print(str(new_state))
        self._current_state = new_state

    def value_position(self, board_state, color, depth):
        pos = board_state.win()
        if pos == ' ' or pos == 'D':
            return 0
        if pos == 'X':
            return (5/depth)
        return -5*depth

    def tree_search(self, node, depth, color):
        children = self._bf.successors(node)
        if depth == 0 or len(children)==0:
            return color*self.value_position(node, color, depth), node
        best_value = -sys.maxsize
        best_child = children[0]
        for child in children:
            v = -(self.tree_search(child, depth-1, -color))[0]
            if v>best_value:
                best_child = child
                best_value = v

        return best_value, best_child