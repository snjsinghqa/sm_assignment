import pytest

@pytest.mark.run(order=3)
def test_C(oneTimeSetup,setUp):
    print("Test case first 'C'")

@pytest.mark.run(order=1)
def test_D(oneTimeSetup,setUp):
    print("Test case Second 'D'")

@pytest.mark.run(order=4)
def test_E(oneTimeSetup,setUp):
    print("Test case Second 'E'")

@pytest.mark.run(order=2)
def test_F(oneTimeSetup,setUp):
    print("Test case first 'F'")

@pytest.mark.run(order=6)
def test_G(oneTimeSetup,setUp):
    print("Test case Second 'G'")

@pytest.mark.run(order=5)
def test_H(oneTimeSetup,setUp):
    print("Test case Second 'H'")
# D,F,C,E,H,G