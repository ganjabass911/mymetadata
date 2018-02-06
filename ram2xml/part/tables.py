from ram2xml.part.part_tables import fields
from ram2xml.part.part_tables import constraints
from ram2xml.part.part_tables import indices


def create(dom, schema):
    tables = dom.createElement("tables")
    for teg in schema.tables:
        table = dom.createElement("table")
        if teg.id is not None:
            table.setAttribute("id", teg.id)
        if teg.schema_id is not None:
            table.setAttribute("schema_id", teg.schema_id)
        if teg.name is not None:
            table.setAttribute("name", teg.name)
        if teg.description is not None:
            table.setAttribute("description", teg.description)
        if teg.props is not None:
            table.setAttribute("props", teg.props)
        if teg.ht_table_flags is not None:
            table.setAttribute("ht_table_flags", teg.ht_table_flags)
        if teg.access_level is not None:
            table.setAttribute("access_level", teg.access_level)
        if teg.can_add is not None:
            table.setAttribute("can_add", teg.can_add)
        if teg.can_edit is not None:
            table.setAttribute("can_edit", teg.can_edit)
        if teg.can_delete is not None:
            table.setAttribute("can_delete", teg.can_delete)
        if teg.temporal_mode is not None:
            table.setAttribute("temporal_mode", teg.temporal_mode)
        if teg.means is not None:
            table.setAttribute("means", teg.means)
        if teg.uuid is not None:
            table.setAttribute("uuid", teg.uuid)
        table.appendChild(fields.create(dom, teg))
        table.appendChild(constraints.create(dom, teg))
        table.appendChild(indices.create(dom, teg))
        tables.appendChild(table)
    return tables
