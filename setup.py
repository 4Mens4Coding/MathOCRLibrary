from setuptools import setup, find_packages

setup(
    name = "MathOCRLibrary",
    version = "1.0",
    url = "https://github.com/4Mens4Coding/MathOCRLibrary/tree/master/MathOCRLibrary",
    author = "valentk777, dogecode, tomas-drasutis, DeividasBrazenas",
    author_email = "valentk777@gmail.com",
    description = "Description of my package",
    packages = find_packages(),    
    install_requires = ['numpy >= 1.11.1', 'matplotlib >= 1.5.1'],
)
