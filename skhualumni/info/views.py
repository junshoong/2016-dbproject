from django.shortcuts import render
from info.models import Info


def render_greeting(request):
    greeting = Info.objects.filter(category='GRT')
    context = {'greeting': greeting}
    return render(request, 'info/greeting.html', context)


def render_business(request):
    business = Info.objects.filter(category='BSN')
    context = {'business': business}
    return render(request, 'info/business.html', context)


def render_organization(request):
    organization = Info.objects.filter(category='ORG')
    context = {'organization': organization}
    return render(request, 'info/organization.html', context)


def render_map(request):
    map = Info.objects.filter(category='MAP')
    context = {'map': map}
    return render(request, 'info/map.html', context)


def render_usage(request):
    usage = Info.objects.filter(category='USE')
    context = {'usage': usage}
    return render(request, 'info/usage.html', context)

