'''
Reader for litter json files
'''
import json

from rabbit_genetics.rabbit_utils import rabbit

def read_litter(path):
    '''
    Read a rabbit litter from json. This litter contains all rabbits
    belonging to the player.

    The rabbit litter follows a specific json format.
    The litter var contains the information for the rabbit objects.
    Rabbit objects have the following attributes:
      ID (int): Unique ID of rabbit
      genotype (dict): Dictionary of all genes. Each gene name (as a string)
      maps to a list of length 2 that contains 2 ints. Each int corresponds to
      an allele for that gene.

    Example json file:

        var litter = [{
          "ID" : 1,
          "genotype" : {
                       "B": [0,1],
                       }
        },
        {
          "ID" : 2,
          "genotype" : {
                       "B": [0,1]
                       }
        }
        ]

    args:
      path (str): Path to json file containing litter data
    returns:
      dict of Rabbit objects, ID mapping to rabbit
    '''
    with open(path, 'r') as myfile:
        litter_data = json.loads(myfile.read())
    litter = {}
    for bunny in litter_data:
        litter[bunny['ID']] = rabbit.Rabbit(bunny['ID'], bunny['genotype'])
    return litter
