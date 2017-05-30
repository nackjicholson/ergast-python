"""
Tests for ergast.request
"""

import unittest

from ergast.request import Request


class RequestTestCase(unittest.TestCase):
    """
    python -m unittest -v test.test_request.RequestTestCase
    """
    def test_default_values(self):
        """should provide default settings"""
        subject = Request()

        actual = subject.data
        expected = {'protocol': 'http', 'host': 'www.ergast.com',
                    'series': 'f1', 'limit': '1000', 'offset': '0'}

        self.assertEqual(actual, expected)

    def test_kwargs_provide_additional_values(self):
        """should allow kwargs to define additional values"""
        subject = Request(resource='races', season='2017')

        self.assertEqual(subject.data['resource'], 'races')
        self.assertEqual(subject.data['season'], '2017')

    def test_request_validation(self):
        """should raise RuntimeError when given invalid settings"""
        self.assertRaises(RuntimeError, Request, resources='INVALID', limit=True)

    def test_coerce_number_values_to_string(self):
        """should coerce integer values to be strings"""
        subject = Request(
            resource='results',
            id=1,
            season=2017,
            round=1,
            limit=30,
            offset=2,
            criteria=dict(status=1)
        )

        actual = subject.data
        expected = dict(
            protocol='http',
            host='www.ergast.com',
            series='f1',
            resource='results',
            id='1',
            season='2017',
            round='1',
            limit='30',
            offset='2',
            criteria=dict(status='1')
        )

        self.assertEqual(actual, expected)
