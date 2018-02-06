from metadata.field import Field


def search(dom):
    fields = []
    for tag in dom.getElementsByTagName("field"):
        temp = Field()
        for name, value in tag.attributes.items():
            if name == "id":
                temp.id = value
            if name == "table_id":
                temp.table_id = value
            if name == "position":
                temp.position = value
            if name == "name":
                temp.name = value
            if name == "rname":
                temp.russian_short_name = value
            if name == "description":
                temp.description = value
            if name == "domain":
                temp.domain_id = value
            if name == "props":
                temp.can_input = value
            if name == "can_edit":
                temp.can_edit = value
            if name == "show_in_grid":
                temp.show_in_grid = value
            if name == "show_in_details":
                temp.show_in_details = value
            if name == "is_mean":
                temp.is_mean = value
            if name == "autocalculated":
                temp.autocalculated = value
            if name == "required":
                temp.required = value
            if name == "uuid":
                temp.uuid = value
        fields.append(temp)
    return fields
