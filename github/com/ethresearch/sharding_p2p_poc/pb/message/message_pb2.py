# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: github.com/ethresearch/sharding-p2p-poc/pb/message/message.proto

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
  name='github.com/ethresearch/sharding-p2p-poc/pb/message/message.proto',
  package='proto.message',
  syntax='proto3',
  serialized_pb=_b('\n@github.com/ethresearch/sharding-p2p-poc/pb/message/message.proto\x12\rproto.message\"o\n\x08Response\x12.\n\x06status\x18\x01 \x01(\x0e\x32\x1e.proto.message.Response.Status\x12\x0f\n\x07message\x18\x02 \x01(\t\"\"\n\x06Status\x12\x0b\n\x07SUCCESS\x10\x00\x12\x0b\n\x07\x46\x41ILURE\x10\x01\"!\n\x0e\x41\x64\x64PeerRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"<\n\x0f\x41\x64\x64PeerResponse\x12)\n\x08response\x18\x01 \x01(\x0b\x32\x17.proto.message.Response\";\n\tCollation\x12\x0f\n\x07shardID\x18\x01 \x01(\x03\x12\x0e\n\x06period\x18\x02 \x01(\x03\x12\r\n\x05\x62lobs\x18\x03 \x01(\x0c\"A\n\x10\x43ollationRequest\x12\x0f\n\x07shardID\x18\x01 \x01(\x03\x12\x0e\n\x06period\x18\x02 \x01(\x03\x12\x0c\n\x04hash\x18\x03 \x01(\t\"k\n\x11\x43ollationResponse\x12)\n\x08response\x18\x01 \x01(\x0b\x32\x17.proto.message.Response\x12+\n\tcollation\x18\x02 \x01(\x0b\x32\x18.proto.message.Collation\"$\n\x10ShardPeerRequest\x12\x10\n\x08shardIDs\x18\x01 \x03(\x03\"\xf7\x01\n\x11ShardPeerResponse\x12)\n\x08response\x18\x01 \x01(\x0b\x32\x17.proto.message.Response\x12\x44\n\nshardPeers\x18\x02 \x03(\x0b\x32\x30.proto.message.ShardPeerResponse.ShardPeersEntry\x1a\x16\n\x05Peers\x12\r\n\x05peers\x18\x01 \x03(\t\x1aY\n\x0fShardPeersEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\x35\n\x05value\x18\x02 \x01(\x0b\x32&.proto.message.ShardPeerResponse.Peers:\x02\x38\x01\"\'\n\x13NotifyShardsRequest\x12\x10\n\x08shardIDs\x18\x01 \x03(\x03\x62\x06proto3')
)



_RESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='proto.message.Response.Status',
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
  serialized_start=160,
  serialized_end=194,
)
_sym_db.RegisterEnumDescriptor(_RESPONSE_STATUS)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='proto.message.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='proto.message.Response.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='proto.message.Response.message', index=1,
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
  serialized_start=83,
  serialized_end=194,
)


_ADDPEERREQUEST = _descriptor.Descriptor(
  name='AddPeerRequest',
  full_name='proto.message.AddPeerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='proto.message.AddPeerRequest.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=196,
  serialized_end=229,
)


_ADDPEERRESPONSE = _descriptor.Descriptor(
  name='AddPeerResponse',
  full_name='proto.message.AddPeerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='proto.message.AddPeerResponse.response', index=0,
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
  serialized_start=231,
  serialized_end=291,
)


_COLLATION = _descriptor.Descriptor(
  name='Collation',
  full_name='proto.message.Collation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shardID', full_name='proto.message.Collation.shardID', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='period', full_name='proto.message.Collation.period', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blobs', full_name='proto.message.Collation.blobs', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=293,
  serialized_end=352,
)


_COLLATIONREQUEST = _descriptor.Descriptor(
  name='CollationRequest',
  full_name='proto.message.CollationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shardID', full_name='proto.message.CollationRequest.shardID', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='period', full_name='proto.message.CollationRequest.period', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash', full_name='proto.message.CollationRequest.hash', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=354,
  serialized_end=419,
)


_COLLATIONRESPONSE = _descriptor.Descriptor(
  name='CollationResponse',
  full_name='proto.message.CollationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='proto.message.CollationResponse.response', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collation', full_name='proto.message.CollationResponse.collation', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=421,
  serialized_end=528,
)


