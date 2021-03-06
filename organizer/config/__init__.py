from marshmallow import Schema, fields

from organizer.config.input_config import InputConfig
from organizer.config.output_config import OutputConfig
from organizer.config.tmdb_config import TmDbConfig


class GlobalConfig(Schema):
    """
    Global configuration for Media Organizer
    """

    tmdb = fields.Nested(TmDbConfig, missing=TmDbConfig().load({}))
    input = fields.Nested(InputConfig, missing=InputConfig().load({'folders': []}))
    output = fields.List(fields.Nested(OutputConfig), missing=[])
