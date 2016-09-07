from setuptools import setup, find_packages
import sys, os

version = '0.1.0'

setup(name='nisteag',
      version=version,
      description="An implementation of recommendations from the NIST Electronic Authentication Guideline",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='nist electronic authentication guideline password security',
      author='Diogo Baeder',
      author_email='diogo.baeder@yougov.com',
      url='',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
