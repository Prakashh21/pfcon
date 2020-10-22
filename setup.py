
from os import path
from setuptools import find_packages, setup


with open(path.join(path.dirname(path.abspath(__file__)), 'README.rst')) as f:
    readme = f.read()

setup(
      name             =   'pfcon',
      version          =   '3.0.0.0',
      description      =   '(Python) Process and File Controller',
      long_description =   readme,
      author           =   'Rudolph Pienaar',
      author_email     =   'rudolph.pienaar@gmail.com',
      url              =   'https://github.com/FNNDSC/pfcon',
      packages         =   find_packages(),
      install_requires =   ['pudb', 'nose', 'pfurl', 'pfmisc', 'Flask', 'Flask_RESTful',
                            'environs'],
      test_suite       =   'nose.collector',
      tests_require    =   ['nose'],
      scripts          =   ['bin/pfcon'],
      license          =   'MIT',
      zip_safe         =   False,
      python_requires  =   '>=3.5'
     )
