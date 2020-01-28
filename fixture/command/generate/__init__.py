from __future__ import absolute_import

class code_str(str):
    """string that reproduces without quotes.
    
    """
    def __repr__(self):
        return str.__repr__(self)[1:-1]

from . import generate
from .generate import *
__doc__ = generate.__doc__

# load modules so they can register themselves (better way?)
try:
    from . import generate_sqlobject
except ImportError:
    pass
try:
    from . import generate_sqlalchemy
except ImportError:
    pass