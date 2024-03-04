import setuptools

with open("README.md", 'r') as file_handler:
    long_description  = file_handler.read()

setuptools.setup(
    name="is-the-build-done-yet",
    version="1.0.0",
    author="Josiah Craw",
    author_email="jos@joscraw.net",
    description="Make Hue lights change colour when a subprocess is complete",  
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JosiahCraw/Is-the-Build-Done-Yet",
    packages=setuptools.find_packages(),
    entry_points='''
        [console_scripts]
        itbdy=is_the_build_done_yet.is_the_build_done_yet:main
    ''',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
