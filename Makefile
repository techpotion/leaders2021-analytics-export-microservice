generate:
	rm -rf gen/pb/*.py
	mkdir -p gen/pb

	python -m grpc_tools.protoc \
	-I=proto/ \
	-I=${GOPATH}/src/ \
	--python_out=./gen/pb \
	--grpc_python_out=./gen/pb proto/export_microservice.proto

	sed -i -e 's/import export_microservice_pb2/import gen.pb.export_microservice_pb2/g' gen/pb/export_microservice_pb2_grpc.py