_SHARDPEERREQUEST = _descriptor.Descriptor(
  name='ShardPeerRequest',
  full_name='proto.message.ShardPeerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shardIDs', full_name='proto.message.ShardPeerRequest.shardIDs', index=0,
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
  serialized_start=530,
  serialized_end=566,
)


_SHARDPEERRESPONSE_PEERS = _descriptor.Descriptor(
  name='Peers',
  full_name='proto.message.ShardPeerResponse.Peers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='peers', full_name='proto.message.ShardPeerResponse.Peers.peers', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=703,
  serialized_end=725,
)

_SHARDPEERRESPONSE_SHARDPEERSENTRY = _descriptor.Descriptor(
  name='ShardPeersEntry',
  full_name='proto.message.ShardPeerResponse.ShardPeersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='proto.message.ShardPeerResponse.ShardPeersEntry.key', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='proto.message.ShardPeerResponse.ShardPeersEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=727,
  serialized_end=816,
)

_SHARDPEERRESPONSE = _descriptor.Descriptor(
  name='ShardPeerResponse',
  full_name='proto.message.ShardPeerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='proto.message.ShardPeerResponse.response', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shardPeers', full_name='proto.message.ShardPeerResponse.shardPeers', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SHARDPEERRESPONSE_PEERS, _SHARDPEERRESPONSE_SHARDPEERSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=569,
  serialized_end=816,
)


_NOTIFYSHARDSREQUEST = _descriptor.Descriptor(
  name='NotifyShardsRequest',
  full_name='proto.message.NotifyShardsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shardIDs', full_name='proto.message.NotifyShardsRequest.shardIDs', index=0,
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
  serialized_start=818,
  serialized_end=857,
)

_RESPONSE.fields_by_name['status'].enum_type = _RESPONSE_STATUS
_RESPONSE_STATUS.containing_type = _RESPONSE
_ADDPEERRESPONSE.fields_by_name['response'].message_type = _RESPONSE
_COLLATIONRESPONSE.fields_by_name['response'].message_type = _RESPONSE
_COLLATIONRESPONSE.fields_by_name['collation'].message_type = _COLLATION
_SHARDPEERRESPONSE_PEERS.containing_type = _SHARDPEERRESPONSE
_SHARDPEERRESPONSE_SHARDPEERSENTRY.fields_by_name['value'].message_type = _SHARDPEERRESPONSE_PEERS
_SHARDPEERRESPONSE_SHARDPEERSENTRY.containing_type = _SHARDPEERRESPONSE
_SHARDPEERRESPONSE.fields_by_name['response'].message_type = _RESPONSE
_SHARDPEERRESPONSE.fields_by_name['shardPeers'].message_type = _SHARDPEERRESPONSE_SHARDPEERSENTRY
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['AddPeerRequest'] = _ADDPEERREQUEST
DESCRIPTOR.message_types_by_name['AddPeerResponse'] = _ADDPEERRESPONSE
DESCRIPTOR.message_types_by_name['Collation'] = _COLLATION
DESCRIPTOR.message_types_by_name['CollationRequest'] = _COLLATIONREQUEST
DESCRIPTOR.message_types_by_name['CollationResponse'] = _COLLATIONRESPONSE
DESCRIPTOR.message_types_by_name['ShardPeerRequest'] = _SHARDPEERREQUEST
DESCRIPTOR.message_types_by_name['ShardPeerResponse'] = _SHARDPEERRESPONSE
DESCRIPTOR.message_types_by_name['NotifyShardsRequest'] = _NOTIFYSHARDSREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'github.com.ethresearch.sharding_p2p_poc.pb.message.message_pb2'
  # @@protoc_insertion_point(class_scope:proto.message.Response)
  ))
_sym_db.RegisterMessage(Response)

AddPeerRequest = _reflection.GeneratedProtocolMessageType('AddPeerRequest', (_message.Message,), dict(
  DESCRIPTOR = _ADDPEERREQUEST,
  __module__ = 'github.com.ethresearch.sharding_p2p_poc.pb.message.message_pb2'
  # @@protoc_insertion_point(class_scope:proto.message.AddPeerRequest)
  ))
_sym_db.RegisterMessage(AddPeerRequest)

