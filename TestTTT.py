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
    assert len(newboard._dump()) == 0

def test_x_in_position():
    newboard = build([0])
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

