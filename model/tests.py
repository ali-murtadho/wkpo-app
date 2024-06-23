from django.test import TestCase, Client
from model.models import ClassificationResult
from .models import ClassificationResult
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

# Create your tests here.
class ClassificationResultModelTest(TestCase):
    def setUp(self):
        ClassificationResult.objects.create(
            varietas="Varietas A",
            warna="Merah",
            rasa="Manis",
            musim="Musim Panas",
            penyakit="Tidak Ada",
            teknik="Organik",
            ph=6.5,
            boron=0.3,
            fosfor=0.4,
            prediction="Prediksi A"
        )

    def test_classification_result_creation(self):
        classification_result = ClassificationResult.objects.get(varietas="Varietas A")
        
        self.assertEqual(classification_result.warna, "Merah")
        self.assertEqual(classification_result.rasa, "Manis")
        self.assertEqual(classification_result.musim, "Musim Panas")
        self.assertEqual(classification_result.penyakit, "Tidak Ada")
        self.assertEqual(classification_result.teknik, "Organik")
        self.assertEqual(classification_result.ph, 6.5)
        self.assertEqual(classification_result.boron, 0.3)
        self.assertEqual(classification_result.fosfor, 0.4)
        self.assertEqual(classification_result.prediction, "Prediksi A")

    def test_classification_result_str(self):
        classification_result = ClassificationResult.objects.get(varietas="Varietas A")
        
        self.assertEqual(str(classification_result), "Varietas A, Merah, Prediksi A")

class UserRegistrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')  # Asumsikan ada URL pattern dengan nama 'register'

    def test_register_get(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_register_post_valid(self):
        response = self.client.post(self.register_url, {
            'username': 'testuser',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123',
        })
        self.assertEqual(response.status_code, 302)  # Redirection after successful registration
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_register_post_invalid(self):
        response = self.client.post(self.register_url, {
            'username': 'testuser',
            'password1': 'complexpassword123',
            'password2': 'wrongpassword',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')
        self.assertFalse(User.objects.filter(username='testuser').exists())

class UserLoginTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')  # Asumsikan ada URL pattern dengan nama 'login'
        self.home_url = reverse('home')  # Asumsikan ada URL pattern dengan nama 'home'
        self.user = User.objects.create_user(username='testuser', password='testpassword123')

    def test_login_get(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertIsInstance(response.context['form'], AuthenticationForm)

    def test_login_post_valid(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'testpassword123',
        })
        self.assertEqual(response.status_code, 302)  # Redirection after successful login
        self.assertRedirects(response, self.home_url)
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_post_invalid(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'wrongpassword',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertFalse(response.context['form'].is_valid())
        self.assertContains(response, "Invalid username or password.")
        self.assertFalse(response.wsgi_request.user.is_authenticated)

