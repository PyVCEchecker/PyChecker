import setuptools

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

print(requirements)
setuptools.setup(
    name="GeoFuns",  # Replace with your own username
    version="1.1.8",
    author="Harry Ritchie",
    author_email="harry.ritchie@prea.eu",
    py_modules=['geofunctions'],
    description="A package for geo tools used to map card score",
    url="https://github.com/harryritchie/Landkarte",
    packages=["GeoFuns"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requirements)
