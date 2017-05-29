"""
Tests for ergast.request
"""

import unittest

from ergast.request import ErgastRequest


class ErgastRequestTestCase(unittest.TestCase):
    """
    python -m unittest -v test.test_request.ErgastRequestTestCase
    """
    def test_default_values(self):
        """should provide default settings"""
        subject = ErgastRequest()

        actual = subject.data
        expected = {'protocol': 'http', 'host': 'www.ergast.com',
                    'series': 'f1', 'limit': '1000', 'offset': '0'}

        self.assertEqual(actual, expected)

    def test_kwargs_provide_additional_values(self):
        """should allow kwargs to define additional values"""
        subject = ErgastRequest(resource='races', season='2017')

        self.assertEqual(subject.data['resource'], 'races')
        self.assertEqual(subject.data['season'], '2017')
