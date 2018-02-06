def create(dom, table):
    fields = dom.createElement("fields")
    for teg in table.fields:
        field = dom.createElement("field")
        if teg.id is not None:
            field.setAttribute("id ", teg.id)
        if teg.table_id is not None:
            field.setAttribute("table_id ", teg.table_id)
        if teg.position is not None:
            field.setAttribute("position ", teg.position)
        if teg.name is not None:
            field.setAttribute("name ", teg.name)
        if teg.russian_short_name is not None:
            field.setAttribute("rname ", teg.russian_short_name)
        if teg.description is not None:
            field.setAttribute("description ", teg.description)
        if teg.domain_id is not None:
            field.setAttribute("domain ", teg.domain_id)
        if teg.can_input is not None:
            field.setAttribute("props ", teg.can_input)
        if teg.can_edit is not None:
            field.setAttribute("can_edit ", teg.can_edit)
        if teg.show_in_grid is not None:
            field.setAttribute("show_in_grid ", teg.show_in_grid)
        if teg.show_in_details is not None:
            field.setAttribute("show_in_details ", teg.show_in_details)
        if teg.is_mean is not None:
            field.setAttribute("is_mean ", teg.is_mean)
        if teg.autocalculated is not None:
            field.setAttribute("autocalculated ", teg.autocalculated)
        if teg.required is not None:
            field.setAttribute("required ", teg.required)
        if teg.uuid is not None:
            field.setAttribute("uuid ", teg.uuid)
        fields.appendChild(field)
    return fields
