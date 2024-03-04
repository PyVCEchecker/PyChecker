import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="argali",
    version="0.1.8",
    author="Aaron Honour",
    author_email="aaron_honour@protonmail.com",
    description="Data Analysis Tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AaronHonour/argali",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)