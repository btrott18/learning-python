import unittest
from hello import Hello

class TestStringMethods(unittest.TestCase):

    def setUp(self): 
        self.classUnderTest = Hello()
    
    def tearDown(self) -> None:
        return super().tearDown()

    def test_standard_greet(self):
        self.assertEqual(self.classUnderTest.greet("John Smith"), "Hello John Smith!")

    def test_template_override(self):
        self.classUnderTest.setTemplate('Hi there {name}!')
        self.assertEqual(self.classUnderTest.greet("Jane"), "Hi there Jane!")    

if __name__ == '__main__':
    unittest.main()