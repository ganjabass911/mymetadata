from metadata.constraint import Constraint


def search(dom):
    constraints = []
    for tag in dom.getElementsByTagName("constraint"):
        temp = Constraint()
        for name, value in tag.attributes.items():
            if name == "id":
                temp.id = value
            if name == "table_id":
                temp.table_id = value
            if name == "name":
                temp.name = value
            if name == "kind":
                temp.kind = value
            if name == "items":
                temp.items = value
            if name == "constraint_type":
                temp.constraint_type = value
            if name == "reference":
                temp.reference = value
            if name == "props":
                temp.props = value
            if name == "unique_key_id":
                temp.unique_key_id = value
            if name == "has_value_edit":
                temp.has_value_edit = value
            if name == "cascading_delete":
                temp.cascading_delete = value
            if name == "expression":
                temp.expression = value
            if name == "uuid":
                temp.uuid = value
        constraints.append(temp)
    return constraints
