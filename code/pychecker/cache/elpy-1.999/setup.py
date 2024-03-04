import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="elpy",
    version="1.999",
    author="Josiah Boning",
    author_email="jboning@gmail.com",
    description="Tombstone package for elpy to not break accidental dependencies",
    long_description=long_description,
    long_description_content_type="text/markdown",
    #url="https://github.com/jboning/elpy-tombstone",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

