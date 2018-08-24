# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rpc.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='rpc.proto',
  package='proto.rpc',
  syntax='proto3',
  serialized_pb=_b('\n\trpc.proto\x12\tproto.rpc\"k\n\x08Response\x12*\n\x06status\x18\x01 \x01(\x0e\x32\x1a.proto.rpc.Response.Status\x12\x0f\n\x07message\x18\x02 \x01(\t\"\"\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\x0b\n\x07\x46\x41ILURE\x10\x01\";\n\x11RPCAddPeerRequest\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x03\x12\x0c\n\x04seed\x18\x03 \x01(\x03\",\n\x18RPCSubscribeShardRequest\x12\x10\n\x08shardIDs\x18\x01 \x03(\x03\".\n\x1aRPCUnsubscribeShardRequest\x12\x10\n\x08shardIDs\x18\x01 \x03(\x03\"\x1e\n\x1cRPCGetSubscribedShardRequest\"X\n\x1dRPCGetSubscribedShardResponse\x12%\n\x08response\x18\x01 \x01(\x0b\x32\x13.proto.rpc.Response\x12\x10\n\x08shardIDs\x18\x02 \x03(\x03\"]\n\x1cRPCBroadcastCollationRequest\x12\x0f\n\x07shardID\x18\x01 \x01(\x03\x12\x0e\n\x06number\x18\x02 \x01(\x03\x12\x0c\n\x04size\x18\x03 \x01(\x03\x12\x0e\n\x06period\x18\x04 \x01(\x03\"=\n\x1aRPCRequestCollationRequest\x12\x0f\n\x07shardID\x18\x01 \x01(\x03\x12\x0e\n\x06period\x18\x04 \x01(\x03\"\x16\n\x14RPCStopServerRequest\"9\n\x10RPCPlainResponse\x12%\n\x08response\x18\x01 \x01(\x0b\x32\x13.proto.rpc.Response2\x94\x04\n\x03Poc\x12\x46\n\x07\x41\x64\x64Peer\x12\x1c.proto.rpc.RPCAddPeerRequest\x1a\x1b.proto.rpc.RPCPlainResponse\"\x00\x12T\n\x0eSubscribeShard\x12#.proto.rpc.RPCSubscribeShardRequest\x1a\x1b.proto.rpc.RPCPlainResponse\"\x00\x12X\n\x10UnsubscribeShard\x12%.proto.rpc.RPCUnsubscribeShardRequest\x1a\x1b.proto.rpc.RPCPlainResponse\"\x00\x12i\n\x12GetSubscribedShard\x12\'.proto.rpc.RPCGetSubscribedShardRequest\x1a(.proto.rpc.RPCGetSubscribedShardResponse\"\x00\x12\\\n\x12\x42roadcastCollation\x12\'.proto.rpc.RPCBroadcastCollationRequest\x1a\x1b.proto.rpc.RPCPlainResponse\"\x00\x12L\n\nStopServer\x12\x1f.proto.rpc.RPCStopServerRequest\x1a\x1b.proto.rpc.RPCPlainResponse\"\x00\x62\x06proto3')
)



_RESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='proto.rpc.Response.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=97,
  serialized_end=131,
)
_sym_db.RegisterEnumDescriptor(_RESPONSE_STATUS)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='proto.rpc.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='proto.rpc.Response.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='proto.rpc.Response.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RESPONSE_STATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=131,
)


_RPCADDPEERREQUEST = _descriptor.Descriptor(
  name='RPCAddPeerRequest',
  full_name='proto.rpc.RPCAddPeerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='proto.rpc.RPCAddPeerRequest.ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='proto.rpc.RPCAddPeerRequest.port', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seed', full_name='proto.rpc.RPCAddPeerRequest.seed', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=133,
  serialized_end=192,
)


_RPCSUBSCRIBESHARDREQUEST = _descriptor.Descriptor(
  name='RPCSubscribeShardRequest',
  full_name='proto.rpc.RPCSubscribeShardRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shardIDs', full_name='proto.rpc.RPCSubscribeShardRequest.shardIDs', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=194,
  serialized_end=238,
)


_RPCUNSUBSCRIBESHARDREQUEST = _descriptor.Descriptor(
  name='RPCUnsubscribeShardRequest',
  full_name='proto.rpc.RPCUnsubscribeShardRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shardIDs', full_name='proto.rpc.RPCUnsubscribeShardRequest.shardIDs', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=240,
  serialized_end=286,
)


