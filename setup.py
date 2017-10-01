from setuptools import setup
from setuptools import find_packages
setup(
    name='pirant',
    version='0.1.4dev1',
    author="aayush",
    author_email='aayushsingh.mail@gmail.com',
    url="https://github.com/aayush26/pirant",
    license='MIT',
    description="DevRant wrapper in Python",
    classifiers=[
        'Programming Language :: Python :: 2.7',
    ],
    keywords="devrant api wrapper",
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[
        "colander",
        "requests",
    ],
    setup_requires=[
        "pytest-runner"
    ],
    tests_require=[
        'pytest'
    ]
)
