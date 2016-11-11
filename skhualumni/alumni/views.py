from django.views.generic import ListView, DetailView
from alumni.models import User


class UserLV(ListView):
    model = User


class UserDV(DetailView):
    model = User
