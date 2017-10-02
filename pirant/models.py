import colander


class News(colander.MappingSchema):
    id = colander.SchemaNode(colander.Int())
    type = colander.SchemaNode(colander.String())
    headline = colander.SchemaNode(colander.String())
    body = colander.SchemaNode(colander.String())
    footer = colander.SchemaNode(colander.String())
    height = colander.SchemaNode(colander.Int())
    action = colander.SchemaNode(colander.String())


class Rant(colander.MappingSchema):
    id = colander.SchemaNode(colander.Int())
    text = colander.SchemaNode(colander.String())
    score = colander.SchemaNode(colander.Int())
    created_time = colander.SchemaNode(colander.Int())
    user_id = colander.SchemaNode(colander.Int())
    num_comments = colander.SchemaNode(colander.Int())
    user_username = colander.SchemaNode(colander.String())


class Rants(colander.SequenceSchema):
    rant = Rant()


class RantsResponse(colander.MappingSchema):
    rants = Rants()
    news = News()
    success = colander.SchemaNode(colander.Boolean(), missing=colander.drop)
    error = colander.SchemaNode(colander.Boolean(), missing=colander.drop)
    settings = colander.SchemaNode(colander.String(), missing=colander.drop)
    set = colander.SchemaNode(colander.String())
    wrw = colander.SchemaNode(colander.Int())


class Comment(colander.MappingSchema):
    id = colander.SchemaNode(colander.Int())
    rant_id = colander.SchemaNode(colander.Int())
    body = colander.SchemaNode(colander.String())
    upvotes = colander.SchemaNode(colander.Int(), missing=colander.drop)
    downvotes = colander.SchemaNode(colander.Int(), missing=colander.drop)
    score = colander.SchemaNode(colander.Int())
    created_time = colander.SchemaNode(colander.Int())
    user_id = colander.SchemaNode(colander.Int())
    user_username = colander.SchemaNode(colander.String())
    user_userscore = colander.SchemaNode(colander.Int(), missing=colander.drop)


class Comments(colander.SequenceSchema):
    comment = Comment()

class RantResponse(colander.MappingSchema):
    comments = Comments()
    rant = Rant()
    success = colander.SchemaNode(colander.Boolean(), missing=colander.drop)
    error = colander.SchemaNode(colander.Boolean(), missing=colander.drop)