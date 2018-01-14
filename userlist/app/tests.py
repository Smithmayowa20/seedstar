from django.test import TestCase
from app.forms import UserForm
from app.models import Users
from django.core.urlresolvers import reverse

class UserFormTestCase(TestCase):
	#loading a saved python-manage.py-datadump 
	#database stored in the fixtures directory
    fixtures = ['users_view_testdata.json']
    
    def setUp(self):
        super(UserFormTestCase, self).setUp()
        self.user_1 = Users.objects.get(pk=1)
        self.user_2 = Users.objects.get(pk=2)
    
    def test_init(self):
        # Test successful init without data.
        form_1 = UserForm(instance=self.user_1)
        self.assertTrue(isinstance(form_1.instance, Users))
        self.assertEqual(form_1.instance.pk, self.user_1.pk)
        self.assertEqual(form_1.instance.name, self.user_1.name)
        self.assertEqual(form_1.instance.email, self.user_1.email)
		
        form_2 = UserForm(instance=self.user_2)
        self.assertTrue(isinstance(form_2.instance, Users))
        self.assertEqual(form_2.instance.pk, self.user_2.pk)
        self.assertEqual(form_2.instance.name, self.user_2.name)
        self.assertEqual(form_2.instance.email, self.user_2.email)
        
    
    def test_save(self):
        
        # Test the first choice.
        form_1 = UserForm(instance=self.user_1)
        self.assertEqual(self.user_1.pk, 1)
        
         # Test the second choice.
        form_2 = UserForm( instance=self.user_2)
        self.assertEqual(self.user_2.pk, 2)
        


class UsersTestCase(TestCase):
    fixtures = ['users_view_testdata.json']
    
    def setUp(self):
        super(UsersTestCase, self).setUp()
        self.user_1 = Users.objects.get(pk=1)
        self.user_2 = Users.objects.get(pk=2)
    
    def assert_data(self):
        # Assert pk's, usernames and emails are equal to 
		# data provided
        self.assertEqual(self.user_1.pk,1)
        self.assertEqual(self.user_2.pk,2)
        self.assertEqual(self.user_1.name,"Jacob Smith")
        self.assertEqual(self.user_1.email,"jacobsmith28@yahoo.com")
        self.assertEqual(self.user_2.name,"Evelyn Perty")
        self.assertEqual(self.user_2.email,"evelynperty50@yahoo.com")
		
    def test_new_user(self):
		# test newly created user
        user = Users.objects.create(
            name="Patrick Jones",email="patrickjones@gmail.com"
        )
        user.save()
        self.assertEqual(user.name,"Patrick Jones")
        self.assertEqual(user.email,"patrickjones@gmail.com")
    


class PollsViewsTestCase(TestCase):
    fixtures = ['users_view_testdata.json']
    
    def test_index(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)

    
    def test_list(self):
        resp = self.client.get(reverse('list_users'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('users' in resp.context)
        user_2 = resp.context['users'][0]
        self.assertEqual(user_2.name,"Jacobs")
        self.assertEqual(user_2.email,"smithmayowa20@gmail.com")
        
    
    def test_add(self):
        resp = self.client.get(reverse('add_user'))
        self.assertEqual(resp.status_code, 200)
