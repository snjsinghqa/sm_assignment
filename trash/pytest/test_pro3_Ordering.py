import pytest

@pytest.mark.last
def test_case_add(oneTimeSetup,setUp):
    a=10
    b=20
    c=a+b
    print("Add method result is "+ str(c)+ " "  +"*"*20)
@pytest.mark.second_to_last
def test_case_sub(oneTimeSetup,setUp):
    a = 10
    b = 20
    c = a - b
    print("Sub method result is " + str(c)+ " " + "*" * 20)
@pytest.mark.first
def test_case_mul(oneTimeSetup,setUp):
    a = 8
    b = 20
    c = a * b
    print("Mul method result is " + str(c)+ " "  + "*" * 20)
@pytest.mark.second
def test_case_div(oneTimeSetup,setUp):
    a = 20
    b = 2
    c = a / b
    print("div method result is " + str(c)+ " "  + "*" * 20)
