import hashlib


class _Digest:
    def __init__(self, digest: bytes) -> None:
        self._digest = digest

    def digest(self) -> bytes:
        return self._digest


def xxh3_128(data: bytes) -> _Digest:
    return _Digest(hashlib.blake2b(data, digest_size=16).digest())
