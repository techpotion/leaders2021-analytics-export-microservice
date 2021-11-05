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
  serialized_pb=b'\n\x19\x65xport_microservice.proto\x12\x02pb\"\xb6\x02\n\x07\x45xports\x1a\x8d\x02\n\nGetRequest\x12\x35\n\x0e\x62\x61sicAnalytics\x18\x01 \x01(\x0b\x32\x1d.pb.PolygonAnalytics.Response\x12\x38\n\rparkAnalytics\x18\x02 \x01(\x0b\x32!.pb.PolygonParkAnalytics.Response\x12\x42\n\x12pollutionAnalytics\x18\x03 \x01(\x0b\x32&.pb.PolygonPollutionAnalytics.Response\x12<\n\x0fsubwayAnalytics\x18\x04 \x01(\x0b\x32#.pb.PolygonSubwayAnalytics.Response\x12\x0c\n\x04mark\x18\x05 \x01(\x02\x1a\x1b\n\x0bGetResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"\xc7\x02\n\x10PolygonAnalytics\x1a\xb2\x02\n\x08Response\x12\x13\n\x0b\x61reasSquare\x18\x01 \x01(\x01\x12\x1a\n\x12\x61reasSquarePer100k\x18\x02 \x01(\x01\x12\x13\n\x0b\x61reasAmount\x18\x03 \x01(\r\x12\x1a\n\x12\x61reasAmountPer100k\x18\x04 \x01(\x01\x12\x14\n\x0csportsAmount\x18\x05 \x01(\r\x12\x1b\n\x13sportsAmountPer100k\x18\x06 \x01(\x01\x12\x13\n\x0bsportsKinds\x18\x07 \x03(\t\x12\x11\n\tareaTypes\x18\x08 \x03(\t\x12\x17\n\x0f\x61reaTypesAmount\x18\t \x01(\r\x12\x1b\n\x13sportsObjectsAmount\x18\n \x01(\r\x12\"\n\x1asportsObjectsAmountPer100k\x18\x0b \x01(\x01\x12\x0f\n\x07\x64\x65nsity\x18\x0c \x01(\x01\"]\n\x14PolygonParkAnalytics\x1a\x45\n\x08Response\x12\x17\n\x05parks\x18\x01 \x03(\x0b\x32\x08.pb.Park\x12 \n\tlistStats\x18\x02 \x01(\x0b\x32\r.pb.ListStats\"\x85\x01\n\x19PolygonPollutionAnalytics\x1ah\n\x08Response\x12\x1d\n\x06points\x18\x01 \x03(\x0b\x32\r.pb.Pollution\x12\x1b\n\x13pollutionPercentage\x18\x02 \x01(\x02\x12 \n\tlistStats\x18\x03 \x01(\x0b\x32\r.pb.ListStats\"b\n\x16PolygonSubwayAnalytics\x1aH\n\x08Response\x12\x1a\n\x06points\x18\x01 \x03(\x0b\x32\n.pb.Subway\x12 \n\tlistStats\x18\x02 \x01(\x0b\x32\r.pb.ListStats\"`\n\x06Subway\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tlineColor\x18\x02 \x01(\t\x12\x18\n\x05point\x18\x03 \x01(\x0b\x32\t.pb.Point\x12\x1b\n\x13\x64istanceFromPolygon\x18\x04 \x01(\x01\"\x1a\n\tListStats\x12\r\n\x05\x63ount\x18\x01 \x01(\r\"\x97\x01\n\x04Park\x12\x12\n\ncommonName\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64mArea\x18\x02 \x01(\t\x12\x10\n\x08\x64istrict\x18\x03 \x01(\t\x12\x10\n\x08location\x18\x04 \x01(\t\x12\x16\n\x0ehasSportground\x18\x05 \x01(\x08\x12\x1e\n\x0bobjectPoint\x18\x06 \x01(\x0b\x32\t.pb.Point\x12\x0e\n\x06square\x18\x07 \x01(\x01\"\x85\x01\n\tPollution\x12\x0f\n\x07\x61\x64mArea\x18\x01 \x01(\t\x12\x10\n\x08\x64istrict\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x12\n\nisPolluted\x18\x04 \x01(\x08\x12\x1e\n\x0bobjectPoint\x18\x05 \x01(\x0b\x32\t.pb.Point\x12\x0f\n\x07results\x18\x06 \x01(\t\"!\n\x05Point\x12\x0b\n\x03lat\x18\x01 \x01(\x02\x12\x0b\n\x03lng\x18\x02 \x01(\x02\x32X\n\x16\x41nalyticsExportService\x12>\n\tGetExport\x12\x16.pb.Exports.GetRequest\x1a\x17.pb.Exports.GetResponse\"\x00\x62\x06proto3'
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
      name='basicAnalytics', full_name='pb.Exports.GetRequest.basicAnalytics', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parkAnalytics', full_name='pb.Exports.GetRequest.parkAnalytics', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pollutionAnalytics', full_name='pb.Exports.GetRequest.pollutionAnalytics', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subwayAnalytics', full_name='pb.Exports.GetRequest.subwayAnalytics', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mark', full_name='pb.Exports.GetRequest.mark', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=46,
  serialized_end=315,
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
      name='data', full_name='pb.Exports.GetResponse.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=317,
  serialized_end=344,
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
  serialized_start=34,
  serialized_end=344,
)


