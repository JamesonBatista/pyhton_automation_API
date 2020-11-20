import requests

from Environment.environment import Environment


class GetBody:

    def __init__(self):
        self.response = None
        self.pathSchema = "schemas/"
        self.base_url = Environment().BASE_PATH

    def get_endpoint(self, endpoint):
        self.response = requests.get("http://api.zippopotam.us/us/90210")
        assert self.response.status_code == 200, f"\nEndpoint error system {self.response.status_code}!"

    def validation_path_value(self):
        response_body = self.response.json()
        response_value = response_body["places"]
        for places in response_value:
            place_name = places["place name"]
            assert place_name == "Beverly Hills", f"\nResponse correct is: ***{place_name}***"

    def validation_schema_json(self):
        response_body = self.response.json()
        type_value = response_body["places"]
        assert (type(type_value)) == dict, f"\nType the  ♥{type_value}♥ is not value, is ***☻☻{type(type_value)}☻☻*** "
