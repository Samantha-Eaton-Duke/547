# test_blood_calculator.py


import pytest

# generic testing functon that takes two inputs, the function input and the
# expected answer

# @ indicates a decorator


@pytest.mark.parametrize("input_HDL, expected", [
    [70, "Normal"],
    [45, "Borderline Low"],
    [20, "Low"],
])
# will run these values three times in the test funciton
def test_check_HDL(input_HDL, expected):
    from blood_calculator import check_HDL
    answer = check_HDL(input_HDL)
    assert answer == expected
