from django.urls import reverse
from core.models import *
from django.test import TestCase, TransactionTestCase, Client

class TestCoreViews(TransactionTestCase):
    
    @classmethod
    def setUp(cls):
        cls.client = Client()
        cls.homePageUrl = reverse("homePage")
        cls.user = User.objects.create(id=1,username='test_user')


    def test_login_function(self):
        response = self.client.get(self.homePageUrl)
        print(response.context)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,"core/homePage.html")
        self.assertEqual(response.context["user"],"django.contrib.auth.models.AnonymousUser")
        #self.assertContains(response,"'partials/authButtons.html'")
        #self.assertIsInstance(response.context["form"], APIKey)
        
    """ 
    def test_collect_freshdesk_GET(self):
       
        response = self.client.get(self.url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,"main/get_api_key.html")
        self.assertContains(response,"form")
        self.assertIsInstance(response.context["form"], APIKey)
        
    def test_collect_freshdesk_POST_valid_key(self):
       
        response = self.client.post(reverse("collect_freshdesk"),{"key":FRESHDESK_API_KEY})
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,"main/tickets.html")
        self.assertContains(response,"Tickets added to database")
            
    def test_collect_freshdesk_POST_wrong_key(self):
              
        # Form is valid but key is wrong for authentication 
        response = self.client.post(reverse("collect_freshdesk"),{"key":"api_key"})
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,"main/tickets.html")
        self.assertContains(response,"401 Unauthorized - Invalid API Key")
        
    def test_collect_freshdesk_POST_expired_key(self):
       
        response = self.client.post(reverse("collect_freshdesk"),{"key":FRESHDESK_EXPIRED_API_KEY})
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,"main/tickets.html")
        self.assertContains(response,"401")
        
    def test_collect_freshdesk_POST_invalid_key(self):
       
        response = self.client.post(reverse("collect_freshdesk"),{"key":""})
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,"main/error.html")
        self.assertContains(response,"Invalid API Key")
        
    def test_tickets_are_in_the_database(self):
        
        # Creating ticket
        integration = Integration.objects.create(user = self.user, data = {"FRESHDESK": {"api_key": ".."},"channel_type": "FRESHDESK"})
        customer = Customer.objects.create(owner = self.user, integration = integration, data = {"FRESHDESK":{"sender_id":"12347433"}}, identifier = "user_id")
        conversation = Conversation.objects.create(integration = integration,
                                                        user = self.user,
                                                        customer = customer)
        
        self.comment = UserComment(customer = customer, 
                                integration = integration,
                                conversation = conversation,
                                                 
                                title = "Payment failed",
                                comment = "I was trying to make a payment on your site and got a \"Your payment failed\" error. However, my card was charged. Can you let me know if the order is processed or what I need to do? Please see the attached screenshot.\n\nThanks,\nMatt",
                                rating = 5,
                                sender = "151011197607",
                                sent_date_time = "2022-12-28 01:32:43+03",
                                collect_date_time = "2022-11-25 17:29:21.366687+03").save()
        
       
        response = self.client.post(reverse("collect_freshdesk"),{"key":FRESHDESK_API_KEY})
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,"main/tickets.html")
        self.assertContains(response,"Duplicate Error - Tickets are in the database.")
    """ 