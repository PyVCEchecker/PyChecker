from .api_constants import apilevel, threadsafety, paramstyle
from .connect import connect
from .constructors import Date, Time, Timestamp
from .exceptions import Error, InterfaceError, DatabaseError, ParameterError
from .data_types import STRING, BINARY, NUMBER, DATETIME, ROWID
from .options import make_options
from turbodbc_intern import Rows, Megabytes

import pkg_resources

try:
    __version__ = pkg_resources.get_distribution(__name__).version
except:
    __version__ = 'unknown'
