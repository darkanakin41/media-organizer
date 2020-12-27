from marshmallow import Schema, fields


class OutputConfig(Schema):
    """
    Output folders configuration
    """

    target = fields.String(required=True, allow_none=False)
    type = fields.String(required=True, allow_none=False)
    filters = fields.Dict(required=False, allow_none=False, missing={})
