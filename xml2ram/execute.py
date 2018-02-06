
from xml.dom import minidom

from metadata.schema import Schema
from xml2ram.part import \
    domains, \
    tables


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
    schema.domains = domains.search(dom)
    schema.tables = tables.search(dom)
    return schema
