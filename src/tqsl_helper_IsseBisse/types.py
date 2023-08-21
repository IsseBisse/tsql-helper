def _trim(name):
    return name.replace("[", "").replace("]", "")


class Table:
    def __init__(self, schema, name):
        self.schema = _trim(schema)
        self.name = _trim(name)

    def __str__(self):
        return f"[{self.schema}].[{self.name}]"
