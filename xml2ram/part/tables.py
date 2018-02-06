from metadata.table import Table
from xml2ram.part.tables_path import fields
from xml2ram.part.tables_path import constraints
from xml2ram.part.tables_path import indices


def search(dom):
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
            if name == "props":
                temp.props = value
            if name == "ht_table_flags":
                temp.ht_table_flags = value
            if name == "access_level":
                temp.access_level = value
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
        temp.fields = fields.search(tag)
        temp.constraints = constraints.search(tag)
        temp.indices = indices.search(tag)
        tables.append(temp)
    return tables
