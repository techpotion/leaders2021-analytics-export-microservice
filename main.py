import grpc
from concurrent import futures
import gen.pb.export_microservice_pb2 as pb2
import gen.pb.export_microservice_pb2_grpc as pb2_grpc
from protobuf_to_dict import protobuf_to_dict
from src.exporter import Exporter

class AnalyticsExportService(pb2_grpc.AnalyticsExportServiceServicer):
    def __init__(self, *args, **kwargs):
        self.__exporter = Exporter()

    def GetExport(self, request, context):
        filepath = self.__exporter.to_xlsx(protobuf_to_dict(request))
        b = self.__exporter.file_to_bytes(filepath)
        result = {
            'data': b
        }
        return pb2.Exports.GetResponse(**result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_AnalyticsExportServiceServicer_to_server(AnalyticsExportService(), server)
    server.add_insecure_port('[::]:3400')
    print('Started microservice on :3400')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()