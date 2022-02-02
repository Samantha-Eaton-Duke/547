# this module will test the line.py module

import pytest

@pytest.mark.parametrize("in_x1, in_y1, in_x2, in_y2, in_x, expected", [
    [-5, 10, -3, 4, -4, -3],
    ])


#def test_line_point():
#    from line import line_point
#    result = line_point(-5, 10, -3, 4, -4)
#    expected = 7
#   assert result == expected
    
def test_line(in_x1, in_y1, in_x2, in_y2, in_x, expected):
    from line import calculate_slope
    result = calculate_slope(in_x1, in_y1, in_x2, in_y2, in_x)
    #expected = -3
    assert result == expected
    

    #[-5, 10, -3, 4, -3, 4],
    #[-5, 10, -3, 4, -3.5, 5.5],