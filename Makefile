shardingp2p_rpc_pb = github.com/ethresearch/sharding-p2p-poc/pb/rpc
shardingp2p_rpc_pb_path = ${GOPATH}/src/$(shardingp2p_rpc_pb)
rpc_proto_source = $(shardingp2p_rpc_pb_path)/rpc.proto
rpc_proto_result = rpc_pb2.py rpc_pb2_grpc.py

all: $(rpc_proto_result)

$(rpc_proto_result): $(rpc_proto_source)
	python -m grpc_tools.protoc -I$(shardingp2p_rpc_pb_path) --python_out=. --grpc_python_out=. $(rpc_proto_source)

clean:
	rm -f $(rpc_proto_result)

