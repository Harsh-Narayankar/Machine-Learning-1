from setuptools import find_packages, setup
''' 
*setuptools* : Helps to build the package
*find_packages* : This will and find out all the pakages (folders with __init__.py)
*setup* : Entry point (like function) that define metadata and configuration(arrangment/ pars of element in a perticular way)
'''

from typing import List

def get_requirements(file_path:str)->List[str]:
    # :str and ->List [str] is just to help to read code and handle error
    
    requirements =[]
    with open(file_path) as objs:
        requirements = objs.readlines()
        requirements = [req.replace("/n", "") for req in requirements]

        # also remove that -e .
        if "-e ." in requirements:
            requirements.remove('-e .')

    return requirements






setup(

    name = 'Machine learning project END-END',
    version = '0.0.1',
    author = 'Harsh Narayankar',
    author_email='harshnnarayankar@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),

)