_RPCGETSUBSCRIBEDSHARDREQUEST = _descriptor.Descriptor(
  name='RPCGetSubscribedShardRequest',
  full_name='proto.rpc.RPCGetSubscribedShardRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=288,
  serialized_end=318,
)


_RPCGETSUBSCRIBEDSHARDRESPONSE = _descriptor.Descriptor(
  name='RPCGetSubscribedShardResponse',
  full_name='proto.rpc.RPCGetSubscribedShardResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='proto.rpc.RPCGetSubscribedShardResponse.response', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shardIDs', full_name='proto.rpc.RPCGetSubscribedShardResponse.shardIDs', index=1,
      number=2, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=320,
  serialized_end=408,
)


_RPCBROADCASTCOLLATIONREQUEST = _descriptor.Descriptor(
  name='RPCBroadcastCollationRequest',
  full_name='proto.rpc.RPCBroadcastCollationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shardID', full_name='proto.rpc.RPCBroadcastCollationRequest.shardID', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='number', full_name='proto.rpc.RPCBroadcastCollationRequest.number', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='proto.rpc.RPCBroadcastCollationRequest.size', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='period', full_name='proto.rpc.RPCBroadcastCollationRequest.period', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=410,
  serialized_end=503,
)


_RPCREQUESTCOLLATIONREQUEST = _descriptor.Descriptor(
  name='RPCRequestCollationRequest',
  full_name='proto.rpc.RPCRequestCollationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shardID', full_name='proto.rpc.RPCRequestCollationRequest.shardID', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='period', full_name='proto.rpc.RPCRequestCollationRequest.period', index=1,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=505,
  serialized_end=566,
)


_RPCSTOPSERVERREQUEST = _descriptor.Descriptor(
  name='RPCStopServerRequest',
  full_name='proto.rpc.RPCStopServerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=568,
  serialized_end=590,
)


_RPCPLAINRESPONSE = _descriptor.Descriptor(
  name='RPCPlainResponse',
  full_name='proto.rpc.RPCPlainResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='proto.rpc.RPCPlainResponse.response', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=592,
  serialized_end=649,
)

_RESPONSE.fields_by_name['status'].enum_type = _RESPONSE_STATUS
_RESPONSE_STATUS.containing_type = _RESPONSE
_RPCGETSUBSCRIBEDSHARDRESPONSE.fields_by_name['response'].message_type = _RESPONSE
_RPCPLAINRESPONSE.fields_by_name['response'].message_type = _RESPONSE
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['RPCAddPeerRequest'] = _RPCADDPEERREQUEST
DESCRIPTOR.message_types_by_name['RPCSubscribeShardRequest'] = _RPCSUBSCRIBESHARDREQUEST
DESCRIPTOR.message_types_by_name['RPCUnsubscribeShardRequest'] = _RPCUNSUBSCRIBESHARDREQUEST
DESCRIPTOR.message_types_by_name['RPCGetSubscribedShardRequest'] = _RPCGETSUBSCRIBEDSHARDREQUEST
DESCRIPTOR.message_types_by_name['RPCGetSubscribedShardResponse'] = _RPCGETSUBSCRIBEDSHARDRESPONSE
DESCRIPTOR.message_types_by_name['RPCBroadcastCollationRequest'] = _RPCBROADCASTCOLLATIONREQUEST
DESCRIPTOR.message_types_by_name['RPCRequestCollationRequest'] = _RPCREQUESTCOLLATIONREQUEST
DESCRIPTOR.message_types_by_name['RPCStopServerRequest'] = _RPCSTOPSERVERREQUEST
DESCRIPTOR.message_types_by_name['RPCPlainResponse'] = _RPCPLAINRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:proto.rpc.Response)
  ))
_sym_db.RegisterMessage(Response)

RPCAddPeerRequest = _reflection.GeneratedProtocolMessageType('RPCAddPeerRequest', (_message.Message,), dict(
  DESCRIPTOR = _RPCADDPEERREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:proto.rpc.RPCAddPeerRequest)
  ))
_sym_db.RegisterMessage(RPCAddPeerRequest)

RPCSubscribeShardRequest = _reflection.GeneratedProtocolMessageType('RPCSubscribeShardRequest', (_message.Message,), dict(
  DESCRIPTOR = _RPCSUBSCRIBESHARDREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:proto.rpc.RPCSubscribeShardRequest)
  ))
