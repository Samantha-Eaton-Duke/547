# this module will test the line.py module


#@pytest.mark.parametrize("x1, y1, x2, y2, x, expected", [
 #   [-5, 10, -3, 4, -4, 7],
  #  [-5, 10, -3, 4, -3, 4],
   # [-5, 10, -3, 4, -3.5, 5.5],
    #])


def test_line_point():
    from line import line_point
    result = line_point(-5, 10, -3, 4, -4)
    expected = 7
    assert result == expected