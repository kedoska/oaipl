import json
import quart
import quart_cors
from quart import request

from domain.services import SoftwareService, ClientService, PermissionService


class OnboardingAPI:
    def __init__(self, port, software_repo, client_repo, permission_repo):
        self.app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")
        self.port = port

        self.software_service = SoftwareService(software_repo)
        self.client_service = ClientService(client_repo)
        self.permission_service = PermissionService(permission_repo)
        self.register_routes()

    def register_routes(self):
        @self.app.route('/software', methods=['GET'])
        async def get_all_software():
            return json.dumps([software.__dict__ for software in self.software_service.get_all_software()])

        @self.app.route('/software/<id>', methods=['GET'])
        async def get_software_by_id(id):
            return json.dumps(self.software_service.get_software_by_id(id).__dict__)

        @self.app.route('/client', methods=['GET'])
        async def get_all_clients():
            return json.dumps([client.__dict__ for client in self.client_service.get_all_clients()])

        @self.app.route('/client/<id>', methods=['GET'])
        async def get_client_by_id(id):
            return json.dumps(self.client_service.get_client_by_id(id).__dict__)

        @self.app.route('/permission', methods=['GET'])
        async def get_all_permissions():
            return json.dumps([permission.__dict__ for permission in self.permission_service.get_all_permissions()])

        @self.app.route('/permission/<id>', methods=['GET'])
        async def get_permission_by_id(id):
            return json.dumps(self.permission_service.get_permission_by_id(id).__dict__)

        @self.app.get("/logo.png")
        async def plugin_logo():
            filename = 'logo.png'
            return await quart.send_file(filename, mimetype='image/png')

        @self.app.get("/.well-known/ai-plugin.json")
        async def plugin_manifest():
            host = request.headers['Host']
            with open("./.well-known/ai-plugin.json") as f:
                text = f.read()
                return quart.Response(text, mimetype="text/json")

        @self.app.get("/openapi.yaml")
        async def openapi_spec():
            host = request.headers['Host']
            with open("openapi.yaml") as f:
                text = f.read()
                return quart.Response(text, mimetype="text/yaml")

    def run(self):
        self.app.run(debug=True, host="0.0.0.0", port=self.port)
