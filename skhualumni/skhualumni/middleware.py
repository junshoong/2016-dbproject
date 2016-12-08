from alumni.models import User
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
import re


class PasswordChangeMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated() \
                and not re.match(r'^/password_change/?', request.path) \
                and not re.match(r'^/logout/?', request.path) \
                and request.user.is_active:
            u = User.objects.get(id=request.user.id)
            if u.is_first_login:
                return HttpResponseRedirect('/password_change/')
