"""
This type stub file was generated by pyright.
"""

from collections import namedtuple

"""Type codes for MongoDB servers."""
SERVER_TYPE = namedtuple('ServerType', ['Unknown', 'Mongos', 'RSPrimary', 'RSSecondary', 'RSArbiter', 'RSOther', 'RSGhost', 'Standalone'])(*range(8))
