from .News import News
from .Rant import Rants

import colander

class RantsResponse(colander.MappingSchema):
    rants = Rants()
    news = News()
    success = colander.SchemaNode(colander.Boolean())
    error = colander.SchemaNode(colander.Boolean(), missing=colander.drop)
    settings = colander.SchemaNode(colander.String(), missing=colander.drop)
    set = colander.SchemaNode(colander.String())
    wrw = colander.SchemaNode(colander.Int())
