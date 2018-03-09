import minidom_fixed as md


def start_convert(schema):
    dom = md.Document()
    node = dom.createElement("dbd_schema")
    if schema.fulltext_engine is not None:
        node.setAttribute("fulltext_engine", schema.fulltext_engine)
    if schema.version is not None:
        node.setAttribute("version", schema.version)
    if schema.name is not None:
        node.setAttribute("name", schema.name)
    if schema.description is not None:
        node.setAttribute("description", schema.description)
    node.appendChild(dom.createElement("custom"))
    node.appendChild(domains_create(dom, schema))
    node.appendChild(tables_create(dom, schema))
    dom.appendChild(node)
    return dom


def domains_create(dom, schema):
    domains = dom.createElement("domains")
    for teg in schema.domains:
        domain = dom.createElement("domain")
        if teg.id is not None:
            domain.setAttribute("id", teg.id)
        if teg.name is not None:
            domain.setAttribute("name", teg.name)
        if teg.description is not None:
            domain.setAttribute("description", teg.description)
        if teg.type is not None:
            domain.setAttribute("type", teg.type)
        if teg.align is not None:
            domain.setAttribute("align", teg.align)
        if teg.width is not None:
            domain.setAttribute("width", teg.width)
        if teg.length is not None:
            domain.setAttribute("length", teg.length)
        if teg.precision is not None:
            domain.setAttribute("precision", teg.precision)
        if teg.props is not None:
            domain.setAttribute("props", teg.props)
        if teg.scale is not None:
            domain.setAttribute("scale", teg.scale)
        if teg.char_length is not None:
            domain.setAttribute("char_length", teg.char_length)
        if teg.show_null is not None:
            domain.setAttribute("show_null", teg.show_null)
        if teg.show_lead_nulls is not None:
            domain.setAttribute("show_lead_nulls", teg.show_lead_nulls)
        if teg.thousands_separator is not None:
            domain.setAttribute("thousands_separator", teg.thousands_separator)
        if teg.summable is not None:
            domain.setAttribute("summable", teg.summable)
        if teg.case_sensitive is not None:
            domain.setAttribute("case_sensitive", teg.case_sensitive)
        if teg.uuid is not None:
            domain.setAttribute("uuid", teg.uuid)
        domains.appendChild(domain)
    return domains


def tables_create(dom, schema):
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
        if teg.fields is not None:
            for tag_fields in teg.fields:
                table.appendChild(fields_create(dom, tag_fields))
        if teg.constraints is not None:
            for tag_constraints in teg.constraints:
                table.appendChild(constraints_create(dom, tag_constraints))
        if teg.indices is not None:
            for tag_indices in teg.indices:
                table.appendChild(indices_create(dom, tag_indices))
        tables.appendChild(table)
    return tables


def fields_create(dom, teg):
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
        field.setAttribute("can_input ", teg.can_input)
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
    return field


def constraints_create(dom, teg):
    constraint = dom.createElement("constraint")
    # if teg.id is not None:
    #     constraint.setAttribute("id ", teg.id)
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
    return constraint


def indices_create(dom, teg):
    index = dom.createElement("index")
    if teg.id is not None:
        index.setAttribute("id", teg.id)
    if teg.table_id is not None:
        index.setAttribute("table_id", teg.table_id)
    if teg.name is not None:
        index.setAttribute("name", teg.name)
    if teg.fields is not None:
        index.setAttribute("field", teg.fields)
    if teg.props is not None:
        index.setAttribute("props", teg.props)
    if teg.local is not None:
        index.setAttribute("local", teg.local)
    if teg.kind is not None:
        index.setAttribute("kind", teg.kind)
    if teg.uuid is not None:
        index.setAttribute("uuid", teg.uuid)
    return index