AddPeerResponse = _reflection.GeneratedProtocolMessageType('AddPeerResponse', (_message.Message,), dict(
  DESCRIPTOR = _ADDPEERRESPONSE,
  __module__ = 'github.com.ethresearch.sharding_p2p_poc.pb.message.message_pb2'
  # @@protoc_insertion_point(class_scope:proto.message.AddPeerResponse)
  ))
_sym_db.RegisterMessage(AddPeerResponse)

Collation = _reflection.GeneratedProtocolMessageType('Collation', (_message.Message,), dict(
  DESCRIPTOR = _COLLATION,
  __module__ = 'github.com.ethresearch.sharding_p2p_poc.pb.message.message_pb2'
  # @@protoc_insertion_point(class_scope:proto.message.Collation)
  ))
_sym_db.RegisterMessage(Collation)

CollationRequest = _reflection.GeneratedProtocolMessageType('CollationRequest', (_message.Message,), dict(
  DESCRIPTOR = _COLLATIONREQUEST,
  __module__ = 'github.com.ethresearch.sharding_p2p_poc.pb.message.message_pb2'
  # @@protoc_insertion_point(class_scope:proto.message.CollationRequest)
  ))
_sym_db.RegisterMessage(CollationRequest)

CollationResponse = _reflection.GeneratedProtocolMessageType('CollationResponse', (_message.Message,), dict(
  DESCRIPTOR = _COLLATIONRESPONSE,
  __module__ = 'github.com.ethresearch.sharding_p2p_poc.pb.message.message_pb2'
  # @@protoc_insertion_point(class_scope:proto.message.CollationResponse)
  ))
_sym_db.RegisterMessage(CollationResponse)

ShardPeerRequest = _reflection.GeneratedProtocolMessageType('ShardPeerRequest', (_message.Message,), dict(
  DESCRIPTOR = _SHARDPEERREQUEST,
  __module__ = 'github.com.ethresearch.sharding_p2p_poc.pb.message.message_pb2'
  # @@protoc_insertion_point(class_scope:proto.message.ShardPeerRequest)
  ))
_sym_db.RegisterMessage(ShardPeerRequest)

ShardPeerResponse = _reflection.GeneratedProtocolMessageType('ShardPeerResponse', (_message.Message,), dict(

  Peers = _reflection.GeneratedProtocolMessageType('Peers', (_message.Message,), dict(
    DESCRIPTOR = _SHARDPEERRESPONSE_PEERS,
    __module__ = 'github.com.ethresearch.sharding_p2p_poc.pb.message.message_pb2'
    # @@protoc_insertion_point(class_scope:proto.message.ShardPeerResponse.Peers)
    ))
  ,

  ShardPeersEntry = _reflection.GeneratedProtocolMessageType('ShardPeersEntry', (_message.Message,), dict(
    DESCRIPTOR = _SHARDPEERRESPONSE_SHARDPEERSENTRY,
    __module__ = 'github.com.ethresearch.sharding_p2p_poc.pb.message.message_pb2'
    # @@protoc_insertion_point(class_scope:proto.message.ShardPeerResponse.ShardPeersEntry)
    ))
  ,
  DESCRIPTOR = _SHARDPEERRESPONSE,
  __module__ = 'github.com.ethresearch.sharding_p2p_poc.pb.message.message_pb2'
  # @@protoc_insertion_point(class_scope:proto.message.ShardPeerResponse)
  ))
_sym_db.RegisterMessage(ShardPeerResponse)
_sym_db.RegisterMessage(ShardPeerResponse.Peers)
_sym_db.RegisterMessage(ShardPeerResponse.ShardPeersEntry)

NotifyShardsRequest = _reflection.GeneratedProtocolMessageType('NotifyShardsRequest', (_message.Message,), dict(
  DESCRIPTOR = _NOTIFYSHARDSREQUEST,
  __module__ = 'github.com.ethresearch.sharding_p2p_poc.pb.message.message_pb2'
  # @@protoc_insertion_point(class_scope:proto.message.NotifyShardsRequest)
  ))
_sym_db.RegisterMessage(NotifyShardsRequest)


_SHARDPEERRESPONSE_SHARDPEERSENTRY.has_options = True
_SHARDPEERRESPONSE_SHARDPEERSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
