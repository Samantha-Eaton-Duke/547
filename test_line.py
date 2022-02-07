# this module will test the line.py module

import pytest

@pytest.mark.parametrize("in_x1, in_y1, in_x2, in_y2, in_x, expected", [
    [-5, 10, -3, 4, -4, -3],
    [-5, 10, -3, 4, -3, -3],
    [-5, 10, -3, 4, 0, -3],
    ])

   
def test_calculate_slope(in_x1, in_y1, in_x2, in_y2, in_x, expected):
    from line import calculate_slope
    result = calculate_slope(in_x1, in_y1, in_x2, in_y2, in_x)
    assert result == expected


@pytest.mark.parametrize("y1, m, x1, expected", [
    [10, -3, -5, -5],
    [10, -3, -5, -5],
    [10, -3, -5, -5],
    ])


def test_x_intercept(y1, m, x1, expected):
    from line import x_intercept
    result = x_intercept(y1, m, x1)
    assert result == expected


@pytest.mark.parametrize("m, x, b, expected", [
    [-3, -4, -5, 7],
    [-3, -3, -5, 4],
    [-3, 0, -5, -5],
    ])


def test_y_intercept(m, x, b, expected):
    from line import y_intercept
    result = y_intercept(m, x, b)
    assert result == expected
 

@pytest.mark.parametrize("x1,y1,x2,y2, x, expected", [
    [-5, 10, -3, 4, -4, 7],
    [-5, 10, -3, 4, -3, 4],
    [-5, 10, -3, 4, 0, -5],
    ])


def test_line_point(x1,y1,x2,y2, x, expected):
    from line import line_point
    result = line_point(x1,y1,x2,y2, x)
    assert result == expected