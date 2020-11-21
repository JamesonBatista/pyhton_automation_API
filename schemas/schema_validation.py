class SchemaJsonValidation:

    def schema_path(self, name):
        v = self.json()
        assert (type(v[name])) == str, f"\nType the  ♥{v[name]}♥ is not type, is ***☻☻{type(v[name])}☻☻*** "

    def schema_validation_array(self, address, street):
        json = self.json()
        v = json[address]
        assert type(v) == dict, f"Type the ♥{v}♥ is not type, is ***☻☻{type(v)}☻☻***"
        v = json[address][street]
        assert type(v) == str, f"Type the ♥{v}♥ is not type, is ***☻☻{type(v)}☻☻*** "

# type array
# for address in response_value:
#     street = address["street"]
#     assert street == "Kulas Light", f"\nResponse correct is: ***{street}***"

# validate type str
# response_body = self.response.json()
# type_value = response_body["name"]
# assert (type(type_value)) == str, f"\nType the  ♥{type_value}♥ is not type, is ***☻☻{type(type_value)}☻☻*** "
