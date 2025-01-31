from dataclasses import dataclass, field

from common.ctype import ctype

from .base import LoginServerPacket


@dataclass(kw_only=True)
class LoginOk(LoginServerPacket):
    type: ctype.char = field(default=3, repr=False, init=False)
    login_ok1: ctype.int32
    login_ok2: ctype.int32
    unknown_bytes: bytes = field(
        default=b"\x00\x00\x00\x00"
        b"\x00\x00\x00\x00"
        b"\xEA\x03\x00\x00"
        b"\x00\x00\x00\x00"
        b"\x00\x00\x00\x00"
        b"\x02\x00\x00\x00",
        init=False,
        repr=False,
    )
