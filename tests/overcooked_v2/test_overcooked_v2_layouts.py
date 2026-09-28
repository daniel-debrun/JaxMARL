import pytest

from jaxmarl.environments.overcooked_v2.layouts import Layout, overcooked_v2_layouts


def test_builtin_layouts_are_enclosed():
    assert len(overcooked_v2_layouts) > 0


@pytest.mark.parametrize(
    "grid",
    [
        "\nWWWWW\nA   0\nWWWWW\n",  # walkable left and right edges
        "\nWWW\nWA  W\nWWW0W\n",  # a short top row is padded with floor
    ],
)
def test_walkable_border_is_rejected(grid):
    with pytest.raises(ValueError, match="border"):
        Layout.from_string(grid, possible_recipes=[[0, 0, 0]])


def test_border_may_hold_pots_piles_and_goals():
    Layout.from_string("\nWWPWW\n0A AB\nWWXWW\n", possible_recipes=[[0, 0, 0]])
