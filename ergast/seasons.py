import requests

API_URL = 'http://ergast.com/api/f1'


def get_seasons():
    endpoint = '/seasons.json'
    res = requests.get(API_URL + endpoint)
    res_data = res.json()
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
    res = requests.get(API_URL + endpoint)
    res_data = res.json()
    mrd = res_data['MRData']
    result = mrd['SeasonTable']['Seasons']

    return {
        'limit': mrd['limit'],
        'offset': mrd['offset'],
        'total': mrd['total'],
        'result': result
    }
