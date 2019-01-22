from setuptools import setup

setup(
    name='pysys',
    version='0.1',
    license='MIT',
    description='A simple Python package that returns information about the system it is run on.',
    long_description=open('README.md').read(),
    install_requires=['psutil'],
    url='https://github.com/patrickjkennedy/pysys',
    author='Patrick Kennedy',
    author_email='patrickken@gmail.com'
)

