def search(self, dom):
    domains = dom.createElement("domains")
    for teg in self.schema.domains:
        domain = dom.appendChild("domain")
        if teg.id is not None:
            domain.setAttribute("id", teg.id)
        if teg.name is not None:
            domain.setAttribute("name", teg.name)
        if teg.description is not None:
            domain.setAttribute("description", teg.description)
        if teg.data_type_id is not None:
            domain.setAttribute("data_type_id", teg.data_type_id)
        if teg.length is not None:
            domain.setAttribute("length", teg.length)
        if teg.char_length is not None:
            domain.setAttribute("char_length", teg.char_length)
        if teg.precision is not None:
            domain.setAttribute("precision", teg.precision)
        if teg.scale is not None:
            domain.setAttribute("scale", teg.scale)
        if teg.width is not None:
            domain.setAttribute("width", teg.width)
        if teg.align is not None:
            domain.setAttribute("align", teg.align)
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