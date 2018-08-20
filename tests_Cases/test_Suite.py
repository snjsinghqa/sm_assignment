import unittest
from tests_Cases.test_login import LoginTests
from tests_Cases.test_signout import SignOutTests

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignOutTests)
# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1,tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)