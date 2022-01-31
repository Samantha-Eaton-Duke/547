

def test_line_point((x1,y1),(x2,y2), x):
    from line import line_point
    result = line_point((0,0), (2,2), 1)
    expected = 1
    assert result == expected