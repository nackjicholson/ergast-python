"""
ErgastRequest for describing requests to the ergast service
"""

from cerberus import Validator
from six.moves import UserDict

req_schema = {
    'protocol': {'type': 'string', 'allowed': ['http', 'https'], 'required': True},
    'host': {'type': 'string', 'allowed': ['www.ergast.com'], 'required': True},
    'series': {'type': 'string', 'allowed': ['f1'], 'required': True},
    'resource': {
        'type': 'string',
        'allowed': ['seasons', 'circuits', 'races', 'constructors',
                    'drivers', 'qualifying', 'results', 'driverStandings'
                    'constructorStandings', 'status', 'laps', 'pitstops']
    },
    'id': {
        'type': ['string', 'integer'],
        'coerce': str,
        'dependencies': 'resource'
    },
    'season': {'type': ['string', 'integer'], 'coerce': str},
    'round': {'type': ['string', 'integer'], 'coerce': str},
    'criteria': {
        'type': 'dict',
        'keyschema': {
            'type': 'string',
            'allowed': ['circuits', 'constructors', 'drivers',
                        'driverStandings', 'constructorStandings', 'grid',
                        'results', 'status', 'fastest', 'laps']
        },
        'valueschema': {'type': ['string', 'integer'], 'coerce': str}
    },
    'limit': {'type': ['string', 'integer'], 'coerce': str},
    'offset': {'type': ['string', 'integer'], 'coerce': str}
}
req_validator = Validator(req_schema)


class Request(UserDict):
    def __init__(self, *args, **kwargs):
        defaults = {'protocol': 'http', 'host': 'www.ergast.com',
                    'series': 'f1', 'limit': '1000', 'offset': '0'}
        settings = dict(defaults, **kwargs)

        if not req_validator.validate(settings):
            raise RuntimeError(req_validator.errors)

        super().__init__(*args, **req_validator.document)
