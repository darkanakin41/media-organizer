import os

from marshmallow import Schema, fields


class TheTvDbConfig(Schema):
    """
    The TV DB configuration
    """

    api_key = fields.String(required=False, allow_none=True, missing=lambda: os.environ.get('THETVDB_API_KEY'))
    language = fields.String(required=False, allow_none=False, missing='en')
    debug = fields.Boolean(required=False, allow_none=False, missing=False)


class InputConfig(Schema):
    """
    Input folders configuration
    """
    # pylint: disable=anomalous-backslash-in-string
    extensions = fields.String(required=False, allow_none=False, missing='.*\.(mkv|mp4|avi)$')
    folders = fields.List(fields.String, required=True, allow_none=False)
    ignored = fields.List(fields.String, required=False, allow_none=False, missing=[])


class OutputConfig(Schema):
    """
    Output folders configuration
    """

    target = fields.String(required=True, allow_none=False)
    type = fields.String(required=True, allow_none=False)
    filters = fields.Dict(required=False, allow_none=False, missing={})


class GlobalConfig(Schema):
    """
    Global configuration for Media Organizer
    """

    thetvdb = fields.Nested(TheTvDbConfig, missing=TheTvDbConfig())
    input = fields.Nested(InputConfig, missing=InputConfig())
    output = fields.List(fields.Nested(OutputConfig, missing=OutputConfig()), missing=[])
