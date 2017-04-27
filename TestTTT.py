import pytest
from Board import BoardFactory
from Negamax import Negamax
@pytest.fixture(scope="session", autouse=True)
def init():
    global bf
    bf = BoardFactory()

def build(list =[], player = 'X'):
    return bf.new_board(move_list=list, player=player)

def test_state_dump():
    newboard = build()
    assert len(newboard.get_move_list()) == 0

def test_x_in_position():
    newboard = build([0], 'O')
    assert newboard[0] == 'X'

def test_o_in_position():
    newboard = build(['1'])
    assert newboard[1] == 'O'

def test_empty_position():
    newboard = build()
    assert newboard[8] == ' '

def test_out_of_bounds():
    newboard = build()
    try:
        newboard[9]
    except Exception as e:
        assert str(e) == 'index out of bounds'

def test_successors_simple():
    # X O X
    # O   O
    # X O X
    newboard = build([0,2,6,8,'1','3','5','7'])
    next_states = bf.successors(newboard)
    assert next_states[0].get_move_list() == [0,2,6,8,'1','3','5','7',4]

def test_successors_from_start():
    newboard = build([])
    next_states = bf.successors(newboard)
    assert [s.get_move_list() for s in next_states] == [[x] for x in range(9)]

def test_successors_complex():
    newboard = build (['0', 4, '8'], 'X')
    next_states = bf.successors(newboard)
    next_states = bf.successors(next_states[0])
    # for n in range(len(next_states)):
    #     print(str(next_states[n]))

def test_simple_horizontal_win():
    # X X X
    #
    #
    newboard = build([0,1,2])
    assert newboard.win() == 'X'

def test_simple_vertical_win():
    #   X
    #   X
    #   X
    newboard = build([1,4,7])
    assert newboard.win() == 'X'

def test_simple_diagonal_win():
    # X
    #   X
    #     X
    newboard = build([0,4,8])
    assert newboard.win() == 'X'

def test_no_win():
    # X X O
    #   O
    #   O X
    newboard = build([0, '4', 8,'7',1,'2'])
    assert newboard.win() == ' '

def test_draw():
    # O X O
    # O X X
    # X O X
    newboard = build([4,'2',8,'0',1,'7',5,'3',6])
    assert newboard.win() == 'D'

def test_simple_o_win():
    #
    #
    # O O O
    newboard = build(['6','7','8'])
    assert newboard.win() == 'O'

def test_midgame_win():
    # O O X
    #   X O
    # X   X
    newboard = build([4, '1', 8, '0', 2, '5,', 6])
    assert newboard.win() == 'X'

def test_str():
    newboard = build(['0',1, '2', 3, '4', 5, '6', 7, '8'])
    #print(str(newboard))

def test_negamax():
    newboard = build (['0', 4, '8'], 'O')
    driver = Negamax(newboard)
    driver.make_move()
    driver.make_move()
    driver.make_move()