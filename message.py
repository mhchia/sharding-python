from eth_utils import (
    big_endian_to_int,
    int_to_big_endian,
)

INT_BYTES = 32


def int_to_bytes(value):
    if not isinstance(value, int):
        raise ValueError
    return bytes.rjust(int_to_big_endian(value), INT_BYTES)

def bytes_to_int(value):
    if not isinstance(value, bytes):
        raise ValueError("value should be bytes type")
    if len(value) != INT_BYTES:
        raise ValueError("len of bytes should be {}, instead of {}".format(INT_BYTES, len(value)))
    return big_endian_to_int(value.lstrip())


class Collation:
    shard_id = None
    period = None
    blobs = None

    def __init__(self, shard_id, period, blobs):
        self.shard_id = shard_id
        self.period = period
        self.blobs = blobs

    def to_bytes(self):
        return int_to_bytes(self.shard_id) + int_to_bytes(self.period) + self.blobs

    @classmethod
    def from_bytes(self, b):
        if len(b) < INT_BYTES * 2:
            raise ValueError("bytes too short for a collation: len={}".format(len(b)))
        return Collation(
            bytes_to_int(b[:INT_BYTES]),
            bytes_to_int(b[INT_BYTES:INT_BYTES * 2]),
            b[INT_BYTES * 2:],
        )
