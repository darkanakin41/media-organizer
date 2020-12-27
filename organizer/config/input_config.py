from marshmallow import Schema, fields


class InputConfig(Schema):
    """
    Input folders configuration
    """

    # pylint: disable=anomalous-backslash-in-string
    extensions = fields.String(required=False, allow_none=False, missing='.*\.(mkv|mp4|avi)$')
    folders = fields.List(fields.String, required=True, allow_none=False)
    ignored = fields.List(fields.String, required=False, allow_none=False, missing=[])
