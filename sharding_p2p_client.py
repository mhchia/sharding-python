import functools

import grpc

import github.com.ethresearch.sharding_p2p_poc.pb.message.message_pb2 as message_pb2
import github.com.ethresearch.sharding_p2p_poc.pb.rpc.rpc_pb2 as rpc_pb2
import github.com.ethresearch.sharding_p2p_poc.pb.rpc.rpc_pb2_grpc as rpc_pb2_grpc


REMOTE_IP = "127.0.0.1"
RPCPORT = 13000


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


class ShardingP2PController:
    stub = None

    def __init__(self, stub):
        self.stub = stub

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


def make_grpc_stub():
    dial_addr = "{}:{}".format(REMOTE_IP, RPCPORT)
    channel = grpc.insecure_channel(dial_addr)
    return rpc_pb2_grpc.PocStub(channel)


stub = make_grpc_stub()
# stub = MockRPCStub()
ch = ShardingP2PController(stub)
print(ch.get_subscribed_shards())
print(ch.subscribe_shards([40, 56]))  # RPC should fail when subscribing an invalid shard
print(ch.get_subscribed_shards())
print(ch.unsubscribe_shards([40]))
print(ch.get_subscribed_shards())
print(ch.broadcast_collation(40, 10, 5566, 100))
print(ch.send_collation(40, 1, b'123'))
# print(ch.stop_server())

