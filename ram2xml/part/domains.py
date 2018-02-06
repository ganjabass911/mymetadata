def create(dom, schema):
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
