"""
This type stub file was generated by pyright.
"""

from enum import IntEnum

class Cert:
    """
    permission certification

    used in auth/data encrypt/decrypt
    """
    class Types(IntEnum):
        NOTSET = ...
        WS = ...
        WH = ...
    
    
    def __init__(self, *, type: Types = ..., client_id: str, client_secret: str, token: str, verify_token: str = ..., encrypt_key: str = ...) -> None:
        """
        all fields from bot config panel
        """
        ...
    
    def decrypt(self, data: bytes) -> str:
        """ decrypt data

        :param data: encrypted byte array
        :return: decrypted str
        """
        ...
    


