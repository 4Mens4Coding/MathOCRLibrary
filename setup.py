from setuptools import setup, find_packages

setup(
    name = 'MathOCRLibrary',
    version = '1.0.0',
    url = 'https://github.com/4Mens4Coding/MathOCRLibrary/tree/master/MathOCRLibrary',
    author = 'Author Name',
    author_email = 'author@gmail.com’,
    description = 'Description of my package',
    packages = find_packages(),    
    install_requires = ['numpy >= 1.11.1', 'matplotlib >= 1.5.1'],
)