_POLYGONANALYTICS_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='pb.PolygonAnalytics.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='areasSquare', full_name='pb.PolygonAnalytics.Response.areasSquare', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='areasSquarePer100k', full_name='pb.PolygonAnalytics.Response.areasSquarePer100k', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='areasAmount', full_name='pb.PolygonAnalytics.Response.areasAmount', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='areasAmountPer100k', full_name='pb.PolygonAnalytics.Response.areasAmountPer100k', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sportsAmount', full_name='pb.PolygonAnalytics.Response.sportsAmount', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sportsAmountPer100k', full_name='pb.PolygonAnalytics.Response.sportsAmountPer100k', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sportsKinds', full_name='pb.PolygonAnalytics.Response.sportsKinds', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='areaTypes', full_name='pb.PolygonAnalytics.Response.areaTypes', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='areaTypesAmount', full_name='pb.PolygonAnalytics.Response.areaTypesAmount', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sportsObjectsAmount', full_name='pb.PolygonAnalytics.Response.sportsObjectsAmount', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sportsObjectsAmountPer100k', full_name='pb.PolygonAnalytics.Response.sportsObjectsAmountPer100k', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='density', full_name='pb.PolygonAnalytics.Response.density', index=11,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=368,
  serialized_end=674,
)

_POLYGONANALYTICS = _descriptor.Descriptor(
  name='PolygonAnalytics',
  full_name='pb.PolygonAnalytics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_POLYGONANALYTICS_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=347,
  serialized_end=674,
)


_POLYGONPARKANALYTICS_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='pb.PolygonParkAnalytics.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parks', full_name='pb.PolygonParkAnalytics.Response.parks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='listStats', full_name='pb.PolygonParkAnalytics.Response.listStats', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=700,
  serialized_end=769,
)

_POLYGONPARKANALYTICS = _descriptor.Descriptor(
  name='PolygonParkAnalytics',
  full_name='pb.PolygonParkAnalytics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_POLYGONPARKANALYTICS_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=676,
  serialized_end=769,
)


_POLYGONPOLLUTIONANALYTICS_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='pb.PolygonPollutionAnalytics.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='points', full_name='pb.PolygonPollutionAnalytics.Response.points', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pollutionPercentage', full_name='pb.PolygonPollutionAnalytics.Response.pollutionPercentage', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='listStats', full_name='pb.PolygonPollutionAnalytics.Response.listStats', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=801,
  serialized_end=905,
)

_POLYGONPOLLUTIONANALYTICS = _descriptor.Descriptor(
  name='PolygonPollutionAnalytics',
  full_name='pb.PolygonPollutionAnalytics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_POLYGONPOLLUTIONANALYTICS_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=772,
  serialized_end=905,
)


_POLYGONSUBWAYANALYTICS_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='pb.PolygonSubwayAnalytics.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='points', full_name='pb.PolygonSubwayAnalytics.Response.points', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='listStats', full_name='pb.PolygonSubwayAnalytics.Response.listStats', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=933,
  serialized_end=1005,
)

_POLYGONSUBWAYANALYTICS = _descriptor.Descriptor(
  name='PolygonSubwayAnalytics',
  full_name='pb.PolygonSubwayAnalytics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_POLYGONSUBWAYANALYTICS_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=907,
  serialized_end=1005,
)


_SUBWAY = _descriptor.Descriptor(
  name='Subway',
  full_name='pb.Subway',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='pb.Subway.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lineColor', full_name='pb.Subway.lineColor', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='point', full_name='pb.Subway.point', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='distanceFromPolygon', full_name='pb.Subway.distanceFromPolygon', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=1007,
  serialized_end=1103,
)


_LISTSTATS = _descriptor.Descriptor(
  name='ListStats',
  full_name='pb.ListStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='pb.ListStats.count', index=0,
      number=1, type=13, cpp_type=3, label=1,
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
  serialized_start=1105,
  serialized_end=1131,
)


