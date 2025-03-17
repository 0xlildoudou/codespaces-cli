from setuptools import setup, find_packages

setup(
    name='codespaces-cli',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'codespaces-cli=codespaces_cli.codespaces_cli:main',
        ],
    },
    author='0xlildoudou',
    description='A CLI tool for managing GitHub Codespaces',
    url='https://github.com/0xlildoudou/codespaces-cli',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
)