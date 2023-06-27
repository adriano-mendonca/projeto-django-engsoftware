from django.test import TestCase
from django.urls import reverse

from .models import Question


class QuestionDetailViewTest(TestCase):
    def setUp(self):
        self.question = Question.objects.create(
            title="Qual é a capital do Piauí?"
        )

    def test_question_detail_view(self):
        url = reverse("question_detail", kwargs={"pk": self.question.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, self.question.title)

        self.assertContains(response, self.question.content)
