from __future__ import absolute_import

from . import client
from .request import Request


def get_all():
    req = Request(resource='seasons')
    return client.send(req)


def by_driver(driver_id):
    req = Request(resource='seasons', criteria=dict(drivers=driver_id))
    return client.send(req)
