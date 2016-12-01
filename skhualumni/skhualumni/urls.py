"""skhualumni URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from skhualumni.views import HomeView, UserUpdateView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    # login, logout, password_change
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^my_page/$', UserUpdateView.as_view(), name='my_page'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^board/', include('board.urls', namespace='board')),
    url(r'^alumni/', include('alumni.urls', namespace='alumni')),
    url(r'^info/', include('info.urls', namespace='info')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
