try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import os
import sys


def long_description():
    readme = os.path.join(os.path.dirname(__file__), 'README.md')
    with open(readme, 'r') as inf:
        readme_text = inf.read()
    return(readme_text)

#Check for dependencies
dependencies = []
if sys.platform == 'darwin':  # Mac
    dependencies.append('pyobjc-framework-Quartz')
elif sys.platform == 'win32':  # Windows
    dependencies.extend(['pyHook', 'pywin32'])
else:  # X11 (LInux)
    dependencies.append('python-xlib')

setup(name='PyUserInput',
      version='0.1.11',
      description='A simple, cross-platform module for mouse and keyboard control',
      long_description=long_description(),
      author='Paul Barton <pablo.barton@gmail.com>, Pepijn de Vos <pepijndevos@gmail.com>',
      author_email='pablo.barton@gmail.com',  # Replace with mailing list perhaps
      url='https://github.com/PyUserInput/PyUserInput',
      package_dir = {'': '.'},
      packages = ['pykeyboard', 'pymouse'],
      license='http://www.gnu.org/licenses/gpl-3.0.html',
      keywords='mouse,keyboard user input event',
      install_requires=dependencies,
      )
