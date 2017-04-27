import pytest
from Board import BoardFactory
@pytest.fixture(scope="session", autouse=True)
def init():
    global bf
    bf = BoardFactory()

def build(list =[], player = 'X'):
    global bf
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
    newboard = build([0,2,6,8,'1','3','5','7'])
    next_states = bf.successors(newboard)
    assert next_states[0].get_move_list() == [0,2,6,8,'1','3','5','7',4]

