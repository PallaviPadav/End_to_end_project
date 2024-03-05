from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirement(file_path:str)->List[str]:
    ''' this function will return the requirement'''
    requirement=[]
    with open(file_path) as file_obj:
        requiremnt=file_obj.readlines()
        requirement=[req.replace("\n","") for req in requirement]

        if HYPEN_E_DOT in requirement:
            requirement.remove(HYPEN_E_DOT)
    return requirement
    


setup(
name= 'END_to_END',
version= '0.0.1',
author= 'Pallavi',
author_email='pallavi.padav@gmail.com',
packages=find_packages(),
install_requires=get_requirement('requirement.txt')
)

