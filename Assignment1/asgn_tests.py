import asgn
import unittest


class HelloWorldTestCase(unittest.TestCase):
    def setUp(self):
        asgn.app.config['TESTING'] = True
        self.app = asgn.app.test_client()

    def test_hello_world(self):
        rv = self.app.get('/')
        assert b'Hello World' in rv.data

    def test_not_hello_world(self):
        rv = self.app.get('/')
        assert b'Huyu' not in rv.data

if __name__ == '__main__':
    unittest.main()