_PARK = _descriptor.Descriptor(
  name='Park',
  full_name='pb.Park',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='commonName', full_name='pb.Park.commonName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='admArea', full_name='pb.Park.admArea', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='district', full_name='pb.Park.district', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='pb.Park.location', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hasSportground', full_name='pb.Park.hasSportground', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='objectPoint', full_name='pb.Park.objectPoint', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='square', full_name='pb.Park.square', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=1134,
  serialized_end=1285,
)


_POLLUTION = _descriptor.Descriptor(
  name='Pollution',
  full_name='pb.Pollution',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='admArea', full_name='pb.Pollution.admArea', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='district', full_name='pb.Pollution.district', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='pb.Pollution.location', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isPolluted', full_name='pb.Pollution.isPolluted', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='objectPoint', full_name='pb.Pollution.objectPoint', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='results', full_name='pb.Pollution.results', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=1288,
  serialized_end=1421,
)


_POINT = _descriptor.Descriptor(
  name='Point',
  full_name='pb.Point',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='lat', full_name='pb.Point.lat', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lng', full_name='pb.Point.lng', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=1423,
  serialized_end=1456,
)

_EXPORTS_GETREQUEST.fields_by_name['basicAnalytics'].message_type = _POLYGONANALYTICS_RESPONSE
_EXPORTS_GETREQUEST.fields_by_name['parkAnalytics'].message_type = _POLYGONPARKANALYTICS_RESPONSE
_EXPORTS_GETREQUEST.fields_by_name['pollutionAnalytics'].message_type = _POLYGONPOLLUTIONANALYTICS_RESPONSE
_EXPORTS_GETREQUEST.fields_by_name['subwayAnalytics'].message_type = _POLYGONSUBWAYANALYTICS_RESPONSE
_EXPORTS_GETREQUEST.containing_type = _EXPORTS
_EXPORTS_GETRESPONSE.containing_type = _EXPORTS
_POLYGONANALYTICS_RESPONSE.containing_type = _POLYGONANALYTICS
_POLYGONPARKANALYTICS_RESPONSE.fields_by_name['parks'].message_type = _PARK
_POLYGONPARKANALYTICS_RESPONSE.fields_by_name['listStats'].message_type = _LISTSTATS
_POLYGONPARKANALYTICS_RESPONSE.containing_type = _POLYGONPARKANALYTICS
_POLYGONPOLLUTIONANALYTICS_RESPONSE.fields_by_name['points'].message_type = _POLLUTION
_POLYGONPOLLUTIONANALYTICS_RESPONSE.fields_by_name['listStats'].message_type = _LISTSTATS
_POLYGONPOLLUTIONANALYTICS_RESPONSE.containing_type = _POLYGONPOLLUTIONANALYTICS
_POLYGONSUBWAYANALYTICS_RESPONSE.fields_by_name['points'].message_type = _SUBWAY
_POLYGONSUBWAYANALYTICS_RESPONSE.fields_by_name['listStats'].message_type = _LISTSTATS
_POLYGONSUBWAYANALYTICS_RESPONSE.containing_type = _POLYGONSUBWAYANALYTICS
_SUBWAY.fields_by_name['point'].message_type = _POINT
_PARK.fields_by_name['objectPoint'].message_type = _POINT
_POLLUTION.fields_by_name['objectPoint'].message_type = _POINT
DESCRIPTOR.message_types_by_name['Exports'] = _EXPORTS
DESCRIPTOR.message_types_by_name['PolygonAnalytics'] = _POLYGONANALYTICS
DESCRIPTOR.message_types_by_name['PolygonParkAnalytics'] = _POLYGONPARKANALYTICS
DESCRIPTOR.message_types_by_name['PolygonPollutionAnalytics'] = _POLYGONPOLLUTIONANALYTICS
DESCRIPTOR.message_types_by_name['PolygonSubwayAnalytics'] = _POLYGONSUBWAYANALYTICS
DESCRIPTOR.message_types_by_name['Subway'] = _SUBWAY
DESCRIPTOR.message_types_by_name['ListStats'] = _LISTSTATS
DESCRIPTOR.message_types_by_name['Park'] = _PARK
DESCRIPTOR.message_types_by_name['Pollution'] = _POLLUTION
DESCRIPTOR.message_types_by_name['Point'] = _POINT
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

PolygonAnalytics = _reflection.GeneratedProtocolMessageType('PolygonAnalytics', (_message.Message,), {

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _POLYGONANALYTICS_RESPONSE,
    '__module__' : 'export_microservice_pb2'
    # @@protoc_insertion_point(class_scope:pb.PolygonAnalytics.Response)
    })
  ,
  'DESCRIPTOR' : _POLYGONANALYTICS,
  '__module__' : 'export_microservice_pb2'
  # @@protoc_insertion_point(class_scope:pb.PolygonAnalytics)
  })
