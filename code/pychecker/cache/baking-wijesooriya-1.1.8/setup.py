import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="baking-wijesooriya", # Replace with your own username
    version="1.1.8",
    author="Kiran Wijesooriya",
    author_email="kiranw1000@gmail.com",
    description="Contains functions named after the steps of baking to help with cake baking analogy for beginners.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)