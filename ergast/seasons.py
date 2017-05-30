from __future__ import absolute_import

from . import client
from .request import Request


def get_seasons():
    req = Request(resource='seasons')
    res_data = client.send(req)
    mrd = res_data['MRData']
    result = mrd['SeasonTable']['Seasons']

    return {
        'limit': mrd['limit'],
        'offset': mrd['offset'],
        'total': mrd['total'],
        'result': result
    }


def get_driver_seasons(driver_id):
    endpoint = '/drivers/{}/seasons.json'.format(driver_id)
    req = Request(resource='seasons', criteria=dict(drivers=driver_id))
    res_data = client.send(req)
    mrd = res_data['MRData']
    result = mrd['SeasonTable']['Seasons']

    return {
        'limit': mrd['limit'],
        'offset': mrd['offset'],
        'total': mrd['total'],
        'result': result
    }
