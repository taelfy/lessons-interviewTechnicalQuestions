#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='challenge02package',
    version='0.1.0',
    description='Machine Learning Technical Challenge',
    author='User',
    author_email='user@email.com',
    license='LICENSE.txt',
    long_description=open('README.txt').read(),
    install_requires=[
        'numpy==1.23.0',
        'scikit-learn==1.1.1',
        'matplotlib==3.5.2',
        'Flask==2.1.2',
        'flask-restx==0.5.0',
    ],
    packages=find_packages(),
    package_data={'challenge02package': ['utils/artifacts/*.json']},
)
