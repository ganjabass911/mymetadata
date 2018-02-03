from xml.dom import minidom

from ram_part.schema import Schema
from xml2ram.part import \
    domains, \
    tables


def __init__(self):
    self.schema = None


def start_convert(self, xmlFileName):
    dom = minidom.parse(xmlFileName)
    self.schema = Schema()
    for name, value in dom.documentElement.attributes.items():
        if name == "fulltext_engine":
            self.schema.fulltext_engine = value
        if name == "version":
            self.schema.version = value
        if name == "name":
            self.schema.name = value
        if name == "description":
            self.schema.description = value
    self.schema.domains = domains.search(dom)
    self.schema.tables = tables.search(dom)
    return dom
