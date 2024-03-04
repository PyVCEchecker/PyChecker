"""
Setup for indico apis
"""
import sys

PY2 = True if sys.version_info[0] == 2 else False
PY3 = not PY2

REQUIREMENTS = [
    "msgpack==0.5.6",
    "msgpack-numpy==0.4.1",
    "Pillow<6.0.0",
    "requests>=2.2.1",
    "setuptools>=36.5.0",
    "six>=1.3.0",
]

# shim for futures support
if PY2:
    REQUIREMENTS.append("futures>=3.0.0")
    REQUIREMENTS.append("numpy<1.17")
else:
    REQUIREMENTS.append("numpy>=1.14.1")

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name="IndicoIo",
    version="1.4.1",
    packages=[
        "indicoio",
        "indicoio.text",
        "indicoio.image",
        "indicoio.multi",
        "indicoio.utils",
        "indicoio.custom",
        "indicoio.pdf",
        "indicoio.docx",
        "indicoio.detection",
        "tests",
    ],
    description="""A Python Wrapper for indico. Use pre-built state of the art machine learning algorithms with a single line of code.""",
    license="MIT License (See LICENSE)",
    long_description=open("README.rst").read(),
    url="https://github.com/IndicoDataSolutions/indicoio-python",
    author="Alec Radford, Slater Victoroff, Aidan McLaughlin, Madison May, Anne Carlson",
    author_email="engineering@indico.io",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    setup_requires=["six >= 1.3.0", "pillow >= 2.8.1"],
    tests_require=["mock >= 1.3.0, < 2.0.0", "nose >= 1.0", "numpy == 1.16.2"],
    test_suite="nose.collector",
    install_requires=REQUIREMENTS,
)
