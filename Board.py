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

        def __str__(self):
            return ('\n'+self[0]+'|'+self[1]+'|'+self[2]+'\n'+
                        '-----'+'\n'+
                        self[3]+'|'+self[4]+'|'+self[5]+'\n'+
                        '-----'+'\n'+
                        self[6]+'|'+self[7]+'|'+self[8])
        #check one type of win
        def _check_rows(self, vec, pt_range, player):
            #translate between grid vectors and movement through list
            def _vec_transform(point, vector, scalar):
                return (point[0] + vector[0] * scalar) + 3 * (point[1] + vector[1] * scalar)
            #start from every point in pt range
            for pt in pt_range:
                # prove rows by contradiction
                win = True
                #travel down the row
                for d in range(3):
                    #travel by vector, check if each point is not what is expected
                    if self[_vec_transform(pt, vec, d)] != player:
                        #proof by contradiction, row is not a win
                        win = False
                #if win hasn't toggled, you won in that row
                if win:
                    return True
            #if you haven't won in any of the rows checked so far, you didn't win in this batch of rows
            return False

        #check some different types of wins for the player
        def win_for(self, player='X'):
            # check the horizontals
            # check the verticals
            # check diagonal from top left
            # check diagonal from top right
            # if any true you have a three in a row
            return self._check_rows( (1, 0), [(0, x) for x in range(3)], player)\
                or self._check_rows( (0, 1), [(x, 0) for x in range(3)], player)\
                or self._check_rows( (1, 1), [(0, 0)], player)\
                or self._check_rows((1,-1), [(0, 2)], player)

        #what a beautiful win method
        def win(self):
            if self.win_for():
                return 'X'
            if self.win_for('O'):
                return 'O'
            if len(self._move_list)==9:
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
            ml = list(board.get_move_list())
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

