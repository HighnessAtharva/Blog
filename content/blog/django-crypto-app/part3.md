---
title: "Django Crypto App Part 3: Wrap-Up and Testing"
date: 2023-05-01T23:20:34+05:30
draft: false
cover: 
    image: blog/django-crypto-app/cover-3.png
    alt: Part 3 - Wrap-Up and Testing
    caption: Here, we will wrap the series up by discussing testing approach by writing test cases for Models, Views and Templates using Pytest.
tags: ["Django", "Python"]
---

- [Introduction](#introduction)
- [Test Driven Development Approach Explained](#test-driven-development-approach-explained)
  - [URL Testing](#url-testing)
  - [Model Testing](#model-testing)
  - [View Testing](#view-testing)
- [Writing Tests](#writing-tests)
  - [Testing URLS](#testing-urls)
  - [Testing Models](#testing-models)
  - [Testing Views](#testing-views)
- [How to Run Tests](#how-to-run-tests)
- [Conclusion](#conclusion)

## Introduction

Welcome to the final part of the 3-part technical tutorial series, where have been building a Django project that enables users to manage their cryptocurrency portfolios. To implement the functionalities and additional features, we'll be utilizing API calls to coingecko or any other cryptocurrency API.

In the first part, we set up the project and created the models. In the second part continued off from that point and added all the templates, views and urls and code up the entire crypto project. So, if you haven't read the previous parts, I highly recommend you to do so before continuing with this part. Here, we will exclusively discuss testing approach by writing test cases for Models, Views and Templates using Pytest. We will also write a ton of tests to ensure that our code is working as expected and generate a coverage report to see how much of our code is covered by the tests.

The code for the entirety of the project can be found here ->  **[Github Repo for Django Crypto App](
<https://github.com/HighnessAtharva/django-crypto-app>)**

Testing is an important part of software development. It helps us to ensure that our code is working as expected and also helps us to catch bugs early on. It also helps us to ensure that our code is maintainable and readable. So, let's get started.

## Test Driven Development Approach Explained

In Django, automated testing can be performed at three levels: URL testing, model testing, and view testing.

### URL Testing

URL testing in Django is used to check if the endpoints specified in the URL patterns are correctly configured and pointing to the appropriate views. This is important because if an endpoint is incorrect or pointing to the wrong view, the application will not be able to process the request, leading to errors or incorrect behavior. URL testing is typically performed using the Django Client class, which simulates a web client and allows the developer to send requests to the application.

### Model Testing

Model testing in Django is used to check if the data stored in the database matches the expected schema and constraints specified in the models.py file. It helps ensure that the application is storing and retrieving data correctly and that the database is working as expected. Model testing is typically performed using the Django TestCase class and its various assertion methods, which allow the developer to create test data, save it to the database, and verify that the data has been saved correctly.

### View Testing

View testing in Django is used to check if the business logic defined in the views.py file is functioning correctly. It is used to test whether the views are handling requests as expected and returning the appropriate responses. View testing is typically performed using the Django TestCase class and its various assertion methods, which allow the developer to simulate requests and verify the responses.

> For this crypto-wallet app, I used all three types of automated testing.

**For URL testing**, I created a series of test cases that used the Django Client class to simulate requests to various endpoints in the application. Each test case sent a request to the endpoint and verified that the response was the expected template.

**For model testing**, I created a series of test cases that used the Django TestCase class to create test data, save it to the database, and verify that it had been saved correctly. Each test case tested a specific model or relationship between models to ensure that the data was being stored and retrieved correctly.

**For view testing**, I created a series of test cases that used the Django TestCase class to simulate requests to various views in the application. Each test case sent a request to the view and verified that the response was the expected result.

## Writing Tests

Go to the `tests.py` file in the `mainapp` folder and add the following imports since we will be using them in our tests.

```python
from decimal import Decimal
from unittest.mock import patch

from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import Client, TestCase
from django.urls import resolve, reverse
from test_plus import TestCase

from .forms import CustomUserCreationForm
from .models import *
from .views import *
```

Now that we have understood the theory, motivation and the approach, let's start writing tests.

### Testing URLS

This is a test class for testing the URLs of a web application. The test class inherits from Django's `TestCase` class, and it has test methods for each of the URLs in the application.

The class has a `setUp()` method that creates a test user to use for the tests.

The test methods are named according to the following convention:

- `test[PageName]` tests that the page with the given name can be accessed by the client.
- `test[PageName]Url` tests that the URL for the given page resolves to the correct view function.
- `test[PageName]Template` tests that the correct template is used for the given page.
- `test[PageName]ContainsCorrectHtml` tests that the correct HTML content is displayed on the given page.
- `test[PageName]FormCorrect` tests that the correct form is used for the given page.
- `test[PageName]RedirectsTo[OtherPageName]` tests that the given page redirects to the correct other page.
- `test[PageName]RedirectIfAlreadyLoggedIn` tests that the given page redirects to the correct page if the user is already logged in.

The test methods use Django's testing client to make requests to the application's URLs and check the responses. They use Django's `reverse()` function to generate URLs for the application's views, and they use Django's `resolve()` function to match URLs to view functions. They also use Django's `assertTemplateUsed()` function to check that the correct template is used, and they use Django's `assertContains()` and `assertNotContains()` functions to check for the presence or absence of specific HTML content in the response.

```python
class UrlTest(TestCase):

    # CREATE THE TEST USER
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='12345'
        )
    

    """ 
    ----------------
    HOME PAGE TESTS
    -----------------
    """
    def testHomePage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
      
    def testHomePageUrl(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home_view)  
    
    def testHomePageTemplate(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
    
    def testHomePageContainsCorrectHtml(self):
        response = self.client.get('/')
        self.assertContains(response, 'Top 10 CryptoCurrency Rankings')
        self.assertNotContains(response, 'Hi there! I should not be on the page.')
        
    
    """ 
    ----------------
    LOGIN PAGE TESTS
    -----------------
    """
    def testLoginPage(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        
    def testLoginPageUrl(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, login_view)
        
    def testLoginPageTemplate(self):
        response = self.client.get('/login/')
        self.assertTemplateUsed(response, 'login.html')
         
    def testLoginPageContainsCorrectHtml(self):
        response = self.client.get('/login/')
        self.assertContains(response, 'Login')
        self.assertNotContains(response, 'Hi there! I should not be on the page.')
    
    def testLoginPageRedirectsToPortfolioPage(self):
        self.client.login(username=self.user.username, password='12345')
        response = self.client.get('/login/')
        self.assertRedirects(response, '/portfolio/')
    
    def testLoginPageRedirectIfAlreadyLoggedIn(self):
        self.client.login(username=self.user.username, password='12345')
        response = self.client.get('/login/')
        self.assertRedirects(response, '/portfolio/')
  
    def testLoginPageFormCorrect(self):
        response = self.client.get('/login/')
        form = response.context.get('form')
        self.assertIsInstance(form, AuthenticationForm)
        self.assertContains(response, 'csrfmiddlewaretoken')
         
    """ 
    ----------------
    SIGNUP PAGE TESTS
    -----------------
    """
    def testSignupPage(self):
        response = self.client.get('/signup/')
        self.assertEqual(response.status_code, 200)
        
    
    def testSignupPageUrl(self):
        url = reverse('signup')
        self.assertEqual(resolve(url).func, signup_view)
        
    def testSignupPageTemplate(self):
        response = self.client.get('/signup/')
        self.assertTemplateUsed(response, 'signup.html')
         
    def testSignupPageContainsCorrectHtml(self):
        response = self.client.get('/signup/')
        self.assertContains(response, 'Signup')
        self.assertNotContains(response, 'Hi there! I should not be on the page.')
    
    def testSignupPageRedirectIfAlreadyLoggedIn(self):
        self.client.login(username=self.user.username, password='12345')
        response = self.client.get('/signup/')
        self.assertRedirects(response, '/portfolio/')

    def testSignupPageFormCorrect(self):
        response = self.client.get('/signup/')
        form = response.context.get('form')
        self.assertIsInstance(form, UserCreationForm)
        self.assertContains(response, 'csrfmiddlewaretoken')

    """ 
    ----------------
    PORTFOLIO PAGE TESTS
    -----------------
    """
    def testPortfolioPageNoLogin(self):    
        # check if logged out user can access portfolio page
        response = self.client.get('/portfolio/')
        self.assertEqual(response.status_code, 302)
            
    def testPortfolioPageLogin(self):
        # check if logged in user can access portfolio page
        self.client.login(username=self.user.username, password='12345')
        response = self.client.get('/portfolio/')
        self.assertEqual(response.status_code, 200)
    
    def testPortfolioPageUrl(self):
        url = reverse('portfolio')
        self.assertEqual(resolve(url).func, portfolio_view)
        
    def testPortfolioPageTemplate(self):
        self.client.login(username=self.user.username, password='12345')
        response = self.client.get('/portfolio/')
        self.assertTemplateUsed(response, 'portfolio.html')
    
    def testPortfolioPageContainsCorrectHtml(self):
        self.client.login(username=self.user.username, password='12345')
        response = self.client.get('/portfolio/')
        self.assertContains(response, 'Wallet')
        self.assertNotContains(response, 'Hi there! I should not be on the page.')


    """    
    ----------------
    RESET PAGE TESTS
    -----------------
    """
    
    def testResetPasswordPageUrl(self):
        url = reverse('password_reset')
        self.assertEqual(resolve(url).func.view_class, auth_views.PasswordResetView)
         
    def testResetPasswordPageTemplate(self):
        response = self.client.get('/password_reset/')
        self.assertTemplateUsed(response, 'reset/password_reset.html')
    
    def testResetPasswordPageContainsCorrectHtml(self):
        response = self.client.get('/password_reset/')
        self.assertContains(response, 'Reset Password')
        self.assertNotContains(response, 'Hi there! I should not be on the page.')
        
    def testResetPasswordDonePageUrl(self):
        url = reverse('password_reset_done')
        self.assertEqual(resolve(url).func.view_class, auth_views.PasswordResetDoneView)
         
    def testResetPasswordDonePageTemplate(self):
        response = self.client.get('/password_reset_done/')
        self.assertTemplateUsed(response, 'reset/password_reset_done.html')
        
    def testResetPasswordDonePageContainsCorrectHtml(self):
        response = self.client.get('/password_reset_done/')
        self.assertContains(response, 'An email has been sent with instructions to reset your password')
        self.assertNotContains(response, 'Hi there! I should not be on the page.')
    
    def testResetPasswordCompletePageUrl(self):
        url = reverse('password_reset_complete')
        self.assertEqual(resolve(url).func.view_class, auth_views.PasswordResetCompleteView)
        
    def testResetPasswordCompletePageTemplate(self):
        response = self.client.get('/password_reset_complete/')
        self.assertTemplateUsed(response, 'reset/password_reset_complete.html')
        
    def testResetPasswordCompletePageContainsCorrectHtml(self):
        response = self.client.get('/password_reset_complete/')
        self.assertContains(response, 'Your password has been set.')
        self.assertNotContains(response, 'Hi there! I should not be on the page.')
        
    """    
    ----------------
    SEARCH PAGE TESTS
    -----------------
    """
         
    def testSearchPageNoLogin(self):
        response = self.client.get('/search/')
        self.assertEqual(response.status_code, 302)
    
    def testSearchPageUrl(self):
        url = reverse('search')
        self.assertEqual(resolve(url).func, search_view)
    
    # check if search page can only be accessed by POST request
    def testSearchPagePostOnly(self):
        self.client.login(username=self.user.username, password='12345')
        response = self.client.get('/search/')
        self.assertEqual(response.status_code, 405)
        
        response = self.client.post('/search/')
        self.assertEqual(response.status_code, 200)
```

### Testing Models

These test cases are written using the Python unittest framework and are designed to test the functionality of different models in a Django web application.

The setUp() method is a special method that is run before every test method. In this method, two User objects are created - one to serve as a test user and the other as a referral user.

The individual test methods are defined using the def keyword, followed by the name of the test method. Each test method tests a specific aspect of a particular model, such as the User, Cryptocurrency, Referral, Portfolio, or Profile model.

Within each test method, specific actions are taken to test certain aspects of the model, such as creating an instance of the model, setting its attributes, and checking that the expected values are returned. For example, the testUserModelCorrectData() method checks that the attributes of the User model, such as username and email, are correctly set.

The assert statements are used to check that the expected values are equal to the actual values. If the test fails, an error is raised and the test method stops running.

Overall, these test cases aim to ensure that each model in the Django web application functions correctly and behaves as expected.

```python
class ModelTest(TestCase):
    # CREATE THE TEST USER
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser2',
            email='testuser2@example.com',
            password='12345'
        )

        self.referral = User.objects.create_user(
            username='referraluser',
            email='referreduser@example.com',
            password='12345'
        )
       
    """
    ----------------
    USER MODEL TESTS
    -----------------
    """
    
    def testUserModelCorrectData(self):
        test_user = self.user
        self.assertEqual(test_user.username, 'testuser2')
        self.assertEqual(test_user.email, 'testuser2@example.com')
        self.assertTrue(isinstance(test_user, User))
        self.assertTrue(test_user.is_active)
        self.assertFalse(test_user.is_staff)
    
    def testErrorOnDuplicateUsername(self):
        with self.assertRaises(IntegrityError):
            User.objects.create_user(
                username='testuser2',
                email='testuser2@example.com',
                password='12345'
        )
                
    def testErrorOnDuplicateEmail(self):
        with self.assertRaises(IntegrityError):
            User.objects.create_user(
                username='testuser3',
                email='testuser2@example.com',
                password='12345'
            )
    
    """ 
    ----------------
    CRYPTOCURRENCY MODEL TESTS
    -----------------
    """
    
    def testCryptocurrencyModel(self):
        cryptocurrency = Cryptocurrency.objects.create(
            user = User.objects.create(username='testuser'),
            id_from_api = 'bitcoin',
            name = 'Bitcoin', 
            symbol = 'BTC',
            current_price = 10000,
            quantity = 1
        )
        self.assertEqual(cryptocurrency.name, 'Bitcoin')
        self.assertEqual(cryptocurrency.symbol, 'BTC')
        self.assertEqual(cryptocurrency.current_price, 10000)
        self.assertEqual(cryptocurrency.quantity, 1)
        self.assertEqual(cryptocurrency.user.username, 'testuser')
        self.assertTrue(isinstance(cryptocurrency, Cryptocurrency))
        
    def testCryptocurrencyModelErrorOnDuplicate(self):
        Cryptocurrency.objects.create(
            user = User.objects.create(username='testuser'),
            id_from_api = 'bitcoin',
            name = 'Bitcoin', 
            symbol = 'BTC',
            current_price = 10000,
            quantity = 1
        )
        with self.assertRaises(IntegrityError):
            Cryptocurrency.objects.create(
                user = User.objects.create(username='testuser'),
                id_from_api = 'bitcoin',
                name = 'Bitcoin', 
                symbol = 'BTC',
                current_price = 10000,
                quantity = 1
            )
            self.fail('Cryptocurrency model should not allow duplicate cryptocurrencies')
            
    def testCryptocurrencyCurrentPrice(self):
        crypto = Cryptocurrency.objects.create(
            user=self.user,
            id_from_api='bitcoin',
            name='Bitcoin', 
            symbol='BTC',
            current_price=10000,
            quantity=1
        )
        self.assertEqual(crypto.current_price, 10000)
        
    def testCryptocurrencyStr(self):
        crypto = Cryptocurrency.objects.create(
            user=self.user,
            id_from_api='bitcoin',
            name='Bitcoin', 
            symbol='BTC',
            current_price=10000,
            quantity=1
        )
        self.assertEqual(str(crypto), 'Bitcoin (BTC)')
        
    def testCryptocurrencyQuantityDefaultValue(self):
        crypto = Cryptocurrency.objects.create(
            user=self.user,
            id_from_api='bitcoin',
            name='Bitcoin', 
            symbol='BTC',
            current_price=10000
        )
        self.assertEqual(crypto.quantity, 1)
        
        
    """
    ----------------
    REFERRAL MODEL TESTS
    -----------------
    """
    
    # make a referral and check if it is created correctly
    def testReferralModel(self):
        referral = Referal.objects.create(
            user=self.user,
            referrer=self.referral
        )
        self.assertEqual(referral.user.username, 'testuser2')
        self.assertEqual(referral.referrer.username, 'referraluser')
        self.assertTrue(isinstance(referral, Referal))
        
    
    
    """ 
    ----------------
    PORTFOLIO MODEL TESTS
    -----------------
    """
      
    def testPortfolioModel(self):
        portfolio = Portfolio.objects.create(
            user=self.user,
            total_value=10000
        )
        self.assertEqual(portfolio.user.username, 'testuser2')
        self.assertEqual(portfolio.total_value, 10000)
        self.assertTrue(isinstance(portfolio, Portfolio))
    

    """ 
    ----------------
    PROFILE MODEL TESTS
    -----------------
    """
    def testProfileModel(self):
        # referral code should be generated automatically using small uuid
        import shortuuid
        shortuuid.ShortUUID().random(length=10)
          
        referral_code = shortuuid.uuid()
        
        # make a dummy user
        dummy_user = User.objects.create_user(
            username='dummyprofile',
            email = 'dummyemail@example.com',
            password='12345'
        )

        
        profile = Profile.objects.create(
            user=dummy_user,
            referral_code=referral_code
        )
        
        self.assertEqual(profile.user.username, 'dummyprofile')
        self.assertEqual(profile.referral_code, referral_code)
        self.assertTrue(isinstance(profile, Profile))
```

### Testing Views

```python
        
""" 
MAKING SEPERATE TEST CLASSES FOR VIEWS
"""

class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email="example@example.com", password='testpass')

    def test_login_view_with_valid_credentials(self):
        url = reverse('login')
        response = self.client.post(url, {'username': 'testuser', 'password': 'testpass'})
        self.assertRedirects(response, reverse('portfolio'))

    def test_login_view_with_invalid_credentials(self):
        url = reverse('login')
        response = self.client.post(url, {'username': 'invaliduser', 'password': 'invalidpass'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invalid username or password.")
        
        
class TestAddToPortfolioView(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_add_to_portfolio_view_success(self):
        with patch('mainapp.views.requests.get') as mock_get:
            mock_data = {
                'name': 'Bitcoin',
                'id': 'bitcoin',
                'symbol': 'BTC',
                'market_data': {
                    'current_price': {
                        'usd': 50000.00
                    }
                }
            }
            mock_get.return_value.json.return_value = mock_data

            data = {
                'id': 'bitcoin',
                'quantity': 10
            }
            response = self.client.post(
                reverse('add_to_portfolio'), data=data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('portfolio'))

        crypto_currency = Cryptocurrency.objects.get(
            user=self.user, id_from_api='bitcoin')
        self.assertEqual(crypto_currency.name, 'Bitcoin')
        self.assertEqual(crypto_currency.symbol, 'BTC')
        self.assertEqual(crypto_currency.quantity, 10)
        self.assertEqual(crypto_currency.current_price, 50000.00)

        portfolio = Portfolio.objects.get(user=self.user)
        self.assertEqual(portfolio.total_value, 500000.00)

    def test_add_to_portfolio_view_get_request(self):
        response = self.client.get(reverse('add_to_portfolio'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Need a crypto currency to add to your portfolio. Go back to the home page and search for a crypto currency.')

from django.contrib.auth.models import User
from django.test import Client, TestCase


class SearchViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')
        
    def test_valid_search(self):
        response = self.client.post('/search/', {'search_query': 'bitcoin'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'BTC')
        
    def test_invalid_search(self):
        response = self.client.post('/search/', {'search_query': 'invalid_crypto_currency'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No crypto currency found based on your search query.')


class DeleteFromPortfolioViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.crypto_currency = Cryptocurrency.objects.create(user=self.user, id_from_api='bitcoin', name='Bitcoin', symbol='BTC', current_price=Decimal('10000'), quantity=Decimal('2'))
        self.portfolio = Portfolio.objects.create(user=self.user, total_value=Decimal('20000'))

    def test_delete_from_portfolio_view(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('delete_from_portfolio', args=[self.crypto_currency.pk])
        response = self.client.post(url)
        self.assertRedirects(response, reverse('portfolio'))
        self.assertFalse(Cryptocurrency.objects.filter(pk=self.crypto_currency.pk).exists())
        self.portfolio.refresh_from_db()
        self.assertEqual(self.portfolio.total_value, Decimal('0'))

    def test_delete_from_portfolio_view_with_unauthenticated_user(self):
        url = reverse('delete_from_portfolio', args=[self.crypto_currency.pk])
        response = self.client.post(url)
        self.assertRedirects(response, reverse('login') + '?next=' + url)
        self.assertTrue(Cryptocurrency.objects.filter(pk=self.crypto_currency.pk).exists())
        self.portfolio.refresh_from_db()
        self.assertEqual(self.portfolio.total_value, Decimal('20000'))



class TestHomeView(TestCase):
    def setUp(self):
        self.client = Client()
        self.top_10_crypto_url_global = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=10&page=1&sparkline=true'
        self.top_10_crypto_data_global = requests.get(self.top_10_crypto_url_global).json()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.crypto = Cryptocurrency.objects.create(name='Bitcoin', symbol='BTC', id_from_api='bitcoin', user=self.user, current_price=Decimal('10000'), quantity=Decimal('2'))
        self.portfolio = Portfolio.objects.create(user=self.user, total_value=Decimal('20000'))
        self.url = reverse('home')

    def test_home_view_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTrue('top_10_crypto_data_global' in response.context)
        self.assertTrue('user_cryptocurrencies' in response.context)
        self.assertTrue('user_portfolio' in response.context)
        self.assertTrue('crypto_price_changes' in response.context)

    def test_home_view_unauthenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTrue('top_10_crypto_data_global' in response.context)
        self.assertFalse('user_cryptocurrencies' in response.context)
        self.assertFalse('user_portfolio' in response.context)
        self.assertFalse('crypto_price_changes' in response.context)
        
class SignupWithReferrerViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.referrer = User.objects.create_user(
            username='test_referrer', email='test_referrer@example.com', password='testpassword')
        self.referrer_profile = Profile.objects.get(user=self.referrer)
        self.referral_code = self.referrer_profile.referral_code

    def test_signup_with_referrer_view_GET(self):
        response = self.client.get(reverse('signup_with_referrer_view', args=[self.referral_code]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_with_referrer_view_POST(self):
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        }
        response = self.client.post(reverse('signup_with_referrer_view', args=[self.referral_code]), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 2)
        # get the user object from the database
    
        self.assertEqual(Referal.objects.get(user__username='testuser').referrer, self.referrer)
        self.assertEqual(Profile.objects.get(user__username='test_referrer').bonus, 100)
        self.assertRedirects(response, reverse('login'))
        
class SignupViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('signup')
        self.valid_data = {
            'username': 'johndoe',
            'email': 'johndoe@example.com',
            'password1': 'passw0rd',
            'password2': 'passw0rd'
        }
        
    def test_signup_view_get(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')
        self.assertIsInstance(response.context['form'], CustomUserCreationForm)
        
    def test_signup_view_post_invalid_data(self):
        invalid_data = self.valid_data.copy()
        invalid_data['password2'] = 'different_password'
        response = self.client.post(self.signup_url, invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')
        self.assertIsInstance(response.context['form'], CustomUserCreationForm)
        self.assertEqual(User.objects.count(), 0)
        
class LogoutViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpass'
        )
        self.client.login(username='testuser', password='testpass')
        
    def test_logout_view(self):
        # make sure user is logged in
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        # this is only visible to logged in users below the Top 10 Cryptocurrencies table
        self.assertTrue('24 Hour Price Changes' in str(response.content))

        # logout
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

        # check if user is logged out
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertFalse('testuser' in str(response.content))
        
class LoginViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@test.com',
            password='testpass'
        )

    def test_login_view_get(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_view_post_valid_credentials(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'testpass',
        })
        self.assertRedirects(response, reverse('portfolio'))
        user = authenticate(username='testuser', password='testpass')
        self.assertIsNotNone(user)
        self.assertEqual(user, self.user)
        self.assertTrue(user.is_authenticated)

    def test_login_view_post_invalid_credentials(self):
        response = self.client.post(self.login_url, {
            'username': 'wronguser',
            'password': 'wrongpass',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertContains(response, "Invalid username or password.")

    def tearDown(self):
        self.user.delete()
```

These are unit tests for a Django web application, testing various views in the application. Here's a detailed explanation of each of the views being tested and the purpose of the tests:

1. `LoginViewTest`:
   - `test_login_view_with_valid_credentials`: This test checks if a user can successfully log in to the application with valid credentials. It sends a `POST` request to the login URL with a valid username and password, and expects to be redirected to the portfolio page (assuming successful login).
   - `test_login_view_with_invalid_credentials`: This test checks if a user is unable to log in with invalid credentials. It sends a `POST` request to the login URL with an invalid username and password, and expects to receive a status code of 200 (assuming failed login) and to see an error message on the login page.
2. `TestAddToPortfolioView`:
   - `test_add_to_portfolio_view_success`: This test checks if a user can successfully add a cryptocurrency to their portfolio. It sends a `POST` request to the add-to-portfolio URL with a valid cryptocurrency ID and quantity, and expects to be redirected to the portfolio page (assuming successful addition). It also checks if the added cryptocurrency and its details (name, symbol, quantity, and current price) have been saved in the database, and if the user's portfolio value has been updated accordingly.
   - `test_add_to_portfolio_view_get_request`: This test checks if a user cannot add a cryptocurrency to their portfolio through a `GET` request. It sends a `GET` request to the add-to-portfolio URL and expects to receive a status code of 200 and an error message on the page.
3. `SearchViewTestCase`:
   - `test_valid_search`: This test checks if a user can successfully search for a cryptocurrency by sending a `POST` request to the search URL with a valid search query. It expects to receive a status code of 200 and to see the cryptocurrency's symbol on the search results page.
   - `test_invalid_search`: This test checks if a user receives an error message when searching for an invalid cryptocurrency. It sends a `POST` request to the search URL with an invalid search query and expects to receive a status code of 200 and an error message on the search results page.
4. `DeleteFromPortfolioViewTest`
   - This test case is testing a view called `DeleteFromPortfolioView`. The view is expected to receive a POST request with the primary key of a cryptocurrency object. The view should delete that cryptocurrency object from the database and update the user's portfolio value accordingly.
   - The `setUp` method creates a test client, a test user, a test cryptocurrency object, and a test portfolio object in the database.
   - The `test_delete_from_portfolio_view` method tests the view when the user is authenticated. It logs in the user using the test client, makes a POST request to the view with the primary key of the test cryptocurrency object, and asserts that the response redirects to the portfolio page. It then checks that the test cryptocurrency object no longer exists in the database and that the portfolio's total value is 0.
   - The `test_delete_from_portfolio_view_with_unauthenticated_user` method tests the view when the user is not authenticated. It makes a POST request to the view with the primary key of the test cryptocurrency object and asserts that the response redirects to the login page. It then checks that the test cryptocurrency object still exists in the database and that the portfolio's total value is still 20000.
5. `TestHomeView`
   - This test case is testing a view called `HomeView`. The view is expected to render a template called `home.html` and display a list of the top 10 cryptocurrencies, the user's cryptocurrencies, the user's portfolio, and the percentage changes in cryptocurrency prices.
   - The `setUp` method creates a test client, a test user, a test cryptocurrency object, and a test portfolio object in the database. It also makes a request to an external API to get the top 10 cryptocurrencies.
   - The `test_home_view_authenticated` method tests the view when the user is authenticated. It logs in the user using the test client, makes a GET request to the view, and asserts that the response status code is 200 and the correct template is used. It also checks that the response context contains the top 10 cryptocurrencies, the user's cryptocurrencies, the user's portfolio, and the percentage changes in cryptocurrency prices.
   - The `test_home_view_unauthenticated` method tests the view when the user is not authenticated. It makes a GET request to the view and asserts that the response status code is 200 and the correct template is used. It also checks that the response context contains the top 10 cryptocurrencies but does not contain the user's cryptocurrencies, the user's portfolio, or the percentage changes in cryptocurrency prices.
6. `SignupWithReferrerViewTestCase`
   - This test case checks the behavior of the view used for signing up with a referral code. In the `setUp`() method, a test user (referrer) is created, and the referral code is obtained from their profile.
   - The `test_signup_with_referrer_view_GET`() method sends a GET request to the view using the referral code and checks that the response status code is 200 and the `'signup.html`' template is used.
   - The `test_signup_with_referrer_view_POST`() method sends a POST request with valid user data and the referral code. It checks that the response status code is 302, indicating a successful redirect, the User object count is 2, and the referrer of the test user is the referrer created in `setUp`(). Additionally, it checks that the bonus of the referrer is now 100, and the response redirects to the '`login`' view.
7. `SignupViewTestCase`
   - This test case checks the behavior of the view used for normal user sign up. The `setUp`() method initializes the Client object, the URL of the view, and valid user data.
   - The `test_signup_view_get`() method sends a GET request to the view and checks that the response status code is 200, the '`signup.html`' template is used, and the context form is of type `CustomUserCreationForm`.
   - The `test_signup_view_post_invalid_data`() method sends a POST request with invalid user data, and it checks that the response status code is 200, the 'signup.html' template is used, and the form is of type CustomUserCreationForm. Additionally, it checks that no User objects have been created.
8. `LogoutViewTestCase`
   - This test case checks the behavior of the view used for user logout. The `setUp`() method initializes the Client object, creates a test user, and logs them in.
   - The `test_logout_view`() method sends a GET request to the home page and checks that the response status code is 200 and the '24 Hour Price Changes' element is present.
   - It then sends a GET request to the logout view and checks that the response status code is 302. Finally, it sends another GET request to the home page and checks that the response status code is 200, and the test user's name is not present.
9. `LoginViewTestCase`
    - This test case checks the behavior of the view used for user login. The `setUp`() method initializes the Client object, the URL of the view, and creates a test user. The `test_login_view_get`() method sends a GET request to the view and checks that the response status code is 200, and the `'login.html'` template is used.
    - The `test_login_view_post_valid_credentials`() method sends a POST request with valid user credentials and checks that the response is a successful redirect to the portfolio view, the user object is authenticated, and the user object is the same as the one created in `setUp`().
    - The `test_login_view_post_invalid_credentials`() method sends a POST request with invalid user credentials and checks that the response status code is 200, the '`login.html`' template is used, and an error message is displayed. Finally, the tearDown() method deletes the test user object.

## How to Run Tests

All tests are written in the `tests.py` file in the `mainapp` folder.

```bash
# to run all tests
python manage.py test

# to run tests for a specific class
python manage.py test -k <class-name>

# start coverage
coverage run --source='.' --omit=mainapp\tests.py manage.py test mainapp

# generate coverage report
coverage html

# check the htmlcov folder and open the index.html file
```

![test1](/blog/django-crypto-app/3-test1.png)
![test2](/blog/django-crypto-app/3-test2.png)
![test3](/blog/django-crypto-app/3-test3.png)

![coverage](https://github.com/HighnessAtharva/django-crypto-app/raw/main/assets/coverage.png?raw=true)

## Conclusion

This concludes the third and the final part of the series. Here we learned how to write tests for our Django project as well as the TDD approach. We saw how to write tests for models, views, and reverse urls and wrote over 60 test cases for our project achieving 90%+ test coverage.

This project was a great learning experience for me. I learned a lot about Django, and I also learned how to use the CoinGecko API. I also learned how to use the `unittest` module to write tests for my Django project. I hope you enjoyed reading this article. If you have any questions or suggestions, feel free to leave a comment below. Thank you for reading! 😊
