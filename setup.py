from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = "MathOCRLibrary"
DESCRIPTION = "Open source math OCR with ML"
URL = "https://github.com/4Mens4Coding/MathOCRLibrary/tree/master/MathOCRLibrary"
EMAIL = "valentk777@gmail.com"
AUTHOR = "dogecode, tomas-drasutis, DeividasBrazenas, valentk777"
REQUIRES_PYTHON = ">=3.6.0"
VERSION = "1.0"

# What packages are required for this module to be executed?
REQUIRED = [
    # 'requests', 'maya', 'records',
]

setup(
    name = NAME,
    version = about['__version__'],
    description = DESCRIPTION,
    long_description = long_description,
    long_description_content_type = "text/markdown"
    author = AUTHOR,
    author_email = EMAIL,
    python_requires = REQUIRES_PYTHON,
    url = URL,
    packages = find_packages(),
    install_requires = REQUIRED,
    # install_requires = ['numpy >= 1.11.1', 'matplotlib >= 1.5.1'],
    classifiers = ["Programming Language :: Python :: 3.6"]
)
