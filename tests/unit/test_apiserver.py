import unittest
from apiserver import apiserver
from urllib import parse

class TestApiServer(unittest.TestCase):

  def setUp(self):
    self.client = apiserver.app.test_client()
    print("Testing: ", self._testMethodName)

  def tearDown(self):
    pass

  def test_index(self):
    resp = self.client.get('/')
    self.assertEqual(resp.status, '200 OK')
    result = resp.get_data().decode('utf-8')
    self.assertTrue("API server is running" in result)

  def test_fibonacci(self):
    query = {'count': '10'}
    resp = self.client.get('fibonacci', query_string=query)
    self.assertEqual(resp.status, '200 OK')
    result = resp.get_data().decode('utf-8')
    self.assertEqual(result, '[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]')

  def test_factors(self):
    query = {'count': '150'}
    resp = self.client.get('factors', query_string=query)
    self.assertEqual(resp.status, '200 OK')
    result = resp.get_data().decode('utf-8')
    self.assertEqual(result, '[1, 2, 3, 5, 6, 10, 15, 25, 30, 50, 75, 150]')

  def test_intentional_failure(self):
    self.assertEqual(0, 1)

if __name__ == '__main__':
  unittest.main()
