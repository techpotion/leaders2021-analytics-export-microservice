# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import gen.pb.export_microservice_pb2 as export__microservice__pb2


class AnalyticsExportServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetExport = channel.unary_unary(
                '/pb.AnalyticsExportService/GetExport',
                request_serializer=export__microservice__pb2.Exports.GetRequest.SerializeToString,
                response_deserializer=export__microservice__pb2.Exports.GetResponse.FromString,
                )


class AnalyticsExportServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetExport(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AnalyticsExportServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetExport': grpc.unary_unary_rpc_method_handler(
                    servicer.GetExport,
                    request_deserializer=export__microservice__pb2.Exports.GetRequest.FromString,
                    response_serializer=export__microservice__pb2.Exports.GetResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pb.AnalyticsExportService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AnalyticsExportService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetExport(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pb.AnalyticsExportService/GetExport',
            export__microservice__pb2.Exports.GetRequest.SerializeToString,
            export__microservice__pb2.Exports.GetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
