# Contributing to dmp

## Setup

Once in your development environment, create a virtualenv
and install the appropriate linting tools and dependencies:

    $ cd <path/to/dmp>
    $ make dev
    $ source .venv/bin/activate


## Notes

dmp is a partial fork of [diff-match-patch][],
with extra bits to make this a modern, friendly
member of the Python packaging ecosystem. The
library will be periodically updated with changes
from the upstream project. If you would like to
contribute fixes or improvements to the library
itself, and not the packaging code, please submit
them to the upstream library directly.

[diff-match-patch]: https://github.com/google/diff-match-patch
