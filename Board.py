class BoardFactory:
    class State:
        def __init__(self, move_list, turn):
            self._board = move_list
            self._turn = turn

        def __getitem__(self, item):
            if item < 0 or item > 8:
                raise Exception('index out of bounds')
            if item in self._board:
                return 'X'
            if str(item) in self._board:
                return 'O'
            return ' '

        def win_for(self, player='X'):
            # TODO check for win for player
            pass

        def win(self):
            if self.win_for():
                return 'X'
            if self.win_for('O'):
                return 'O'
            if self.win_for('D'):
                return 'D'
            return ' '

        def _dump(self):
            return self._board

        def get_turn(self):
            return self._turn

    def new_board(self,move_list=None, board=None, move=None, player=None):
        if board is not None and move is not None:
            return  BoardFactory.State(board._dump().append(move),'X' if type(move) == 'str' else 'O')
        if move_list is not None and player is not None:
            return BoardFactory.State(move_list,player)

    def successors(self, board_state):
        suc = []
        if board_state.win() is not ' ':
            return suc
        # move_token = board_state.get_turn()
        # for x in range(9):
        #     if x not in board_state and str(x) not in board_state:
        #         suc.append(self.new_board(board_state, move_token))

