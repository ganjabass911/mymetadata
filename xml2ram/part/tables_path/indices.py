from ram_part.index import Index


def search(self, dom):
    indices = []
    for tag in dom.getElementsByTagName("index"):
        temp = Index()
        if tag.hasChildNodes():
            for item in tag.getElementsByTagName("item"):
                pass
        else:
            temp.fields.append(tag.getAttribute("field"))
        for name, value in tag.attributes.items():
            if name == "id":
                temp.id = value
            if name == "table_id":
                temp.table_id = value
            if name == "name":
                temp.name = value
            if name == "constraint_type":
                temp.constraint_type = value
            if name == "reference":
                temp.reference = value
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
        indices.append(temp)
    return indices