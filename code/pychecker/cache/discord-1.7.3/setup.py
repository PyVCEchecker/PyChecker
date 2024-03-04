from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='discord',
    version='1.7.3',
    url='https://github.com/Rapptz/discord.py',
    author='Rapptz',
    description='A mirror package for discord.py. Please install that instead.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=[],
    install_requires=['discord.py>=1.7.3'],
)
