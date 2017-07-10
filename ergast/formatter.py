from cerberus import Validator


def build_response(mrd, result, req):
    return dict(url=mrd['url'],
                limit=mrd['limit'],
                offset=mrd['offset'],
                total=mrd['total'],
                req=req,
                result=result)

season_schema = {
    'season': {'type': ['string', 'integer'], 'coerce': int},
    'url': {'type': 'string'}
}
season_validator = Validator({
    'Seasons': {
        'type': 'list',
        'schema': {'type': 'dict', 'schema': season_schema}
    }
}, allow_unknown=True)


def seasons_formatter(res_data, req):
    if req['resource'] != 'seasons':
        return None

    mrd = res_data['MRData']

    if not season_validator.validate(mrd['SeasonTable']):
        raise RuntimeError(season_validator.errors)

    result = season_validator.document['Seasons']
    return build_response(mrd, result, req.data)


formatters = [seasons_formatter]


def formatter(res_data, req):
    for formatter in formatters:
        result = formatter(res_data, req)

        if result is not None:
            return result

    return res_data
