import unittest
import json
from main import create_app, db

class TestAuth(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.app = create_app()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        cls.client = cls.app.test_client()
        db.create_all()

        runner = cls.app.test_cli_runner()
        runner.invoke(args=["db-c", "seed"])

    @classmethod
    def tearDown(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()

    # test not functional
    def test_register(self):
        pass
        # response = self.client.post(
        #     "/auth/register/",
        #     data=json.dumps({"username":"testname", "password": "testpass"}),
        #     content_type='application/json',
        # )

        # data = json.loads(response.get_data(as_text=True))

        # self.assertEqual(response.status_code, 200)
        # self.assertIsInstance(data, dict)

    # test not functional
    def test_login(self):
        pass
        # response = self.client.get("/auth/login/")

        # data = response.get_json()

        # self.assertEqual(response.status_code, 200)
        # # self.assertIsInstance(data, list)