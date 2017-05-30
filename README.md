# ergast-python
Python HTTP client to the Ergast Motor Racing Data API

This is a work in progress. The goal is to create a convenient python client
for the [Ergast Developer API](http://ergast.com/mrd/).

It should:

- include all the resource types the API makes available
- allow a wide range of the filtering and custom requests of the API
- be organized into packages for each resource type
- convert the data to not all be strings. (ergast sends back all strings)
- be well tested, unit and integration.
- have methods for really commmon requests
- have aquery builder for custom requests
- inspire more ideas as I go.
- have constantly improving documentation


**Generic Custom ErgastRequest**

```python
from ergast import Request, client

req = Request(resource='results', id='1', criteria=dict(drivers='ricciardo'))

result = client.send(req)
# Result is the data from following request listing the 4 races won by Daniel Ricciardo
# GET http://ergast.com/api/f1/drivers/ricciardo/results/1.json
```


**Convenience Methods by resource type**

```python
import ergast

ergast.seasons.get_driver_seasons('ricciardo')
# [{'season': '2011', 'url': 'http://en.wikipedia.org/wiki/2011_Formula_One_season'}, ...]

# Convenience for doing:
# req = Request(resource='seasons', criteria=dict(drivers='ricciardo'))
# result_data = client.send(req)
# result_data['MRData']['SeasonTable']['Seasons']
```
