from sem1.SOAP.check_text import checkText
import pytest


def test_step1():
    assert "молоко" in checkText("малако")


if __name__ == '__main__':
    pytest.main(['-vv'])
