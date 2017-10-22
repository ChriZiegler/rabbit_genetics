'''
Tests related to the rabbit object
'''
import unittest

from rabbit_genetics.rabbit_utils import rabbit

class TestRabbitInit(unittest.TestCase):
    '''
    Unittests for initializing a rabbit object
    '''
    def test_make_rabbit(self):
        '''
        Rabbit object initialzed with correct params
        '''
        my_rabbit = rabbit.Rabbit(1, {'B':[0, 1]})
        self.assertEqual(my_rabbit.rabbit_id, 1)
        self.assertEqual(my_rabbit.genotype['B'], [0, 1])

if __name__ == '__main__':
    unittest.main()
