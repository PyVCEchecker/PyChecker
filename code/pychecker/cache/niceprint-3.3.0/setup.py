from setuptools import setup
import pathlib
import os

here = pathlib.Path(__file__).parent
os.chdir(here)
setup(
  name="niceprint",
  version="3.3.0",
  license="GNU 3",
  url="https://niceprint.readthedocs.io/en/latest/",
  description="A minute package for formating output",
  long_description=str(open('README.md').read()),
  long_description_content_type="text/markdown",
  author="AstralDev",
  author_email="ekureedem480@gmail.com",
  python_requires='>=3',
  install_requires=["json"],
  py_modules=["niceprint"]
)
