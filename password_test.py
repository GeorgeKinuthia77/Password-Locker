import unittest
from password import User
from password import Credentials


class TestUser(unittest.TestCase):
    '''
    Test class that defines tests for User class behaviours
    Args:
        unittest.TestCase: TestCase class that helps create test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test instance
        '''
        self.new_user = User("GeorgeKinuthia77","Instagram","ptex")# Instance of class User

    def test_init(self):
        '''
        Test case to test if object is initialised properly
        '''
        self.assertEqual(self.new_user.username, "GeorgeKinuthia77")
        self.assertEqual(self.new_user.account, "Instagram")
        self.assertEqual(self.new_user.password, "ptex")
