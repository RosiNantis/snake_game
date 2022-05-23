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

from snake import move
import pytest


# feature: the snake is moving in all 4 directions


# TODO : also test random positions

def test_move_left():
    position = (5,5) # x, y
    new_position = move(position, 'left')
    assert new_position == (4,5)     # assert command: assert is throughing an exception 

def test_move_left_from_somewhere_else():
    position = (5,0) # x, y
    new_position = move(position, 'left')
    assert new_position == (4,0)     # assert command: assert is throughing an exception 

def test_move_right():
    position = (5,5) # x, y
    new_position = move(position, 'right')
    assert new_position == (6,5)     # assert command: assert is throughing an exception 


def test_move_up():
    position = (5,5) # x, y
    new_position = move(position, 'up')
    assert new_position == (5,6)     # assert command: assert is throughing an exception 

def test_move_down():
    position = (5,5) # x, y
    new_position = move(position, 'down')
    assert new_position == (5,4)     # assert command: assert is throughing an exception 

def test_move_fraction():
    """This is an example of code that is not supposed to work"""
    position = (3.1415,5) # x, y
    with pytest.raises(Exception):
        move(position, 'down')

# To run the pyteest fole just press 
# pytest in terminal or pytest test_snake.py
