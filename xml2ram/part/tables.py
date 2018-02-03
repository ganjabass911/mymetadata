from ram_part.table import Table


def search(self, dom):
    tables = []
    for tag in dom.getElementsByTagName("table"):
        temp = Table()
        for name, value in tag.attributes.items():
            if name == "id":
                temp.id = value
            if name == "schema_id":
                temp.schema_id = value
            if name == "name":
                temp.name = value
            if name == "description":
                temp.description = value
            if name == "can_add":
                temp.can_add = value
            if name == "can_edit":
                temp.can_edit = value
            if name == "can_delete":
                temp.can_delete = value
            if name == "temporal_mode":
                temp.temporal_mode = value
            if name == "means":
                temp.means = value
            if name == "uuid":
                temp.uuid = value
        temp.fields = self.fields.search(tag)
        temp.constraints = self.constraints.search(tag)
        temp.indices = self.indices.search(tag)
        tables.append(temp)
    return tables
