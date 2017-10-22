'''
Reader for litter json files
'''

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
      list of Rabbit objects
    '''
    return True
