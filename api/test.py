from AddressBook import app
import unittest


class FlaskTest(unittest.TestCase):
    # Check for correct status response code (200)
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/welcome")
        statusCode = response.status_code
        self.assertEqual(statusCode, 200)

    # Check for correct content type (application/json)
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get("/welcome")
        self.assertEqual(response.content_type, "application/json")

    # Check for words in return message
    def test_index_data(self):
        tester = app.test_client(self)
        response = tester.get("/welcome")
        self.assertTrue(b"Success" in response.data)


if __name__ == "__main__":
    unittest.main()
