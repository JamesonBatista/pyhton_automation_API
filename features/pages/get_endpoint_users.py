import requests

from Environment.environment import Environment


class GetBody:

    def __init__(self):
        self.response = None
        self.base_url = Environment().BASE_PATH

    def get_endpoint(self, endpoint):
        self.response = requests.get(self.base_url + endpoint)
        assert self.response.status_code == 200, f"\nEndpoint error system {self.response.status_code}!"

    def validation_path_value(self):
        response_body = self.response.json()
        response_value = response_body["name"]
        assert response_value == "Leanne Graham", f"\nResponse correct is: ***{response_value}***"
