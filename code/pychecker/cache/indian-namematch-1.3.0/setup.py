from setuptools import setup

def readme():
    with open("README.rst") as f:
        README = f.read()
    return README

setup(
    name="indian-namematch",
    version="1.3.0",
    description="Indian Fuzzy name Matching Tool.",
    long_description = readme(),
    long_description_content_type = "text/markdown",
    url="https://github.com/pypa/sampleproject",
    author="Siddhesh Sharma",
    author_email="siddheshatjuit@gmail.com",
    license = 'MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["indian_namematch"],
    include_package_data=True,
    install_requires = ["nltk","pyphonetics"]
)