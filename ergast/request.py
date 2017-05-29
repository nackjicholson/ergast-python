"""
ErgastRequest for describing requests to the ergast service
"""

from six.moves import UserDict


class ErgastRequest(UserDict):
    def __init__(self, *args, **kwargs):
        defaults = {'protocol': 'http', 'host': 'www.ergast.com',
                    'series': 'f1', 'limit': '1000', 'offset': '0'}
        settings = dict(defaults, **kwargs)
        super().__init__(*args, **settings)
