import pytest
from trash.pytest.data_class import Data

@pytest.mark.usefixtures("oneTimeSetup","setUp")
class TestDataOfSum():

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.d=Data()

    def test_sum_function(self):
        result=self.d.add_two_number(20,30)
        print(result)
        assert result==50

    def test_sum_flot(self):
        result=self.d.add_two_number(21.5,12.6)
        print(result)
        assert result == 34.1
