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

    def step_validation_json_schema(self):
        schemas.schema_validation_array(self.response, "address", "street")

    def step_validation_schema_json(self):
        schemas.schema_path(self.response, "name")
