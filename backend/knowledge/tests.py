from django.test import TestCase
from rest_framework.test import APIClient

from knowledge.models import KnowledgeBase


class KnowledgeBaseApiTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_create_list_update_and_delete_knowledge_base(self) -> None:
        create_response = self.client.post(
            "/api/knowledge-bases/",
            {
                "name": "产品知识库",
                "description": "客服问答与产品手册",
                "status": KnowledgeBase.Status.ACTIVE,
            },
            format="json",
            HTTP_HOST="localhost",
        )

        self.assertEqual(create_response.status_code, 201)
        self.assertEqual(create_response.data["name"], "产品知识库")
        self.assertEqual(create_response.data["document_count"], 0)

        knowledge_base_id = create_response.data["id"]
        list_response = self.client.get("/api/knowledge-bases/", HTTP_HOST="localhost")

        self.assertEqual(list_response.status_code, 200)
        self.assertEqual(len(list_response.data), 1)
        self.assertEqual(list_response.data[0]["id"], knowledge_base_id)

        update_response = self.client.patch(
            f"/api/knowledge-bases/{knowledge_base_id}/",
            {"status": KnowledgeBase.Status.ARCHIVED},
            format="json",
            HTTP_HOST="localhost",
        )

        self.assertEqual(update_response.status_code, 200)
        self.assertEqual(update_response.data["status"], KnowledgeBase.Status.ARCHIVED)

        delete_response = self.client.delete(
            f"/api/knowledge-bases/{knowledge_base_id}/",
            HTTP_HOST="localhost",
        )

        self.assertEqual(delete_response.status_code, 204)
        self.assertFalse(KnowledgeBase.objects.exists())

    def test_search_knowledge_bases_by_name(self) -> None:
        KnowledgeBase.objects.create(name="产品知识库")
        KnowledgeBase.objects.create(name="销售资料")

        response = self.client.get(
            "/api/knowledge-bases/?search=产品",
            HTTP_HOST="localhost",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "产品知识库")
