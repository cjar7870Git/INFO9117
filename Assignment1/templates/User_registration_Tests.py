import Assignment1
import unittest


class UserRegisterTestCase(unittest.TestCase):
    def setUp(self):
        Assignment1.app.config['TESTING'] = True
        self.app = Assignment1.app.test_client()

    def register(self, username, password):
        return self.app.post('/register', data=dict(
            username = username,
            password=password
        ),follow_redirects=True)

    def test_register_ok(self):
        rv = self.register("testRegister", "test123")
        assert b'Success' in rv.data

    def test_login_existing_user(self):
        rv = self.register("test", "test")
        assert b'Fail' in rv.data

if __name__ == '__main__':
    unittest.main()