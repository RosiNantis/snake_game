"""
# 
Automated Test with pytest
(we write another origram to test our application)


Use Discipline of TDD (Test-Driven-Development)

------------------------------------------------

1. write a test
2. Run a test and make sure it fails
3. Write just enough code to make the test pass
4. Run the test again and make sure it passes
5. Clean up
6. Run the tests again (Regressino test)
7. Back to step one

also see: uncle Bob  "clean Code Lectures"

"""

from snake.moves import move, VALID_DIRECTIONS
import pytest
import random




# test parametrization
@pytest.mark.parametrize('position,direction,expected', [   # the @ symbol is the decorator: modifies the function
    # data examples
    ((5, 5), 'left',  (4, 5)),
    ((5, 5), 'right', (6, 5)),
    ((5, 0), 'left',  (4, 0)),
    ((5, 5), 'up',    (5, 6)), 
    ((5, 5), 'down',  (5, 4)), 
    ((3, 3), 'left',  (2, 3))
])   

def test_move(position, direction, expected):
    """feature: the snake is moving in all 4 directions"""
    assert move(position,direction) == expected

def test_move_random():
    """feature: test random directions"""
    # --> also see: hypothesis library
    for _ in range(100):
        x = random.randint(1,10)
        y = random.randint(1,10)
        direction = random.choice(list(VALID_DIRECTIONS))
        position = x, y
        move(position, direction)


def test_move_invalid_direction():
    with pytest.raises(Exception):  # tst oasses ub an Exception is generated
        move((1,1), 'dummy')

# TODO : also test random positions

def test_move_fraction():
    """This is an example of code that is not supposed to work"""
    position = (3.1415,5) # x, y
    with pytest.raises(Exception):  # tst oasses ub an Exception is generated
        move(position, 'down')


# TODO: check for the boundaries of the playing field

# To run the pyteest fole just press 
# pytest in terminal or pytest test_snake.py
