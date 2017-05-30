from __future__ import absolute_import

from . import client
from .request import Request


def get_all():
    req = Request(resource='seasons')
    res_data = client.send(req)
    mrd = res_data['MRData']
    result = mrd['SeasonTable']['Seasons']

    return {
        'url': mrd['url'],
        'req': req.data,
        'limit': mrd['limit'],
        'offset': mrd['offset'],
        'total': mrd['total'],
        'result': result
    }


def by_driver(driver_id):
    req = Request(resource='seasons', criteria=dict(drivers=driver_id))
    res_data = client.send(req)
    mrd = res_data['MRData']
    result = mrd['SeasonTable']['Seasons']

    return {
        'url': mrd['url'],
        'req': req.data,
        'limit': mrd['limit'],
        'offset': mrd['offset'],
        'total': mrd['total'],
        'result': result
    }
