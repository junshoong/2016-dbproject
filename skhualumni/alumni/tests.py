from django.test import TestCase
from django.test import RequestFactory
from django.test import Client
from unittest import skip
from django.views.generic import ListView
from alumni.views import UserSearchMixin
from alumni.models import User


@skip
class UserSearchMixinTest(TestCase):

    class DummyLV(UserSearchMixin, ListView):
        model = User

    def setUp(self):
        super(UserSearchMixinTest, self).setUp()

        user = User()
        user.login_id = '01050329325'
        user.name = '김준수'
        user.open_login_id = True
        user.period = 7
        user.save()

        self.client = Client().get('/alumni', {"q": "김준수"})
        self.request = RequestFactory().get('/alumni', {"q": "김준수"})
        self.view = self.DummyLV()

    def test_search_name(self):
        self.assertEqual(User.objects.all().count(), 1)
        # self.assertEqual(User.objects.filter(name="김준수").first().login_id, self.request.)
        d = self.view.get_queryset(self.request)
        print(d)

        # print(context)
        # self.assertEqual(context['name'], '김준수')


class UserModelTest(TestCase):

    def test_saving_and_retrieving_users(self):
        first_user = User()
        first_user.login_id = '01050329325'
        first_user.name = '김준수'
        first_user.save()

        saved_users = User.objects.all()
        self.assertEqual(saved_users.count(), 1)

        first_saved_user = saved_users[0]
        self.assertEqual(first_saved_user.login_id, '01050329325')
        self.assertEqual(first_saved_user.name, '김준수')
