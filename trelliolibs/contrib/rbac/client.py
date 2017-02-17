from trellio.services import TCPServiceClient, request


class RBACTCPClient(TCPServiceClient):
    def __init__(self, *args, **kwargs):
        super(RBACTCPClient, self).__init__("rbac_service", 1)


    @request
    def create_resource_action(self, resource_id, action_name, action_value):
        return locals()

    @request
    def create_service_resources(self, service_name, service_version, http_resources):
        return locals()