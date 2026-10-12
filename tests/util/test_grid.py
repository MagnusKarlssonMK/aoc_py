"""Unit tests for the shared Grid helper in util.grid."""

from aoc_py.util.grid import Grid
from aoc_py.util.point import Point


def test_construction() -> None:
    grid = Grid("abc\ndef")
    assert grid.x_max == 3
    assert grid.y_max == 2
    assert grid.elements == ["a", "b", "c", "d", "e", "f"]


def test_new() -> None:
    grid = Grid.new(2, 3, ".")
    assert grid.x_max == 2
    assert grid.y_max == 3
    assert grid.elements == ["."] * 6


def test_get_element() -> None:
    grid = Grid("ab\ncd")
    assert grid.get_element(Point(0, 0)) == "a"
    assert grid.get_element(Point(1, 1)) == "d"
    assert grid.get_element(Point(-1, 0)) == ""
    assert grid.get_element(Point(2, 0)) == ""
    assert grid.get_element(Point(0, 2)) == ""


def test_find() -> None:
    grid = Grid("aab\nbaa")
    assert grid.find("a") == Point(0, 0)
    assert grid.find("b") == Point(2, 0)
    assert grid.find("a", reverse=True) == Point(2, 1)
    assert grid.find("z") == Point(-1, -1)
    assert grid.find("z", reverse=True) == Point(-1, -1)


def test_find_all() -> None:
    grid = Grid("aab\nbaa")
    assert grid.find_all("a") == [
        Point(0, 0),
        Point(1, 0),
        Point(1, 1),
        Point(2, 1),
    ]
    assert grid.find_all("z") == []


def test_get_index() -> None:
    grid = Grid("ab\ncd")
    assert grid.get_index(Point(0, 0)) == 0
    assert grid.get_index(Point(1, 1)) == 3
    assert grid.get_index(Point(-1, 0)) == -1
    assert grid.get_index(Point(2, 0)) == -1
    assert grid.get_index(Point(0, 2)) == -1


def test_get_point() -> None:
    grid = Grid("ab\ncd")
    assert grid.get_point(0) == Point(0, 0)
    assert grid.get_point(3) == Point(1, 1)


def test_set_point() -> None:
    grid = Grid("ab\ncd")
    grid.set_point(Point(0, 0), "z")
    assert grid.get_element(Point(0, 0)) == "z"
    grid.set_point(Point(2, 2), "y")
    assert grid.elements == ["z", "b", "c", "d"]


def test_str() -> None:
    assert str(Grid("ab\ncd")) == "ab\ncd\n"
