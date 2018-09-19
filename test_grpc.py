import grpc

from config import (
    RPC_SERVER_LISTEN_IP,
    RPC_SERVER_PORT,
    RPC_CLIENT_IP,
    RPC_CLIENT_PORT,
)
from constants import (
    COLLATION_TOPIC_FORMAT,
    UNKNOWN_TOPIC,
)
from grpc_client import (
    GRPCClient,
)
from grpc_server import (
    GRPCServer,
)
from message import (
    Collation,
    CollationRequest,
    MsgType,
)

import github.com.ethresearch.sharding_p2p_poc.pb.event.event_pb2 as event_pb2
import github.com.ethresearch.sharding_p2p_poc.pb.event.event_pb2_grpc as event_pb2_grpc
import github.com.ethresearch.sharding_p2p_poc.pb.message.message_pb2 as message_pb2
import github.com.ethresearch.sharding_p2p_poc.pb.rpc.rpc_pb2_grpc as rpc_pb2_grpc


def make_event_stub():
    dial_addr = "{}:{}".format(RPC_SERVER_LISTEN_IP, RPC_SERVER_PORT)
    channel = grpc.insecure_channel(dial_addr)
    return event_pb2_grpc.EventStub(channel)


def send_receive():
    """Test if `Receive` servicer works
    """
    stub = make_event_stub()
    cr = CollationRequest(1, 2, "")
    req = event_pb2.ReceiveRequest(
        peerID="",
        topic="",
        msgType=MsgType.CollationRequest,
        data=cr.to_bytes(),
    )
    stub.Receive(req)


# Client

def make_collation_topic(shard_id):
    return COLLATION_TOPIC_FORMAT.format(shard_id)


class P2PClient:
    rpc_client = None

    def __init__(self, rpc_client):
        self.rpc_client = rpc_client

    def broadcast_collation(self, collation):
        topic = make_collation_topic(collation.shard_id)
        collation_bytes = collation.to_bytes()
        self.rpc_client.broadcast(topic, MsgType.Collation, collation_bytes)
        return True

    def request_collation(self, peer_id, shard_id, period, collation_hash):
        req = CollationRequest(shard_id, period, collation_hash)
        req_bytes = req.to_bytes()
        res_bytes = self.rpc_client.send(peer_id, MsgType.CollationRequest, req_bytes)
        return Collation.from_bytes(res_bytes)


def make_grpc_stub():
    dial_addr = "{}:{}".format(RPC_CLIENT_IP, RPC_CLIENT_PORT)
    channel = grpc.insecure_channel(dial_addr)
    return rpc_pb2_grpc.PocStub(channel)


def test_grpc_client():
    stub = make_grpc_stub()
    rpc_client = GRPCClient(stub)
    rpc_client.subscribe_shards([0, 1])
    rpc_client.unsubscribe_shards([0])
    assert 1 in rpc_client.get_subscribed_shards()
    # print(rpc_client.get_subscribed_shards())
    # print(rpc_client.subscribe_shards([40, 56]))  # RPC should fail when subscribing an invalid shard
    # print(rpc_client.get_subscribed_shards())
    # print(rpc_client.unsubscribe_shards([40]))
    # print(rpc_client.get_subscribed_shards())
    # print(rpc_client.broadcast_collation(56, 10, 5566, 100))
    # print(rpc_client.send_collation(56, 1, b'123'))

    # peer_id_0 = "QmS5QmciTXXnCUCyxud5eWFenUMAmvAWSDa1c7dvdXRMZ7"
    peer_id_1 = "QmexAnfpHrhMmAC5UNQVS8iBuUUgDrMbMY17Cck2gKrqeX"

    p2p_client = P2PClient(rpc_client)
    c1 = Collation(1, 2, b"\xbe\xef")
    assert p2p_client.broadcast_collation(c1)
    c2 = p2p_client.request_collation(peer_id_1, 1, 2, "")
    assert c2.shard_id == 1
    assert c2.period == 2
