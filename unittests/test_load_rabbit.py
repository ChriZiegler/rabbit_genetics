'''
Test for loading the rabbit object
'''
import unittest

from rabbit_genetics.json_readers import litter_reader, reader_utils
from rabbit_genetics.rabbit_utils import rabbit

class TestLoadRabbit(unittest.TestCase):
    '''
    Tests related to reading in rabbit litters
    '''
    def setUp(self):
        '''
        Comparison fixtures
        '''
        self.rabbit1 = rabbit.Rabbit(1, {'B':[0, 1]})
        self.rabbit2 = rabbit.Rabbit(2, {'B':[0, 1]})
        self.rabbit7 = rabbit.Rabbit(7, {'B':[0, 1]})
        self.rabbit9 = rabbit.Rabbit(9, {'B':[1, 1]})
        self.abspath = 'C:/Users/Christie/Dropbox/OOP/rabbit_genetics/rabbit_genetics/'

    def test_load_starter_data(self):
        '''
        Test that you can load a litter with rabbit data
        '''
        path = self.abspath + 'unittests/fixtures/test_litter_starter.json'
        litter = litter_reader.read_litter(path)

        self.assertEqual(self.rabbit1.rabbit_id, litter[1].rabbit_id)
        self.assertEqual(self.rabbit2.rabbit_id, litter[2].rabbit_id)

    def test_load_save_data(self):
        '''
        Test that you can load a more complicated litter with rabbit data
        '''
        path = self.abspath + 'unittests/fixtures/test_litter_savefile.json'
        litter = litter_reader.read_litter(path)

        self.assertEqual(self.rabbit7.rabbit_id, litter[7].rabbit_id)
        self.assertEqual(self.rabbit9.rabbit_id, litter[9].rabbit_id)

if __name__ == '__main__':
    unittest.main()
