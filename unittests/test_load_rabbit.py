'''
Test for loading the rabbit object
'''
import unittest
from rabbit_genetics.json_readers import litter_reader

class TestLoadRabbit(unittest.TestCase):
    '''
    Tests related to reading in rabbit litters
    '''
    def test_load_rabbit_object(self):
        '''
        Test that you can load a rabbit object
        '''
        litter = litter_reader.read_litter('fixures/test_litter.json')
        self.assertNotEqual(litter, None)

if __name__ == '__main__':
    unittest.main()