_sym_db.RegisterMessage(RPCSubscribeShardRequest)

RPCUnsubscribeShardRequest = _reflection.GeneratedProtocolMessageType('RPCUnsubscribeShardRequest', (_message.Message,), dict(
  DESCRIPTOR = _RPCUNSUBSCRIBESHARDREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:proto.rpc.RPCUnsubscribeShardRequest)
  ))
_sym_db.RegisterMessage(RPCUnsubscribeShardRequest)

RPCGetSubscribedShardRequest = _reflection.GeneratedProtocolMessageType('RPCGetSubscribedShardRequest', (_message.Message,), dict(
  DESCRIPTOR = _RPCGETSUBSCRIBEDSHARDREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:proto.rpc.RPCGetSubscribedShardRequest)
  ))
_sym_db.RegisterMessage(RPCGetSubscribedShardRequest)

RPCGetSubscribedShardResponse = _reflection.GeneratedProtocolMessageType('RPCGetSubscribedShardResponse', (_message.Message,), dict(
  DESCRIPTOR = _RPCGETSUBSCRIBEDSHARDRESPONSE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:proto.rpc.RPCGetSubscribedShardResponse)
  ))
_sym_db.RegisterMessage(RPCGetSubscribedShardResponse)

RPCBroadcastCollationRequest = _reflection.GeneratedProtocolMessageType('RPCBroadcastCollationRequest', (_message.Message,), dict(
  DESCRIPTOR = _RPCBROADCASTCOLLATIONREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:proto.rpc.RPCBroadcastCollationRequest)
  ))
_sym_db.RegisterMessage(RPCBroadcastCollationRequest)

RPCRequestCollationRequest = _reflection.GeneratedProtocolMessageType('RPCRequestCollationRequest', (_message.Message,), dict(
  DESCRIPTOR = _RPCREQUESTCOLLATIONREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:proto.rpc.RPCRequestCollationRequest)
  ))
_sym_db.RegisterMessage(RPCRequestCollationRequest)

RPCStopServerRequest = _reflection.GeneratedProtocolMessageType('RPCStopServerRequest', (_message.Message,), dict(
  DESCRIPTOR = _RPCSTOPSERVERREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:proto.rpc.RPCStopServerRequest)
  ))
_sym_db.RegisterMessage(RPCStopServerRequest)

RPCPlainResponse = _reflection.GeneratedProtocolMessageType('RPCPlainResponse', (_message.Message,), dict(
  DESCRIPTOR = _RPCPLAINRESPONSE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:proto.rpc.RPCPlainResponse)
  ))
_sym_db.RegisterMessage(RPCPlainResponse)



_POC = _descriptor.ServiceDescriptor(
  name='Poc',
  full_name='proto.rpc.Poc',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=652,
  serialized_end=1184,
  methods=[
  _descriptor.MethodDescriptor(
    name='AddPeer',
    full_name='proto.rpc.Poc.AddPeer',
    index=0,
    containing_service=None,
    input_type=_RPCADDPEERREQUEST,
    output_type=_RPCPLAINRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SubscribeShard',
    full_name='proto.rpc.Poc.SubscribeShard',
    index=1,
    containing_service=None,
    input_type=_RPCSUBSCRIBESHARDREQUEST,
    output_type=_RPCPLAINRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UnsubscribeShard',
    full_name='proto.rpc.Poc.UnsubscribeShard',
    index=2,
    containing_service=None,
    input_type=_RPCUNSUBSCRIBESHARDREQUEST,
    output_type=_RPCPLAINRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetSubscribedShard',
    full_name='proto.rpc.Poc.GetSubscribedShard',
    index=3,
    containing_service=None,
    input_type=_RPCGETSUBSCRIBEDSHARDREQUEST,
    output_type=_RPCGETSUBSCRIBEDSHARDRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='BroadcastCollation',
    full_name='proto.rpc.Poc.BroadcastCollation',
    index=4,
    containing_service=None,
    input_type=_RPCBROADCASTCOLLATIONREQUEST,
    output_type=_RPCPLAINRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StopServer',
    full_name='proto.rpc.Poc.StopServer',
    index=5,
    containing_service=None,
    input_type=_RPCSTOPSERVERREQUEST,
    output_type=_RPCPLAINRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_POC)

DESCRIPTOR.services_by_name['Poc'] = _POC

# @@protoc_insertion_point(module_scope)
