import io
import os
import re

from setuptools import find_packages, setup

# Get the version from chembench/__init__.py
# Adapted from https://stackoverflow.com/a/39671214
this_directory = os.path.dirname(os.path.realpath(__file__))
version_matches = re.search(r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                            io.open(f'{this_directory}/chembench/__init__.py', encoding='utf_8_sig').read())
if version_matches is None:
    raise Exception('Could not determine CHEMBENCH version from __init__.py')
__version__ = version_matches.group(1)

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(name='ChemBench',
      version=__version__,
      author='Shen Wanxiang',
      author_email='wanxiang.shen@u.nus.edu',
      description='MoleculeNet benchmark dataset & MolMapNet dataset',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/shenwanxiang/ChemBench',

      packages=find_packages(),

      install_requires=[
          'numpy>=1.16.3', 
          'tqdm>=4.32.1',
          'pandas>=0.24.2'
      ],      include_package_data=True,
      zip_safe=True,

      classifiers=(
          'Programming Language :: Python :: 3',
          'Operating System :: OS Independent',
      ),
      )
