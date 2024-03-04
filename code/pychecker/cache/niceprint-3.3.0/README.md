# niceprint 

Description
-----------
This is a python package for printing text with different colors and styles. Best for printing results from CLI programs. Parts of the code is gotten from `color` package.

niceprint comes with a few other functionalities such as **SetInterval, ProgressBar, MultiColoredPrint.** and many [others](http://astraldev.github.io/niceprint#classes)

Installation
-------
```bash
$ pip3 install niceprint
```

Examples
---------
```python
from niceprint import Print
from niceprint import MultiColoredPrint as mcp

Print("Niceprint", color="c")

mcp("Niceprint", color="crb")

```

Documentation
-------------
Availiable at https://niceprint.readthedocs.io/en/latest/

View [changelog](CHANGELOG)


