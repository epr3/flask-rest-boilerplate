from marshmallow import Schema, fields


class FacultySchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
