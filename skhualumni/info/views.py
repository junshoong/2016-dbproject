from django.shortcuts import render
from info.models import Info


def render_greeting(request):
    greeting = Info.objects.filter(category='GRT')
    greeting = greeting.first()
    old_greeting = Info.objects.filter(category='OLD_GRT')
    old_greeting = old_greeting.first()
    context = {'obj': greeting, 'old_obj': old_greeting}
    return render(request, 'info/greeting.html', context)


def render_business(request):
    business = Info.objects.filter(category='BSN')
    business = business.first()
    context = {'obj': business}
    return render(request, 'info/business.html', context)


def render_organization(request):
    organization = Info.objects.filter(category='ORG')
    organization = organization.first()
    context = {'obj': organization}
    return render(request, 'info/organization.html', context)


def render_map(request):
    map = Info.objects.filter(category='MAP')
    map = map.first()
    context = {'obj': map}
    return render(request, 'info/map.html', context)


def render_usage(request):
    usage = Info.objects.filter(category='USE').reverse()
    context = {'obj_list': usage}
    return render(request, 'info/usage.html', context)

