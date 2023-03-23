from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements
    
    
setup(
    name='bostonhousepricing',
    version='0.0.1',
    author='Saket',
    author_email='sakettrivedi.trivedi3@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    
    
)