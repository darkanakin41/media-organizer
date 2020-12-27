import os

from marshmallow import Schema, fields


class TmDbConfig(Schema):
    """
    The TV DB configuration
    """

    api_key = fields.String(required=False, allow_none=True, missing=lambda: os.environ.get('THETVDB_API_KEY'))
    language = fields.String(required=False, allow_none=False, missing='en')
    debug = fields.Boolean(required=False, allow_none=False, missing=False)
