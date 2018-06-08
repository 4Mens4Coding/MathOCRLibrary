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

OPTIONAL = [
    "xlwt"
]

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    with open(os.path.join(here, NAME, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION

setup(
    name = NAME,
    version = about['__version__'],
    description = DESCRIPTION,
    long_description_content_type = "text/markdown",
    author = AUTHOR,
    author_email = EMAIL,
    python_requires = REQUIRES_PYTHON,
    url = URL,
    packages = find_packages(),
    install_requires = REQUIRED,
    extras_require = OPTIONAL,
    classifiers = ["Programming Language :: Python :: 3.6"]
)
