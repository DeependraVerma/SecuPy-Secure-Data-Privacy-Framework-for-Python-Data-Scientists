from setuptools import setup, find_packages
from typing import List

with open('README.rst', 'r', encoding='utf-8') as f:
    long_description = f.read()     

HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str)-> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

__version__ = "0.1.1"
REPO_NAME = "SecuPy-Secure-Data-Privacy-Framework-for-Python-Data-Scientists"
PKG_NAME= "securedf"
AUTHOR_USER_NAME = "DeependraVerma"
AUTHOR_EMAIL = "deependra.verma00@gmail.com"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Protect sensitive data with securedf, a Python package offering encryption, anonymization, and compliance tools for data scientists.",
    long_description=long_description,
    long_description_content="text/x-rst",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires = ["pandas", "faker","cryptography"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    )