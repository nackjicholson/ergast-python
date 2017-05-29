# ergast-python
Python HTTP client to the Ergast Motor Racing Data API

This is a work in progress. The goal is to create a convenient python client
for the [Ergast Developer API](http://ergast.com/mrd/).

It should:

- include all the resource types the API makes available
- allow a wide range of the filtering and custom requests of the API
- be organized into packages for each resource type
- convert the data to not all be strings.
- be well tested, unit and integration.
- more ideas as I go.


```python
import ergast

ergast.seasons.get_list()
# [{'season': '1950', 'url': 'http://en.wikipedia.org/wiki/1950_Formula_One_season'}, ...]
```
