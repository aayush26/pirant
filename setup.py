from setuptools import setup
from setuptools import find_packages
setup(
    name='pirant',
    version='0.1.0devl',
    author = "aayush",
    url="https://github.com/aayush26/pirant",
    license='MIT',
    description = "DevRant wrapper in Python",
    classifiers=[
        'Programming Language :: Python :: 2.7',
    ],
    keywords="devrant api wrapper",
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[
        "colander",
        "requests",
    ]
)