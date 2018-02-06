def create(dom, table):
    constraints = dom.createElement("constraint")
    for teg in table.constraints:
        constraint = dom.createElement("constraint")
        if teg.id is not None:
            constraint.setAttribute("id ", teg.id)
        if teg.table_id is not None:
            constraint.setAttribute("table_id ", teg.table_id)
        if teg.name is not None:
            constraint.setAttribute("name ", teg.name)
        if teg.kind is not None:
            constraint.setAttribute("kind ", teg.kind)
        if teg.items is not None:
            constraint.setAttribute("items ", teg.items)
        if teg.constraint_type is not None:
            constraint.setAttribute("constraint_type ", teg.constraint_type)
        if teg.reference is not None:
            constraint.setAttribute("reference ", teg.reference)
        if teg.props is not None:
            constraint.setAttribute("props ", teg.props)
        if teg.unique_key_id is not None:
            constraint.setAttribute("unique_key_id ", teg.unique_key_id)
        if teg.has_value_edit is not None:
            constraint.setAttribute("has_value_edit ", teg.has_value_edit)
        if teg.cascading_delete is not None:
            constraint.setAttribute("cascading_delete ", teg.cascading_delete)
        if teg.expression is not None:
            constraint.setAttribute("expression ", teg.expression)
        if teg.uuid is not None:
            constraint.setAttribute("uuid ", teg.uuid)
        constraints.appendChild(constraint)
    return constraints
