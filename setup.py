from setuptools import find_packages, setup

# read Readme file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="partitions",
    version="1.0.0",
    python_requires='>3.5.0',
    description="Generates partitions of a positive integer",
    author="Michael Anderson",
    url="https://github.com/mbanders/partitions.git",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    package_data={"": ["*.txt", "*.json", "*.cfg", "*.md"]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
        ],
    entry_points={"console_scripts": ["partitions=partitions.main:main"],},
)
