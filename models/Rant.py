import colander

class Rant(colander.MappingSchema):
    id = colander.SchemaNode(colander.Int())
    text = colander.SchemaNode(colander.String())
    score = colander.SchemaNode(colander.Int())
    created_time = colander.SchemaNode(colander.Int())
    user_id = colander.SchemaNode(colander.Int())
    num_comments = colander.SchemaNode(colander.Int())
    user_username = colander.SchemaNode(colander.String())

class Rants(colander.SequenceSchema):
    rants = Rant()