from setuptools import setup, find_packages
# find packages-> Find the packages from the directory
from typing import List


def get_requirements()->list[str]:
    requirements_list=list[str]=[]
    return requirements_list



setup(
    name='Sensor',
    version='0.0.1',
    author='Nikesh Raj Wagle',
    author_email='nikeshwagle30@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements()
)