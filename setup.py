from setuptools import setup, find_packages
import sys, os

version = '0.4.0'

setup(
    name='nisteag',
    version=version,
    description="An implementation of recommendations from the NIST Electronic Authentication Guideline",
    long_description="""\
""",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Security',
    ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='nist electronic authentication guideline password security',
    author='Diogo Baeder',
    author_email='diogo.baeder@yougov.com',
    url='https://github.com/yougov/nisteag',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests', 'docs']),
    package_dir={'nisteag': 'nisteag'},
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'chardet>=2.3.0',
        'six>=1.10.0',
    ],
    entry_points={
        'console_scripts': [
            'check-entropy = nisteag.scripts.checkers:check_entropy'
        ],
    },
)
