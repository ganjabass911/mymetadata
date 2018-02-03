from xml.dom import minidom


def start_convert(self):
    dom = minidom.Document()
    node = dom.createElement("dbd_schema")
    if self.schema.fulltext_engine is not None:
        node.setAttribute("fulltext_engine", self.schema.version)
    if self.schema.version is not None:
        node.setAttribute("version", self.schema.version)
    if self.schema.name is not None:
        node.setAttribute("name", self.schema.version)
    if self.schema.description is not None:
        node.setAttribute("description", self.schema.version)
    node.appendChild(dom.createElement("custom"))
    node.appendChild(self.domains.search(dom))
    node.appendChild(self.tables.search(dom))
    return dom