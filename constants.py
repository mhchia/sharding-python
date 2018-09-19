UNKNOWN_PID = ""
UNKNOWN_TOPIC = ""

INT_BYTES = 32

COLLATION_TOPIC_FORMAT = "shardCollations_{}"

# FIXME: use plain class instead of Enum now
class MsgType:
    UNKNOWN = -1
    COLLATION = 2
    COLLATION_REQUEST = 3
