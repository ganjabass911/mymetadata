def search(self, dom):
    tables = dom.createElement("tables")
    for teg in self.schema.tables:
        table = dom.appendChild("table")
        if teg.id is not None:
            table.setAttribute("id", teg.id)
        if teg.schema_id is not None:
            table.setAttribute("schema_id", teg.schema_id)
        if teg.name is not None:
            table.setAttribute("name", teg.name)
        if teg.description is not None:
            table.setAttribute("description", teg.description)
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
        table.appendChild(self.__parsXMLfields(dom, table))
        table.appendChild(self.__parsXMLconstraints(dom, table))
        table.appendChild(self.__parsXMLindices(dom, table))
        tables.appendChild(table)
    return tables
