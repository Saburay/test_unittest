# setUp()-runs before each test method
# tearDown()-rens after each test method
import unittest
from shooter import Shooter


class ShooterTest(unittest.TestCase):
	'''Create(setUp) and delete(tearDown) class-instance '''
    def setUp(self):
        self.jake = Shooter('Jake')
        self.moc_data = [1,2,3,4,5,6,7]

    def tearDown(self):
    	self.moc_data = []

    def test_get_cash(self):
    	#jake = Shooter('jake')
	    self.jake.get_cash(500)
	    self.assertEqual(self.jake.money,1500)

    def test_greet(self):
    	#jake = Shooter('jake')
	    self.assertEqual(self.jake.greet(),'Hello!How are you?')
	    self.jake.money = 50
	    self.assertEqual(self.jake.greet(),'Hello!I need cash!')


if __name__ == '__main__':
	unittest.main()

#jake = Shooter('jake')