import requests

API_URL = 'http://ergast.com/api/f1'


def get_list():
    endpoint = '/seasons.json'
    res = requests.get(API_URL + endpoint)
    res_data = res.json()
    return res_data['MRData']['SeasonTable']['Seasons']

