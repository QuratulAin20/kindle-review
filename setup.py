from setuptools import find_packages , setup
from typing import List


HYPHEN_E_DOT  = '-e . '


def get_requirement(file_path:str)->List[str]:
    '''
    list of requireemnts
    '''
    
    requirements=[]
    
    with open (file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n"," ") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
   
    return requirements





setup(
name = 'ML-Project',
version = '0.01',
author = 'Ain',
packages = find_packages(),
install_requirement = get_requirement('requirements.txt')    
    
)