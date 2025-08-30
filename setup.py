from setuptools import setup, find_packages
# find packages-> Find the packages from the directory
from typing import List


def get_requirements(file_path:str)->List[str]:
    """
    This will return the list of strings
    """
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.str.replace('/n','') for req in requirements]

        return requirements




setup(
    name='Sensor',
    version='0.0.1',
    author='Nikesh Raj Wagle',
    author_email='nikeshwagle30@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements()
)