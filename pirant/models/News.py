import colander

class News(colander.MappingSchema):
    id = colander.SchemaNode(colander.Int())
    type = colander.SchemaNode(colander.String())
    headline = colander.SchemaNode(colander.String())
    body = colander.SchemaNode(colander.String())
    footer = colander.SchemaNode(colander.String())
    height = colander.SchemaNode(colander.Int())
    action = colander.SchemaNode(colander.String())