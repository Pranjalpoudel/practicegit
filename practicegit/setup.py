from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements=[]
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('#')]


    return requirements

setup(    
name='practicegit',
version='0.1.0',
author='Pranjal',
author_email="pranjalpaudel62@gmail.com",
description='A practice project for Git',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)