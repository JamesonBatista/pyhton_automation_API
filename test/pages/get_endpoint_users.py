import requests

from Environment.environment import Environment as base
from schemas.schema_validation import SchemaJsonValidation as schemas


class GetBody:

    def __init__(self):
        self.response = None
        self.base_url = base().BASE_PATH

    def step_endpoint(self, endpoint):
        self.response = requests.get(self.base_url + endpoint)
        assert self.response.status_code == 200, f"\nEndpoint error system {self.response.status_code}!"

    def step_validation_schema_json(self, name):
        schemas.schema_path(self.response, name)

    def step_validation_json_schema(self, address, street):
        schemas.schema_validation_array(self.response, address, street)
