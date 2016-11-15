from django.views.generic import ListView, DetailView
from alumni.models import User


class UserLV(ListView):
    model = User

    def get_queryset(self):
        queryset = super(UserLV, self).get_queryset()

        q = self.request.GET.get("q")
        if q:
            return queryset.filter(name__icontains=q)
        return queryset


class UserDV(DetailView):
    model = User
