import Pytest1
import pytest
import sys

@pytest.mark.skipif(sys.version_info < (3,5), reason = "I dont need test this fn")
def test_calc_total():
    total = Pytest1.calc_total(4, 5)
    assert total == 9

def test_calc_multiply():
    resutl = Pytest1.calc_multiply(10, 3)
    assert resutl == 30

@pytest.mark.window
def test_windows1():
    assert True

@pytest.mark.window
def test_windows2():
    assert True

@pytest.mark.mac
def test_mac1():
    assert True

@pytest.mark.mac
def test_mac2():
    assert True
