# Characterizing and Detecting Python Version Incompatibilities Caused by Inconsistent Version Specifications

> ## PyChecker
PyChecker is a lightweight static detection tool for detecting PDSpecErrs, 
which can help TPP developers to improve TPP configuration quality before publishing them. 
PyChecker consists of three components specialized for inspecting PDSpecErrs associated with the three diagnostic patterns.
Specifically, the three parts of PyChecker include: 
(1) detecting setup script issues by checking if the version specifications of the configuration entries are consistent; 
(2) detecting incompatible features by checking the consistencies between the programs’ features and configuration entries; (3) detecting python version conflicts by checking the consistencies of Python version specifications between the TPPs and its (in)direct dependencies. 
Given a TPP release, when PyChecker finishes the detection and finds any PDSpecErr, 
it generates a bug report that contains the key information of detected PDSpecErrs.



### Installation
* Clone this repository
```bash
git clone https://github.com/PyVCEchecker/PyChecker.git
```
* Install local (requires Python>=3.9)
```bash
cd PyVCEchecker/code
python setup.py install
```

### Instruction
```bash
pychecker

usage: pychecker [-h] [-p PACKAGE] [-v VERSION] [-r ROOT] [-c PYTHON_REQUIRES]
                 [-d INSTALL_REQUIRES]

PyChecker: check whether your project's Require-Python is right

optional arguments:
  -h, --help            show this help message and exit

package:
  -p PACKAGE, --package PACKAGE
                        Package name
  -v VERSION, --version VERSION
                        Version of the package

project:
  -r ROOT, --root ROOT  Root path of the project
  -c PYTHON_REQUIRES, --python_requires PYTHON_REQUIRES
                        python_requires expression
  -d INSTALL_REQUIRES, --install_requires INSTALL_REQUIRES
                        Path of requirements.txt
```
For example, 
```bash
pychecker -p django-chroniker -v 1.0.22
```


### Detection Result
For a TPP release, Pychecker sequentially detects setup script issues, 
incompatible features and version conflicts. 
After finishing the detection, if one or more PDSpecErrs are found, 
PyChecker will generate a bug report for them. 
The report contains the key information of found PDSpecErrs, 
including the root cause and the recommended range of Python distributions.
```
An example of the generated report is shown below: 

--------- root cause 2: using incompatible feature---------
cause : using incompatible feature
current python requires : >=3.6
-----------------------------------------------------------
error file : ./src/astral/location.py
specific cause : module: <dataclasses> do not support python ['3.6']
-----------------------------------------------------------
suggest python requires : >=3.7
```


> ## Exploratory study and experimental result
The study and experimental results are in folder ``data``.

> ### All packages
The file ``all_pyckages.csv`` lists the 534 packages we used in our exploratory study.
The table structure is shown below.

| No    | Package | Version | Incompatible python version | Resource type |
| :----:| :----:  | :----:  | :----:                      | :----:        | 

> ### PyErrs packages
The file ``pyerrs_pyckages.csv`` lists the 292 pyerrs we did root cause analysis, and they are also ground truth.
The table structure is shown below.

| No    | Package | Version | Incompatible python version |  Root cause | Error occuring time |
| :----:| :----:  | :----:  | :----:                      | :----:      |  :----:             |

> ### Experiment result for RQ3
The file ```` lists the PyErrs detected by our tool PyChecker. 
The table structure is shown below.

### RQ3_TCon
The file ``RQ3_TCon.csv`` lists detection result for RQ3. The table structure is shown below.
| No    | Package | Version | Incompatible python version | Resource type | Experiment result |
| :----:| :----:  | :----:  | :----:                      | :----:        |  :----:           |

### RQ3_TPoten
The file ``RQ3_TPoten.csv`` lists detection result forRQ3. The table structure is shown below.

| No    | Package | Version | Experiment result |
| :----:| :----:  | :----:  |  :----:           |

> ### Reported issues for RQ4
We randomly selected 80 detected PyErrs for further report and found that 28 issues are fixed at their follow-up versions. The results are shown in the following parts, i.e., 52 reported issues and 28 already fixed libraries. 

### 28 already fixed libraries
The file ``RQ4_fixed.csv`` lists the 28 already fixed libraries for RQ4. The table structure is shown below.

| No    | Root Cause | Library | Buggy version | Fixed version |
| :----:| :----:     | :----:  | :----:        | :----:        |


### 52 reported issues
The file ``RQ4_reported.csv`` lists the 52 reported issues for RQ4.  The table structure is shown below.

| No    | Status | Root Cause | Library | star      | Issue url | Fixed url |
| :----:| :----: | :----:     | :----:  | :----:    | :----:    | :----:    |



