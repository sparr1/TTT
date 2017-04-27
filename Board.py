class BoardFactory:
    class State:
        def __init__(self, move_list, turn):
            self._move_list = move_list
            self._turn = turn

        def __getitem__(self, item):
            if item < 0 or item > 8:
                raise Exception('index out of bounds')
            if item in self._move_list:
                return 'X'
            if str(item) in self._move_list:
                return 'O'
            return ' '

        def win_for(self, player='X'):
            # TODO check for win for player
            return False

        def win(self):
            if self.win_for():
                return 'X'
            if self.win_for('O'):
                return 'O'
            if self.win_for('D'):
                return 'D'
            return ' '

        def get_move_list(self):
            return self._move_list

        def get_turn(self):
            return self._turn

    def new_board(self,move_list=None, board=None, move=None, player=None):
        if move_list is not None:
            ml = list(move_list)
        if player is not None:
            pl = str(player)
        if board is not None and move is not None:
            ml = board.get_move_list()
            ml.append(move)
            pl = 'X' if type(move) == 'str' else 'O'
        return BoardFactory.State(ml,pl)

    def successors(self, board_state):
        suc = []
        if board_state.win() is not ' ':
            return suc
        move_token = board_state.get_turn()
        for n in range(9):
            if board_state[n] == ' ':
                suc.append(
                self.new_board(board=board_state,
                               move= n if move_token=='X' else str(n) ))
        return suc

