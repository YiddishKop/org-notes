import Pytest3
import pytest
# def test_calc_square():
#     result = Pytest3.calc_square(5)
#     assert result == 25

# def test_calc_square():
#     result = Pytest3.calc_square(1)
#     assert result == 1

# def test_calc_square():
#     result = Pytest3.calc_square(10)
#     assert result == 100

# so many duplicate
# combine them by add parameters to test func

@pytest.mark.parametrize("test_input, expected_output",
                         [
                             (5, 25),
                             (9, 81),
                             (10, 100)
                         ])
def test_calc_square(test_input, expected_output):
    result = Pytest3.calc_square(test_input)
    assert result == expected_output
