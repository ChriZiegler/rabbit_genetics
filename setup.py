'''
Setup
'''
from setuptools import setup, find_packages

setup(name='rabbit_genetics',
      version=0.1,
      description='Rabbit genetics simulator',
      url='https://github.com/ChriZiegler/rabbit_genetics',
      author='Christie Ziegler',
      author_email='chriziegler@gmail.com',
      license='MIT',
      packages=find_packages(),
      package_data={'rabbit_genetics.unittests':['unittests/fixtures/test_litter.json']},
      zip_safe=False
     )
