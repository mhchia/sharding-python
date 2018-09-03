from concurrent import futures
import functools
import sys
import time

import grpc

import github.com.ethresearch.sharding_p2p_poc.pb.event.event_pb2 as event_pb2
import github.com.ethresearch.sharding_p2p_poc.pb.event.event_pb2_grpc as event_pb2_grpc
import github.com.ethresearch.sharding_p2p_poc.pb.message.message_pb2 as message_pb2


LISTEN_IP = "127.0.0.1"
REMOTE_IP = "127.0.0.1"
EVENT_RPC_PORT = 35566


def make_response(status):
    response = event_pb2.Response()
    if status:
        response.status = event_pb2.Response.SUCCESS
    else:
        response.status = event_pb2.Response.FAILURE
    return response


class EventServicer(event_pb2_grpc.EventServicer):

    def __init__(self):
        pass

    def NotifyCollation(self, request, context):
        validity = True
        response = make_response(True)  # Request succeeded
        notifycollation_response = event_pb2.NotifyCollationResponse(
            response=response,
            isValid=validity,
        )
        print("NotifyCollation: request={}, response={}".format(request, notifycollation_response))
        return notifycollation_response

    def GetCollation(self, request, context):
        response = make_response(True)  # Request succeeded
        collation = message_pb2.Collation(
            shardID=request.shardID,
            period=request.period,
            blobs="getcollation: shardID={}, period={}".format(
                request.shardID,
                request.period,
            ).encode(),
        )
        getcollation_response = event_pb2.GetCollationResponse(
            response=response,
            collation=collation,
            isFound=True,
        )
        print("GetCollation: request={}, response={}".format(request, getcollation_response))
        return getcollation_response


def run_event_servicer():
    # TODO: should confirm how many workers to use
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    event_pb2_grpc.add_EventServicer_to_server(
        EventServicer(),
        server,
    )
    listen_addr = '{}:{}'.format(REMOTE_IP, EVENT_RPC_PORT)
    server.add_insecure_port(listen_addr)
    server.start()
    print("Server started")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


def make_event_stub():
    dial_addr = "{}:{}".format(REMOTE_IP, EVENT_RPC_PORT)
    channel = grpc.insecure_channel(dial_addr)
    return event_pb2_grpc.EventStub(channel)


def send_notify_collation():
    """This function is used to test whether the servicer works
    """
    stub = make_event_stub()
    collation = message_pb2.Collation(
        shardID=1,
        period=42,
        blobs=b"123",
    )
    notifycollationRequqest = event_pb2.NotifyCollationRequest(
        collation=collation,
    )
    stub.NotifyCollation(notifycollationRequqest)


def send_get_collation():
    """This function is used to test whether the servicer works
    """
    stub = make_event_stub()
    getcollation_request = event_pb2.GetCollationRequest(
        shardID=1,
        period=2,
        hash="abc",
    )
    stub.GetCollation(getcollation_request)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("Wrong arguments")
    mode = sys.argv[1]
    if mode == "server":
        run_event_servicer()
    elif mode == "notifycollation":
        send_notify_collation()
    elif mode == "getcollation":
        send_get_collation()
    else:
        raise ValueError("Wrong mode: {}".format(mode))


# class EventHandler:

#     def __init__(self):
#         pass

#     def listen(self):
#         pass

#     def register(self, handler_func):
#         pass

#     def HandleNewCollation(self, msg):
#         pass

#     def HandleNewTransaction(self, msg):
#         pass
