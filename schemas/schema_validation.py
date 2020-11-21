class SchemaJsonValidation:

    def schema_path(self, name):
        value_path = self.json()
        assert (type(value_path[
                         name])) == str, f"\nType the  ♥{value_path[name]}♥ is not type, is ***☻☻{type(value_path[name])}☻☻*** "

    def schema_validation_array(self, address, street):
        json = self.json()
        value_path = json[address]
        assert type(value_path) == dict, f"Type the ♥{value_path}♥ is not type, is ***☻☻{type(value_path)}☻☻***"
        value_object = json[address][street]
        assert type(value_object) == str, f"Type the ♥{value_object}♥ is not type, is ***☻☻{type(value_object)}☻☻*** "

# type array
# for address in response_value:
#     street = address["street"]
#     assert street == "Kulas Light", f"\nResponse correct is: ***{street}***"

# validate type str
# response_body = self.response.json()
# type_value = response_body["name"]
# assert (type(type_value)) == str, f"\nType the  ♥{type_value}♥ is not type, is ***☻☻{type(type_value)}☻☻*** "
