import pytest

@pytest.mark.run(order=4)
def test_A(oneTimeSetup,setUp):
    print("Test case first 'A'")

@pytest.mark.run(order=3)
def test_B(oneTimeSetup,setUp):
    print("Test case Second 'B'")

@pytest.mark.run(order=1)
def test_third(oneTimeSetup,setUp):
    assert True

def test_second(oneTimeSetup,setUp):
    assert True

@pytest.mark.run(order=2)
def test_first(oneTimeSetup,setUp):
    assert True
