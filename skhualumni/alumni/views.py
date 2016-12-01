from django.views.generic import ListView, DetailView
from alumni.models import User


class UserLV(ListView):
    model = User

    def get_queryset(self):
        queryset = super(UserLV, self).get_queryset()

        q = self.request.GET.get("q")
        if q:
            q1 = queryset.filter(name__icontains=q)
            q2 = queryset.filter(login_id__icontains=q)
            q2 = q2.exclude(open_login_id=False)
            queryset = q1 | q2

            return queryset
        return queryset


class UserDV(DetailView):
    model = User
    context_object_name = 'alumni'
