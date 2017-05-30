"""
Ergast client templates ergast service urls from Request object
"""
from __future__ import absolute_import

import requests
from six import iteritems
from uritemplate import URITemplate

from .formatter import formatter


def send(req):
    criteria = []

    for key, value in iteritems(req.get('criteria', {})):
        criteria.append(key)
        criteria.append(value)

    url_tmpl = URITemplate('{protocol}://{host}/api{/series}{/season}{/round}'
                           '{/criteria*}{/resource}{/id}.json{?limit,offset}')

    url = url_tmpl.expand(req, criteria=criteria)
    res = requests.get(url)

    res.raise_for_status()

    res_data = res.json()

    # TODO: Format responses to target relevant data, and coerce numeric values to numbers
    # something like:
    # {limit, offset, total, url, result: []}
    # Remove all the ['MRData']['XXXXTable']['Races'][0] nonsense
    #
    # Might want a raw=True flag or something to be able to get around the formatting
    # if you want the full response for any reason.
    #
    # return Formatter(res_data, req.get('resource'))
    # return res_data
    return formatter(res_data, req)
