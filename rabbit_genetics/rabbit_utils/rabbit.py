'''
Rabbit object and functions directly related to the rabbit object.
'''

class Rabbit(object):
    '''
    The rabbit object is responsible for holding information about genes
    related to each rabbit. This genetic information is passed on to the
    graphics controller. The rabbit is also responsible for breeding with
    other rabbits to create more rabbits.
    '''
    def __init__(self, rabbit_id, genotype):
        '''
        Create the rabbit object. Rabbit objects are defined in json files

        args:
          rabbit_id (int): Unique ID for this rabbit
          genes (dict): Dict mapping gene names to a list of two alleles.
        '''
        self.rabbit_id = rabbit_id
        self.genotype = genotype

    def public_method_1(self):
        pass
    def public_method_2(self):
        pass
