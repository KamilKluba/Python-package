from setuptools import setup, find_packages

setup(
    name='DPP10_1',
    version='0.2',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A DPP python package',
    long_description=open('README.md').read(),
    install_requires=['string'],
    url='https://github.com/KamilKluba/Python-package',
    author='KamilKluba',
    author_email='226016@student.pwr.edu.pl'
)
