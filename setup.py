from setuptools import setup

setup(
   name='OStools',
   version='1.0',
   description='A useful module for os tools',
   author='Mike Howard',
   author_email='mshiznitzh@gmail.com',
   packages=['OStools'],  #same as name
   install_requires=['os.path'], #external packages as dependencies
)