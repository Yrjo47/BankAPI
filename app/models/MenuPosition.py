import mongoengine as me


class MenuPosition(me.Document):
    name = me.StringField(required=True, unique=True)
    cost = me.IntField(required=True)
