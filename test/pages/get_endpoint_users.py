import requests


from Environment.environment import Environment as base
from schemas.schema_validation import SchemaJsonValidation as schemas


class GetBody:

    def __init__(self):
        self.response = None
        self.base_url = base().BASE_PATH

    def get_endpoint(self, endpoint):
        self.response = requests.get(self.base_url + endpoint)
        assert self.response.status_code == 200, f"\nEndpoint error system {self.response.status_code}!"

    def validation_path_value(self):
        response_body = self.response.json()
        response_value = response_body["address"]
        response_value_address = response_body["address"]["street"]
        assert (type(
            response_value)) == dict, f"Type the ♥{response_value}♥ is not type, is ***☻☻{type(response_value)}☻☻***"
        assert type(
            response_value_address) == str, f"Type the ♥{response_value_address}♥ is not type, is ***☻☻{type(response_value_address)}☻☻*** "

    def validation_schema_json(self):
        schemas.validate_path(self.response, "name")

# type array
# for address in response_value:
#     street = address["street"]
#     assert street == "Kulas Light", f"\nResponse correct is: ***{street}***"

# validate type str
# response_body = self.response.json()
# type_value = response_body["name"]
# assert (type(type_value)) == str, f"\nType the  ♥{type_value}♥ is not type, is ***☻☻{type(type_value)}☻☻*** "
