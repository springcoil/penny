from setuptools import setup
import os

try:
   import pypandoc
   long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
   long_description = open('README.md').read()

setup(name='penny',
      version='0.3.1',
      description='Inspect csv files and lists of data',
      long_description=long_description,
      url='https://github.com/gati/penny',
      download_url ='https://github.com/gati/penny/tarball/0.3.1',
      author='Jonathon Morgan',
      author_email='jonathon@goodattheinternet.com',
      license='MIT',
      packages=['penny'],
      test_suite='tests',
      install_requires=['python-dateutil'],
      package_data = {
            'penny': ['data/*.csv'],
      },
      zip_safe=False)