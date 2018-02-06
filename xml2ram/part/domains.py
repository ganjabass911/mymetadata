from metadata.domain import Domain


def search(dom):
    domains = []
    for dim in dom.getElementsByTagName("domain"):
        domain = Domain()
        for name, value in dim.attributes.items():
            if name == "id":
                domain.id = value
            if name == "name":
                domain.name = value
            if name == "description":
                domain.description = value
            if name == "type":
                domain.type = value
            if name == "length":
                domain.length = value
            if name == "char_length":
                domain.char_length = value
            if name == "precision":
                domain.precision = value
            if name == "scale":
                domain.scale = value
            if name == "props":
                domain.props = value
            if name == "width":
                domain.width = value
            if name == "align":
                domain.align = value
            if name == "show_null":
                domain.show_null = value
            if name == "show_lead_nulls":
                domain.show_lead_nulls = value
            if name == "thousands_separator":
                domain.thousands_separator = value
            if name == "summable":
                domain.summable = value
            if name == "case_sensitive":
                domain.case_sensitive = value
            if name == "uuid":
                domain.uuid = value
        domains.append(domain)
    return domains
