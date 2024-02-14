import setuptools
from typing import List

PROJECT_NAME = "kafka"
VERSION = "0.0.0"
AUTHOR_NAME = "prasad535"
AUTHOR_EMAIL = "prasad.nagineni12345@gmail.com"
DESCRIPTION = "Kafka data pipeline"

REQUIREMENTS_FILE_NAME = "requirements.txt"

HYPEN_E_DOT = "-e ."


def get_requirements_list() -> List[str]:
    """
    Description : This function get the list of the all the library names from the requirements.txt file

    Return : It returns requirements list
    """
    with open(REQUIREMENTS_FILE_NAME, 'r') as f:
        requirements_list = f.readlines()
        requirements_list = [requirement_name.replace("\n", "") for requirement_name in requirements_list]

        if HYPEN_E_DOT in requirements_list:
            requirements_list.remove(HYPEN_E_DOT)
    
    return requirements_list

setuptools.setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    packages=setuptools.find_packages(),
    install_requires=get_requirements_list()
)


