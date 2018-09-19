import functools

import grpc

from config import (
    RPC_CLIENT_IP,
    RPC_CLIENT_PORT,
)
from constants import (
    COLLATION_TOPIC_FORMAT,
    UNKNOWN_PID,
    UNKNOWN_TOPIC,
)
from message import (
    MsgType,
    Collation,
    CollationRequest,
)


import github.com.ethresearch.sharding_p2p_poc.pb.message.message_pb2 as message_pb2
import github.com.ethresearch.sharding_p2p_poc.pb.rpc.rpc_pb2 as rpc_pb2
import github.com.ethresearch.sharding_p2p_poc.pb.rpc.rpc_pb2_grpc as rpc_pb2_grpc


def make_collation_topic(shard_id):
    return COLLATION_TOPIC_FORMAT.format(shard_id)


class CommandFailure(Exception):
    pass


class MockRPCStub:
    peers = None
    subscribed_shards = None

    def __init__(self):
        self.peers = set()
        self.subscribed_shards = set()

    def _make_empty_success_response(self):
        response = rpc_pb2.RPCPlainResponse()
        response.response.status = rpc_pb2.Response.SUCCESS
        return response

    def AddPeer(self, req):
        peer_addr = "{}:{}:{}".format(req.ip, req.port, req.seed)
        self.peers.add(peer_addr)
        return self._make_empty_success_response()

    def SubscribeShard(self, req):
        self.subscribed_shards = self.subscribed_shards.union(req.shardIDs)
        return self._make_empty_success_response()

    def UnsubscribeShard(self, req):
        self.subscribed_shards.difference_update(req.shardIDs)
        return self._make_empty_success_response()

    def GetSubscribedShard(self, req):
        shard_ids = list(self.subscribed_shards)
        response = rpc_pb2.RPCGetSubscribedShardResponse(
            shardIDs=shard_ids,
        )
        response.response.status = rpc_pb2.Response.SUCCESS
        return response

    def BroadcastCollation(self, req):
        return self._make_empty_success_response()

    def SendCollation(self, req):
        return self._make_empty_success_response()

    def StopServer(self, req):
        return self._make_empty_success_response()


def throw_if_not_success(response, request):
    if response.response.status != rpc_pb2.Response.SUCCESS:
        raise CommandFailure(
            "response={}, request={}".format(
                response,
                request,
            )
        )


class P2PRPCClient:
    stub = None

    def __init__(self, stub):
        self.stub = stub

    #
    # RPC for CLI usage
    #

    def add_peer(self, ip, port, seed):
        addpeer_req = rpc_pb2.RPCAddPeerRequest(
            ip=ip,
            port=port,
            seed=seed,
        )
        response = self.stub.AddPeer(addpeer_req)
        throw_if_not_success(response, addpeer_req)
        return response.response.message

    def subscribe_shards(self, shard_ids):
        subscribe_shards_req = rpc_pb2.RPCSubscribeShardRequest(shardIDs=shard_ids)
        response = self.stub.SubscribeShard(subscribe_shards_req)
        throw_if_not_success(response, subscribe_shards_req)
        return response.response.message

    def unsubscribe_shards(self, shard_ids):
        unsubscribe_shards_req = rpc_pb2.RPCUnsubscribeShardRequest(shardIDs=shard_ids)
        response = self.stub.UnsubscribeShard(unsubscribe_shards_req)
        throw_if_not_success(response, unsubscribe_shards_req)
        return response.response.message

    def get_subscribed_shards(self):
        getsubshard_req = rpc_pb2.RPCGetSubscribedShardRequest()
        response = self.stub.GetSubscribedShard(getsubshard_req)
        throw_if_not_success(response, getsubshard_req)
        return response.shardIDs

    def broadcast_collation(self, shard_id, num_collations, collation_size, frequency):
        broadcastcollation_req = rpc_pb2.RPCBroadcastCollationRequest(
            shardID=shard_id,
            number=num_collations,
            size=collation_size,
            period=frequency,
        )
        response = self.stub.BroadcastCollation(broadcastcollation_req)
        throw_if_not_success(response, broadcastcollation_req)
        return response.response.message

    def send_collation(self, shard_id, period, blobs):
        collation_msg = message_pb2.Collation(
            shardID=shard_id,
            period=period,
            blobs=blobs,
        )
        sendcollation_req = rpc_pb2.RPCSendCollationRequest(
            collation=collation_msg,
        )
        response = self.stub.SendCollation(sendcollation_req)
        throw_if_not_success(response, sendcollation_req)
        return response.response.message

    def stop_server(self):
        stopserver_req = rpc_pb2.RPCStopServerRequest()
        response = self.stub.StopServer(stopserver_req)
        throw_if_not_success(response, stopserver_req)
        return response.response.message

    #
    # RPC for data transmission
    #

    def send(self, peer_id, msg_type, data):
        req = rpc_pb2.SendRequest(
            peerID=peer_id,
            topic=UNKNOWN_TOPIC,
            msgType=msg_type,
            data=data,
        )
        response = self.stub.Send(req)
        throw_if_not_success(response, req)
        return response.data

    def broadcast(self, topic, msg_type, data):
        req = rpc_pb2.SendRequest(
            peerID=UNKNOWN_PID,
            topic=topic,
            msgType=msg_type,
            data=data,
        )
        response = self.stub.Send(req)
        throw_if_not_success(response, req)
        return response.data


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


stub = make_grpc_stub()
rpc_client = P2PRPCClient(stub)
# print(rpc_client.get_subscribed_shards())
# print(rpc_client.subscribe_shards([40, 56]))  # RPC should fail when subscribing an invalid shard
# print(rpc_client.get_subscribed_shards())
# print(rpc_client.unsubscribe_shards([40]))
# print(rpc_client.get_subscribed_shards())
# print(rpc_client.broadcast_collation(56, 10, 5566, 100))
# print(rpc_client.send_collation(56, 1, b'123'))
# res = rpc_client.send("", make_collation_topic(56), 0, b"")
# print(res)

peer_id_0 = "QmS5QmciTXXnCUCyxud5eWFenUMAmvAWSDa1c7dvdXRMZ7"
peer_id_1 = "QmexAnfpHrhMmAC5UNQVS8iBuUUgDrMbMY17Cck2gKrqeX"

p2p_client = P2PClient(rpc_client)
collation = Collation(1, 2, b"\xbe\xef")
print(p2p_client.broadcast_collation(collation))
print(p2p_client.request_collation(peer_id_1, 1, 2, ""))
# print(ch.stop_server())
