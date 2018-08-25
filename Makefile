shardingp2p_pb_path = github.com/ethresearch/sharding-p2p-poc/pb
shardingp2p_pb_rpc_path = ${GOPATH}/src/$(shardingp2p_pb_path)/rpc
shardingp2p_pb_msg_path = ${GOPATH}/src/$(shardingp2p_pb_path)/message
rpc_proto_source = $(shardingp2p_pb_rpc_path)/rpc.proto
msg_proto_source = $(shardingp2p_pb_msg_path)/message.proto
pb_py_path = github/com/ethresearch/sharding_p2p_poc/pb
rpc_pb_py = rpc_pb2.py rpc_pb2_grpc.py
msg_pb_py = message_pb2.py
rpc_pb_py_dest = $(patsubst %,$(pb_py_path)/rpc/%, $(rpc_pb_py))
msg_pb_py_dest = $(patsubst %,$(pb_py_path)/message/%, $(msg_pb_py))

all: $(rpc_pb_py_dest) $(msg_pb_py_dest)

$(rpc_pb_py_dest) $(msg_pb_py_dest): $(rpc_proto_source) $(msg_proto_source)
	python -m grpc_tools.protoc -I${GOPATH}/src -I$(shardingp2p_pb_rpc_path) -I$(shardingp2p_pb_msg_path) --python_out=. --grpc_python_out=. $(rpc_proto_source) $(msg_proto_source)
	mv github.com/ethresearch/sharding_p2p_poc/pb/rpc/*.py github/com/ethresearch/sharding_p2p_poc/pb/rpc/
	rm -rf github.com

clean:
	rm -f $(rpc_pb_py_dest) $(msg_pb_py_dest)

