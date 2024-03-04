I first preprocessed data also considering phonetic similarity of alphabets based on some common problems of Indian names.
After that i implemented soundex and used it to find similarity of names.
If two names seems similar , I have implmented my improvised vowels/cosonants functions which clears the situation better and gives an improvised Output.

Requirements
============

-  Python 3 or higher and nltk

Installation
============

Using PIP via PyPI

.. code:: bash

    pip3 install indian_namematch



.. code:: bash

    python3



Usage
=====

.. code:: python

    >>> import indian_namematch
    >>> from indian_namematch import fuzzymatch

Single Comparison
~~~~~~~~~~~~~~~~~

.. code:: python

    >>> results = fuzzymatch.single_compare("A Singh", "Ajeet Singh")
    >>> print(results)
        Match
    >>> results = fuzzymatch.single_compare("Ajeit Singh", "Ajeet Singh")
    >>> print(results)
        Match
    >>> results = fuzzymatch.single_compare("Mr Ajeit Singh", "Ajeet Singh")
    >>> print(results)
        Match
    >>> results = fuzzymatch.single_compare("M/r Ajeit Singh", "Ajeet Singh")
    >>> print(results)

