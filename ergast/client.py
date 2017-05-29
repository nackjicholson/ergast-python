"""

"""
from six import iteritems

import requests
from uritemplate import URITemplate


def send(req):
    criteria = []

    for key, value in iteritems(req.get('criteria', {})):
        criteria.append(key)
        criteria.append(value)

    url_tmpl = URITemplate('{protocol}://{host}/api{/series}{/season}{/round}'
                           '{/criteria*}/{resource}{/id}.json{?limit,offset}')

    url = url_tmpl.expand(req, criteria=criteria)
    res = requests.get(url)
    res_data = res.json()

    # return Formatter(res_data, req.get('resource'))
    return res_data
