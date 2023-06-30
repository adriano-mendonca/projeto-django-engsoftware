
from django.test import TestCase , Client 
from django.urls import reverse

class Test_ResultView(TestCase):
    def test_setUp(self):
        url = 'http://localhost:8000/tese/'
        self.client = Client()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_render_html(self):
        url = 'http://localhost:8000/tese/'
        resposta = self.client.get(url)
        self.assertTemplateUsed(resposta, 'quiz.html')
        

    def test_Used(self):
        url = 'http://localhost:8000/tese/'
        request = self.client.get(url)
        tese = self.assertContains(request , 'Quiz')