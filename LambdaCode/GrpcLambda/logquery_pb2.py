# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: logquery.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='logquery.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0elogquery.proto\"4\n\x0fLogQueryRequest\x12\x11\n\ttimeStamp\x18\x01 \x01(\t\x12\x0e\n\x06window\x18\x02 \x01(\x05\"\'\n\x10LogQueryResponse\x12\x13\n\x0bisAvailable\x18\x01 \x01(\x08\x32\x43\n\x08LogQuery\x12\x37\n\x0e\x43heckLogWindow\x12\x10.LogQueryRequest\x1a\x11.LogQueryResponse\"\x00\x62\x06proto3'
)




_LOGQUERYREQUEST = _descriptor.Descriptor(
  name='LogQueryRequest',
  full_name='LogQueryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeStamp', full_name='LogQueryRequest.timeStamp', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='window', full_name='LogQueryRequest.window', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=70,
)


_LOGQUERYRESPONSE = _descriptor.Descriptor(
  name='LogQueryResponse',
  full_name='LogQueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='isAvailable', full_name='LogQueryResponse.isAvailable', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=111,
)

DESCRIPTOR.message_types_by_name['LogQueryRequest'] = _LOGQUERYREQUEST
DESCRIPTOR.message_types_by_name['LogQueryResponse'] = _LOGQUERYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LogQueryRequest = _reflection.GeneratedProtocolMessageType('LogQueryRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGQUERYREQUEST,
  '__module__' : 'logquery_pb2'
  # @@protoc_insertion_point(class_scope:LogQueryRequest)
  })
_sym_db.RegisterMessage(LogQueryRequest)

LogQueryResponse = _reflection.GeneratedProtocolMessageType('LogQueryResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOGQUERYRESPONSE,
  '__module__' : 'logquery_pb2'
  # @@protoc_insertion_point(class_scope:LogQueryResponse)
  })
_sym_db.RegisterMessage(LogQueryResponse)



_LOGQUERY = _descriptor.ServiceDescriptor(
  name='LogQuery',
  full_name='LogQuery',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=113,
  serialized_end=180,
  methods=[
  _descriptor.MethodDescriptor(
    name='CheckLogWindow',
    full_name='LogQuery.CheckLogWindow',
    index=0,
    containing_service=None,
    input_type=_LOGQUERYREQUEST,
    output_type=_LOGQUERYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LOGQUERY)

DESCRIPTOR.services_by_name['LogQuery'] = _LOGQUERY

# @@protoc_insertion_point(module_scope)
