class SchemaJsonValidation:

    def validate_path(self, path):
        value_path = self.json()
        assert (type(value_path[path])) == str, f"\nType the  ♥{value_path[path]}♥ is not type, is ***☻☻{type(value_path[path])}☻☻*** "
