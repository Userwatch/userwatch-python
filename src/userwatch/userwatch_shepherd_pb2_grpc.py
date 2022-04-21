# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from userwatch import userwatch_public_pb2 as userwatch_dot_userwatch__public__pb2
from userwatch import userwatch_shepherd_pb2 as userwatch_dot_userwatch__shepherd__pb2


class ShepherdStub(object):
    """Server to server APIs

    Shepherd is the service by which customer servers can talk with Userwatch
    in backend integrations. While we may wrap it in libraries, customers can
    interact with it directly too. It has some similar functionality to
    Guardian, but is generally able to trust callers a bit more since requests
    come with the customer's private keys rather than ones which could be
    extracted from their publicly available, client applications.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Validate = channel.unary_unary(
                '/uwGrpc.Shepherd/Validate',
                request_serializer=userwatch_dot_userwatch__shepherd__pb2.ValidationRequest.SerializeToString,
                response_deserializer=userwatch_dot_userwatch__public__pb2.AnalysisResponse.FromString,
                )
        self.CreateChallenge = channel.unary_unary(
                '/uwGrpc.Shepherd/CreateChallenge',
                request_serializer=userwatch_dot_userwatch__shepherd__pb2.CreateChallengeRequest.SerializeToString,
                response_deserializer=userwatch_dot_userwatch__shepherd__pb2.CreateChallengeResponse.FromString,
                )
        self.VerifyChallenge = channel.unary_unary(
                '/uwGrpc.Shepherd/VerifyChallenge',
                request_serializer=userwatch_dot_userwatch__shepherd__pb2.ChallengeVerificationRequest.SerializeToString,
                response_deserializer=userwatch_dot_userwatch__shepherd__pb2.ChallengeVerificationResponse.FromString,
                )
        self.ApproveDevice = channel.unary_unary(
                '/uwGrpc.Shepherd/ApproveDevice',
                request_serializer=userwatch_dot_userwatch__shepherd__pb2.DeviceRequest.SerializeToString,
                response_deserializer=userwatch_dot_userwatch__shepherd__pb2.DeviceResponse.FromString,
                )
        self.ReportDevice = channel.unary_unary(
                '/uwGrpc.Shepherd/ReportDevice',
                request_serializer=userwatch_dot_userwatch__shepherd__pb2.DeviceRequest.SerializeToString,
                response_deserializer=userwatch_dot_userwatch__shepherd__pb2.DeviceResponse.FromString,
                )
        self.GetDeviceList = channel.unary_unary(
                '/uwGrpc.Shepherd/GetDeviceList',
                request_serializer=userwatch_dot_userwatch__shepherd__pb2.DeviceListRequest.SerializeToString,
                response_deserializer=userwatch_dot_userwatch__shepherd__pb2.DeviceListResponse.FromString,
                )
        self.ValidateLastRequest = channel.unary_unary(
                '/uwGrpc.Shepherd/ValidateLastRequest',
                request_serializer=userwatch_dot_userwatch__shepherd__pb2.ValidateLastRequestRequest.SerializeToString,
                response_deserializer=userwatch_dot_userwatch__shepherd__pb2.ValidateLastRequestResponse.FromString,
                )


class ShepherdServicer(object):
    """Server to server APIs

    Shepherd is the service by which customer servers can talk with Userwatch
    in backend integrations. While we may wrap it in libraries, customers can
    interact with it directly too. It has some similar functionality to
    Guardian, but is generally able to trust callers a bit more since requests
    come with the customer's private keys rather than ones which could be
    extracted from their publicly available, client applications.
    """

    def Validate(self, request, context):
        """Requests and Validation
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateChallenge(self, request, context):
        """Verifying Challenge Responses
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VerifyChallenge(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ApproveDevice(self, request, context):
        """User Management
        rpc ListUsers() returns () {};
        rpc GetUser() returns () {};
        rpc AddFlag () returns () {};
        rpc RemoveFlag () returns () {};
        rpc IgnoreFlag () returns () {};
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReportDevice(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDeviceList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ValidateLastRequest(self, request, context):
        """Device Management
        rpc GetDevice() returns () {};
        rpc ListReportedDevices returns () {};

        rpc TestWebHook () returns () {};

        Context specific API calls (eg. Firebase)
        This could be made more generic eg. Fetch matching request?
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ShepherdServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Validate': grpc.unary_unary_rpc_method_handler(
                    servicer.Validate,
                    request_deserializer=userwatch_dot_userwatch__shepherd__pb2.ValidationRequest.FromString,
                    response_serializer=userwatch_dot_userwatch__public__pb2.AnalysisResponse.SerializeToString,
            ),
            'CreateChallenge': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateChallenge,
                    request_deserializer=userwatch_dot_userwatch__shepherd__pb2.CreateChallengeRequest.FromString,
                    response_serializer=userwatch_dot_userwatch__shepherd__pb2.CreateChallengeResponse.SerializeToString,
            ),
            'VerifyChallenge': grpc.unary_unary_rpc_method_handler(
                    servicer.VerifyChallenge,
                    request_deserializer=userwatch_dot_userwatch__shepherd__pb2.ChallengeVerificationRequest.FromString,
                    response_serializer=userwatch_dot_userwatch__shepherd__pb2.ChallengeVerificationResponse.SerializeToString,
            ),
            'ApproveDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.ApproveDevice,
                    request_deserializer=userwatch_dot_userwatch__shepherd__pb2.DeviceRequest.FromString,
                    response_serializer=userwatch_dot_userwatch__shepherd__pb2.DeviceResponse.SerializeToString,
            ),
            'ReportDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.ReportDevice,
                    request_deserializer=userwatch_dot_userwatch__shepherd__pb2.DeviceRequest.FromString,
                    response_serializer=userwatch_dot_userwatch__shepherd__pb2.DeviceResponse.SerializeToString,
            ),
            'GetDeviceList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDeviceList,
                    request_deserializer=userwatch_dot_userwatch__shepherd__pb2.DeviceListRequest.FromString,
                    response_serializer=userwatch_dot_userwatch__shepherd__pb2.DeviceListResponse.SerializeToString,
            ),
            'ValidateLastRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.ValidateLastRequest,
                    request_deserializer=userwatch_dot_userwatch__shepherd__pb2.ValidateLastRequestRequest.FromString,
                    response_serializer=userwatch_dot_userwatch__shepherd__pb2.ValidateLastRequestResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'uwGrpc.Shepherd', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Shepherd(object):
    """Server to server APIs

    Shepherd is the service by which customer servers can talk with Userwatch
    in backend integrations. While we may wrap it in libraries, customers can
    interact with it directly too. It has some similar functionality to
    Guardian, but is generally able to trust callers a bit more since requests
    come with the customer's private keys rather than ones which could be
    extracted from their publicly available, client applications.
    """

    @staticmethod
    def Validate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/uwGrpc.Shepherd/Validate',
            userwatch_dot_userwatch__shepherd__pb2.ValidationRequest.SerializeToString,
            userwatch_dot_userwatch__public__pb2.AnalysisResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateChallenge(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/uwGrpc.Shepherd/CreateChallenge',
            userwatch_dot_userwatch__shepherd__pb2.CreateChallengeRequest.SerializeToString,
            userwatch_dot_userwatch__shepherd__pb2.CreateChallengeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VerifyChallenge(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/uwGrpc.Shepherd/VerifyChallenge',
            userwatch_dot_userwatch__shepherd__pb2.ChallengeVerificationRequest.SerializeToString,
            userwatch_dot_userwatch__shepherd__pb2.ChallengeVerificationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ApproveDevice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/uwGrpc.Shepherd/ApproveDevice',
            userwatch_dot_userwatch__shepherd__pb2.DeviceRequest.SerializeToString,
            userwatch_dot_userwatch__shepherd__pb2.DeviceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReportDevice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/uwGrpc.Shepherd/ReportDevice',
            userwatch_dot_userwatch__shepherd__pb2.DeviceRequest.SerializeToString,
            userwatch_dot_userwatch__shepherd__pb2.DeviceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDeviceList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/uwGrpc.Shepherd/GetDeviceList',
            userwatch_dot_userwatch__shepherd__pb2.DeviceListRequest.SerializeToString,
            userwatch_dot_userwatch__shepherd__pb2.DeviceListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ValidateLastRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/uwGrpc.Shepherd/ValidateLastRequest',
            userwatch_dot_userwatch__shepherd__pb2.ValidateLastRequestRequest.SerializeToString,
            userwatch_dot_userwatch__shepherd__pb2.ValidateLastRequestResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
