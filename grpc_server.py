from concurrent import futures
import functools
import sys
import time

import grpc

from config import (
    RPC_SERVER_LISTEN_IP,
    RPC_SERVER_PORT,
)
from constants import (
    UNKNOWN_TOPIC,
)
from message import (
    Collation,
    CollationRequest,
    MsgType,
)

import github.com.ethresearch.sharding_p2p_poc.pb.event.event_pb2 as event_pb2
import github.com.ethresearch.sharding_p2p_poc.pb.event.event_pb2_grpc as event_pb2_grpc
import github.com.ethresearch.sharding_p2p_poc.pb.message.message_pb2 as message_pb2


def make_response(status):
    response = event_pb2.Response()
    if status:
        response.status = event_pb2.Response.SUCCESS
    else:
        response.status = event_pb2.Response.FAILURE
    return response


def handle_new_collation(collation):
    return bytes(True)


def handle_collation_request(collation_request):
    c = Collation(collation_request.shard_id, collation_request.period, b"affa")
    return c.to_bytes()


type_msg_map = {
    MsgType.Collation: (Collation, handle_new_collation),
    MsgType.CollationRequest: (CollationRequest, handle_collation_request),
}


def dispatch(msg_type, data_bytes):
    if msg_type not in type_msg_map:
        return b""
    msg_cls, handler = type_msg_map[msg_type]
    deserialized_msg = msg_cls.from_bytes(data_bytes)
    return handler(deserialized_msg)


class GRPCServer(event_pb2_grpc.EventServicer):

    def Receive(self, request, context):
        response = make_response(True)  # Request succeeded
        ret_bytes = dispatch(request.msgType, request.data)
        receive_response = event_pb2.ReceiveResponse(
            response=response,
            data=ret_bytes,
        )
        print("Receive: request={}, response={}".format(request, receive_response))
        return receive_response


def run_grpc_server():
    # TODO: should confirm how many workers to use
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    event_pb2_grpc.add_EventServicer_to_server(
        GRPCServer(),
        server,
    )
    listen_addr = '{}:{}'.format(RPC_SERVER_LISTEN_IP, RPC_SERVER_PORT)
    server.add_insecure_port(listen_addr)
    server.start()
    print("Server started")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


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


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("Wrong arguments")
    mode = sys.argv[1]
    if mode == "server":
        run_event_servicer()
    elif mode == "receive":
        send_receive()
    else:
        raise ValueError("Wrong mode: {}".format(mode))
