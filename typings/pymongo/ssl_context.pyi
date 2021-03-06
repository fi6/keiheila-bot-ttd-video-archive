"""
This type stub file was generated by pyright.
"""

import ssl as _ssl

"""A fake SSLContext implementation."""
PROTOCOL_SSLv23 = getattr(_ssl, "PROTOCOL_TLS_CLIENT", _ssl.PROTOCOL_SSLv23)
OP_NO_SSLv2 = getattr(_ssl, "OP_NO_SSLv2", 0)
OP_NO_SSLv3 = getattr(_ssl, "OP_NO_SSLv3", 0)
OP_NO_COMPRESSION = getattr(_ssl, "OP_NO_COMPRESSION", 0)
OP_NO_RENEGOTIATION = getattr(_ssl, "OP_NO_RENEGOTIATION", 0)
HAS_SNI = getattr(_ssl, "HAS_SNI", False)
IS_PYOPENSSL = False
SSLError = _ssl.SSLError
