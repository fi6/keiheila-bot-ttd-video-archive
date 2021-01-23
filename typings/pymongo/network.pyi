"""
This type stub file was generated by pyright.
"""

import struct
from bson.py3compat import PY3

"""Internal network layer helper methods."""
_UNPACK_HEADER = struct.Struct("<iiii").unpack
def command(sock_info, dbname, spec, slave_ok, is_mongos, read_preference, codec_options, session, client, check=..., allowable_errors=..., address=..., check_keys=..., listeners=..., max_bson_size=..., read_concern=..., parse_write_concern_error=..., collation=..., compression_ctx=..., use_op_msg=..., unacknowledged=..., user_fields=..., exhaust_allowed=...):
    """Execute a command over the socket, or raise socket.error.

    :Parameters:
      - `sock`: a raw socket instance
      - `dbname`: name of the database on which to run the command
      - `spec`: a command document as an ordered dict type, eg SON.
      - `slave_ok`: whether to set the SlaveOkay wire protocol bit
      - `is_mongos`: are we connected to a mongos?
      - `read_preference`: a read preference
      - `codec_options`: a CodecOptions instance
      - `session`: optional ClientSession instance.
      - `client`: optional MongoClient instance for updating $clusterTime.
      - `check`: raise OperationFailure if there are errors
      - `allowable_errors`: errors to ignore if `check` is True
      - `address`: the (host, port) of `sock`
      - `check_keys`: if True, check `spec` for invalid keys
      - `listeners`: An instance of :class:`~pymongo.monitoring.EventListeners`
      - `max_bson_size`: The maximum encoded bson size for this server
      - `read_concern`: The read concern for this command.
      - `parse_write_concern_error`: Whether to parse the ``writeConcernError``
        field in the command response.
      - `collation`: The collation for this command.
      - `compression_ctx`: optional compression Context.
      - `use_op_msg`: True if we should use OP_MSG.
      - `unacknowledged`: True if this is an unacknowledged command.
      - `user_fields` (optional): Response fields that should be decoded
        using the TypeDecoders from codec_options, passed to
        bson._decode_all_selective.
      - `exhaust_allowed`: True if we should enable OP_MSG exhaustAllowed.
    """
    ...

_UNPACK_COMPRESSION_HEADER = struct.Struct("<iiB").unpack
def receive_message(sock_info, request_id, max_message_size=...):
    """Receive a raw BSON message or raise socket.error."""
    ...

_POLL_TIMEOUT = 0.5
def wait_for_read(sock_info, deadline):
    """Block until at least one byte is read, or a timeout, or a cancel."""
    ...

if not PY3:
    ...
else:
    ...
