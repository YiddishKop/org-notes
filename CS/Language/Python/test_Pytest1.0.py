import Pytest1

def test_calc_total():
    total = Pytest1.calc_total(4, 5)
    assert total == 9

def test_calc_multiply():
    resutl = Pytest1.calc_multiply(10, 3)
    assert resutl == 30
