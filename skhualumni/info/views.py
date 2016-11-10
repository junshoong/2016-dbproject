from django.shortcuts import render
from info.models import Info

"""
class GreetingView(DetailView):
    model = Info
    template_name = 'greeting.html'


class BusinessView(DetailView):
    model = Info
    template_name = 'business.html'


class OrganizationView(DetailView):
    model = Info
    template_name = 'organization.html'


class MapView(DetailView):
    model = Info
    template_name = 'map.html'


class UsageView(DetailView):
    model = Info
    template_name = 'usage.html'

"""


def greet(request):
    greeting = Info.objects.filter(category='GRT')
    context = {'greeting': greeting}
    return render(request, 'greeting.html', context)
