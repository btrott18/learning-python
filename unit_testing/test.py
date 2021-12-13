# {name} bank account balance is ${amount}
# name can be up to 7 characters
# amount is > 0 and < 10,000,000
import unittest

def formatter(name, amount):
    name_diff= 7 - len(name)
    amount_diff=13 - len(amount)
    filler = (name_diff * " ") + (amount_diff * " ")
    # for i in range(0, amount_diff):
    #     filler += " "

    # if(amount_diff == 1):
    #     filler = " "
    # elif(amount_diff == 2):
    #     filler = "  "

    return f'{name}\'s bank account balance is ${filler + amount}'


print(formatter("Lee", "500.00"))
print(formatter("Bill", "10,500.00"))
print(formatter("Sally", "1,500,000.00"))
print(formatter("Ja", "9,999,999.00"))


class TestStringMethods(unittest.TestCase):

    def test_formatter(self):
        self.assertEqual(formatter("Brad", "10,000,000.00"), "Brad's bank account balance is $   10,000,000.00")
        self.assertEqual(formatter("Brad", "1,000,000.00"),  "Brad's bank account balance is $    1,000,000.00")
        self.assertEqual(formatter("Brad", "500.00"),        "Brad's bank account balance is $          500.00")
        self.assertEqual(formatter("Lee", "10,000,000.00"),  "Lee's bank account balance is $    10,000,000.00")


    

if __name__ == '__main__':
    unittest.main()