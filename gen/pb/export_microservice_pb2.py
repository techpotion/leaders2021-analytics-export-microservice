# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: export_microservice.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='export_microservice.proto',
  package='pb',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19\x65xport_microservice.proto\x12\x02pb\"H\n\x07\x45xports\x1a\x1d\n\nGetRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\x1a\x1e\n\x0bGetResponse\x12\x0f\n\x07message\x18\x02 \x01(\t2W\n\x17\x41nalyticsExportService1\x12<\n\x07GetMark\x12\x16.pb.Exports.GetRequest\x1a\x17.pb.Exports.GetResponse\"\x00\x62\x06proto3'
)




_EXPORTS_GETREQUEST = _descriptor.Descriptor(
  name='GetRequest',
  full_name='pb.Exports.GetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='pb.Exports.GetRequest.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=44,
  serialized_end=73,
)

_EXPORTS_GETRESPONSE = _descriptor.Descriptor(
  name='GetResponse',
  full_name='pb.Exports.GetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='pb.Exports.GetResponse.message', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=75,
  serialized_end=105,
)

_EXPORTS = _descriptor.Descriptor(
  name='Exports',
  full_name='pb.Exports',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_EXPORTS_GETREQUEST, _EXPORTS_GETRESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=105,
)

_EXPORTS_GETREQUEST.containing_type = _EXPORTS
_EXPORTS_GETRESPONSE.containing_type = _EXPORTS
DESCRIPTOR.message_types_by_name['Exports'] = _EXPORTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Exports = _reflection.GeneratedProtocolMessageType('Exports', (_message.Message,), {

  'GetRequest' : _reflection.GeneratedProtocolMessageType('GetRequest', (_message.Message,), {
    'DESCRIPTOR' : _EXPORTS_GETREQUEST,
    '__module__' : 'export_microservice_pb2'
    # @@protoc_insertion_point(class_scope:pb.Exports.GetRequest)
    })
  ,

  'GetResponse' : _reflection.GeneratedProtocolMessageType('GetResponse', (_message.Message,), {
    'DESCRIPTOR' : _EXPORTS_GETRESPONSE,
    '__module__' : 'export_microservice_pb2'
    # @@protoc_insertion_point(class_scope:pb.Exports.GetResponse)
    })
  ,
  'DESCRIPTOR' : _EXPORTS,
  '__module__' : 'export_microservice_pb2'
  # @@protoc_insertion_point(class_scope:pb.Exports)
  })
_sym_db.RegisterMessage(Exports)
_sym_db.RegisterMessage(Exports.GetRequest)
_sym_db.RegisterMessage(Exports.GetResponse)



_ANALYTICSEXPORTSERVICE1 = _descriptor.ServiceDescriptor(
  name='AnalyticsExportService1',
  full_name='pb.AnalyticsExportService1',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=107,
  serialized_end=194,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetMark',
    full_name='pb.AnalyticsExportService1.GetMark',
    index=0,
    containing_service=None,
    input_type=_EXPORTS_GETREQUEST,
    output_type=_EXPORTS_GETRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ANALYTICSEXPORTSERVICE1)

DESCRIPTOR.services_by_name['AnalyticsExportService1'] = _ANALYTICSEXPORTSERVICE1

# @@protoc_insertion_point(module_scope)
