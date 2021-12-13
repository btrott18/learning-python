# python3 -m unittest discover -s . -p 'test*.py'

# or put all tests in their own dir and just look for that
# python3 -m unittest discover __tests__ 

import unittest
from unittest.mock import MagicMock

from data_manager import DataManager
from data_client import Client

class TestStringMethods(unittest.TestCase):

    def setUp(self): 
        self.classUnderTest = DataManager(Client())
    
    def tearDown(self) -> None:
        return super().tearDown()

    #Like an integration test, verify the things you know should be true about the data being returned
    def test_retrieve(self):
        actual = self.classUnderTest.retrieveUsers()

        self.assertIsNotNone(actual)
        self.assertTrue(len(actual) > 0)
        self.assertIsNotNone(actual[0].id)
        self.assertIsNotNone(actual[0].first_name)
        self.assertIsNotNone(actual[0].last_name)
        self.assertIsNotNone(actual[0].status)
        self.assertTrue(actual[0].status == "ACTIVE" or actual[0].status == "INACTIVE")

    #you can never know that an integration test will give you the correct data unless you have special test data built 
    # (in which case why not just mock it locally...), so in order to cover conditional logic you may need to mock data or API results
    def test_inactive_maps_properly(self):
        mockClient = Client()
        mockClient.retrieve = MagicMock(return_value=["1, John, Doe, 2"])
        self.classUnderTest = DataManager(mockClient)
        actual = self.classUnderTest.retrieveUsers()

        print(actual)

        self.assertIsNotNone(actual)
        self.assertTrue(len(actual) > 0)
        self.assertEqual(actual[0].id, "1")
        self.assertEqual(actual[0].first_name, "John")
        self.assertEqual(actual[0].last_name, "Doe")
        self.assertEqual(actual[0].status, "INACTIVE")


if __name__ == '__main__':
    unittest.main()