_sym_db.RegisterMessage(PolygonAnalytics)
_sym_db.RegisterMessage(PolygonAnalytics.Response)

PolygonParkAnalytics = _reflection.GeneratedProtocolMessageType('PolygonParkAnalytics', (_message.Message,), {

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _POLYGONPARKANALYTICS_RESPONSE,
    '__module__' : 'export_microservice_pb2'
    # @@protoc_insertion_point(class_scope:pb.PolygonParkAnalytics.Response)
    })
  ,
  'DESCRIPTOR' : _POLYGONPARKANALYTICS,
  '__module__' : 'export_microservice_pb2'
  # @@protoc_insertion_point(class_scope:pb.PolygonParkAnalytics)
  })
_sym_db.RegisterMessage(PolygonParkAnalytics)
_sym_db.RegisterMessage(PolygonParkAnalytics.Response)

PolygonPollutionAnalytics = _reflection.GeneratedProtocolMessageType('PolygonPollutionAnalytics', (_message.Message,), {

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _POLYGONPOLLUTIONANALYTICS_RESPONSE,
    '__module__' : 'export_microservice_pb2'
    # @@protoc_insertion_point(class_scope:pb.PolygonPollutionAnalytics.Response)
    })
  ,
  'DESCRIPTOR' : _POLYGONPOLLUTIONANALYTICS,
  '__module__' : 'export_microservice_pb2'
  # @@protoc_insertion_point(class_scope:pb.PolygonPollutionAnalytics)
  })
_sym_db.RegisterMessage(PolygonPollutionAnalytics)
_sym_db.RegisterMessage(PolygonPollutionAnalytics.Response)

PolygonSubwayAnalytics = _reflection.GeneratedProtocolMessageType('PolygonSubwayAnalytics', (_message.Message,), {

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _POLYGONSUBWAYANALYTICS_RESPONSE,
    '__module__' : 'export_microservice_pb2'
    # @@protoc_insertion_point(class_scope:pb.PolygonSubwayAnalytics.Response)
    })
  ,
  'DESCRIPTOR' : _POLYGONSUBWAYANALYTICS,
  '__module__' : 'export_microservice_pb2'
  # @@protoc_insertion_point(class_scope:pb.PolygonSubwayAnalytics)
  })
_sym_db.RegisterMessage(PolygonSubwayAnalytics)
_sym_db.RegisterMessage(PolygonSubwayAnalytics.Response)

Subway = _reflection.GeneratedProtocolMessageType('Subway', (_message.Message,), {
  'DESCRIPTOR' : _SUBWAY,
  '__module__' : 'export_microservice_pb2'
  # @@protoc_insertion_point(class_scope:pb.Subway)
  })
_sym_db.RegisterMessage(Subway)

ListStats = _reflection.GeneratedProtocolMessageType('ListStats', (_message.Message,), {
  'DESCRIPTOR' : _LISTSTATS,
  '__module__' : 'export_microservice_pb2'
  # @@protoc_insertion_point(class_scope:pb.ListStats)
  })
_sym_db.RegisterMessage(ListStats)

Park = _reflection.GeneratedProtocolMessageType('Park', (_message.Message,), {
  'DESCRIPTOR' : _PARK,
  '__module__' : 'export_microservice_pb2'
  # @@protoc_insertion_point(class_scope:pb.Park)
  })
_sym_db.RegisterMessage(Park)

Pollution = _reflection.GeneratedProtocolMessageType('Pollution', (_message.Message,), {
  'DESCRIPTOR' : _POLLUTION,
  '__module__' : 'export_microservice_pb2'
  # @@protoc_insertion_point(class_scope:pb.Pollution)
  })
_sym_db.RegisterMessage(Pollution)

Point = _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), {
  'DESCRIPTOR' : _POINT,
  '__module__' : 'export_microservice_pb2'
  # @@protoc_insertion_point(class_scope:pb.Point)
  })
_sym_db.RegisterMessage(Point)



_ANALYTICSEXPORTSERVICE = _descriptor.ServiceDescriptor(
  name='AnalyticsExportService',
  full_name='pb.AnalyticsExportService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1458,
  serialized_end=1546,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetExport',
    full_name='pb.AnalyticsExportService.GetExport',
    index=0,
    containing_service=None,
    input_type=_EXPORTS_GETREQUEST,
    output_type=_EXPORTS_GETRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ANALYTICSEXPORTSERVICE)

DESCRIPTOR.services_by_name['AnalyticsExportService'] = _ANALYTICSEXPORTSERVICE

# @@protoc_insertion_point(module_scope)
