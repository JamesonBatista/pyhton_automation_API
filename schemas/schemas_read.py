class SchemaJsonValidation:

    def validate_path(self,  path):
        value_path = self.json()
        value = value_path[path]
        assert (type(value)) == str, f"\nType the  ♥{value}♥ is not type, is ***☻☻{type(value)} ☻☻*** "
