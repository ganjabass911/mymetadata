def create(dom, teg):
    # indices = dom.createElement("indices")
    # for teg in table.indices:
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
        # indices.appendChild(index)
    return index
