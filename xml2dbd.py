from xml.dom import minidom

from metadata import \
    Schema, \
    Table, \
    Domain, \
    Field, \
    Constraint, \
    Index



def __init__(self):
    self.schema = None


def start_convert(xml_file_name):
    dom = minidom.parse(xml_file_name)
    schema = Schema()
    for name, value in dom.documentElement.attributes.items():
        if name == "fulltext_engine":
            schema.fulltext_engine = value
        if name == "version":
            schema.version = value
        if name == "name":
            schema.name = value
        if name == "description":
            schema.description = value
    schema.domains = domains_search(dom)
    schema.tables = tables_search(dom)
    return schema


def domains_search(dom):
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


def tables_search(dom):
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
        temp.fields = fields_search(tag)
        temp.constraints = constraints_search(tag)
        temp.indices = indices_search(tag)
        tables.append(temp)
    return tables


def fields_search(dom):
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


def constraints_search(dom):
    constraints = []
    for tag in dom.getElementsByTagName("constraint"):
        temp = Constraint()
        for name, value in tag.attributes.items():
            # if name == "id":
            #     temp.id = value
            if name == "table_id":
                temp.table_id = value
            if name == "name":
                temp.name = value
            if name == "kind":
                temp.kind = value
            if name == "items":
                temp.items = value
            if name == "kind":
                temp.constraint_type = value
            if name == "reference":
                temp.reference = value
            if name == "props":
                temp.props = value
            if name == "unique_key_id":
                temp.unique_key_id = value
            if name == "has_value_edit":
                temp.has_value_edit = value
            if name == "cascading_delete":
                temp.cascading_delete = value
            if name == "expression":
                temp.expression = value
            if name == "uuid":
                temp.uuid = value
        constraints.append(temp)
    return constraints


def indices_search(dom):
    indices = []
    for tag in dom.getElementsByTagName("index"):
        temp = Index()
        for name, value in tag.attributes.items():
            if name == "id":
                temp.id = value
            if name == "table_id":
                temp.table_id = value
            if name == "name":
                temp.name = value
            if name == "constraint_type":
                temp.constraint_type = value
            if name == "reference":
                temp.reference = value
            if name == "unique_key_id":
                temp.unique_key_id = value
            if name == "has_value_edit":
                temp.has_value_edit = value
            if name == "cascading_delete":
                temp.cascading_delete = value
            if name == "expression":
                temp.expression = value
            if name == "uuid":
                temp.uuid = value
            if name == "field":
                temp.fields = value
            if name == "props":
                temp.props = value
        indices.append(temp)
    return indices
