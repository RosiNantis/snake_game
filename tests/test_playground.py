"""
Tests for the Playground class:

- creating a Playground object works
- after creating a Playground object it has the correct size attribute
- food should be inside the Playground size
- add_random_food puts the food in random positions
- food is not placed on obstacles (boundaries)
- is_obstacle for a coordinate inside gives True
- is_obstacle for a coordinate at the boundary gives False
"""

from snake.playground import Playground

def test_create():
    """create a Playground object works"""
    p = Playground(10,11)
    # after creating a playground object it has the correct size attribute
    assert p.size == (10,11)

    def test_is_obstacle():
        """Check for obstacls on the playground
        - is obstacle for coordinate inside gives True
        - is obstacle for coordinate outside gives False
        """
        p = Playground(5,6)
        assert p.is_obstacle((3, 3)) is False
        assert p.is_obstacle((-1, -1)) is True
        assert p.is_obstacle((5, 6)) is True
        assert p.is_obstacle((0, 6)) is True
        assert p.is_obstacle((0, 0)) is True

