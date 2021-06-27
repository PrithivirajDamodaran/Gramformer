import setuptools

setuptools.setup(
    name="gramformer",
    version="0.1",
    author="prithiviraj damodaran",
    author_email="d.prithiviraj@gmail.com",
    description="Gramformer",
    long_description="A framework for detecting, highlighting and correcting grammatical errors on natural language text",
    url="https://github.com/PrithivirajDamodaran/Gramformer.git",
    packages=setuptools.find_packages(),
    install_requires=['transformers', 'sentencepiece', 'python-Levenshtein', 'fuzzywuzzy'],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: Apache 2.0",
        "Operating System :: OS Independent",
    ],
)

