import unittest
import json
from main import create_app, db

class TestDocs(unittest.TestCase):
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


    def test_doc_index(self):
        pass
        # response = self.client.get("/document/")

        # data = response.get_json()

        # self.assertEqual(response.status_code, 200)
        # self.assertIsInstance(data, list)
    
    def test_doc_create(self):
        pass
        # response = self.client.post(
        #     "/document/",
        #     data=json.dumps({"name":"testname"}),
        #     content_type='application/json',
        # )

        # data = response.get_json()

        # self.assertEqual(response.status_code, 200)
        # self.assertIsInstance(data, dict)

    def test_doc_retrive(self):
        pass
        # response = self.client.get("/document/")

        # data = response.get_json()

        # self.assertEqual(response.status_code, 200)
        # self.assertIsInstance(data, list)

    def test_doc_update(self):
        pass
        # response = self.client.put(
        #     "/md/1",
        #     data=json.dumps({"name":"testname"}),
        #     content_type='application/json',
        # )

        # data = json.loads(response.get_data(as_text=True))

        # self.assertEqual(response.status_code, 200)
        # self.assertIsInstance(data, list)

    def test_doc_delete(self):
        pass
        # self.client.post(
        #     "/document/",
        #     data=json.dumps({"name":"testname1"}),
        #     content_type='application/json',
        # )
        # response = self.client.get("/md/1")

        # data = response.get_json()

        # self.assertEqual(response.status_code, 200)
        # self.assertIsInstance(data, dict)