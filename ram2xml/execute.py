from metadata import minidom_fixed as md
from ram2xml.part import domains
from ram2xml.part import tables


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
    node.appendChild(domains.create(dom, schema))
    node.appendChild(tables.create(dom, schema))
    dom.appendChild(node)
    return dom
