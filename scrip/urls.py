"""scrip URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.contrib.auth import views as auth_views

from tally import urls as tally_urls
from tally import views as tally_views
from main import urls as main_urls


urlpatterns = [
    url(r'^', include(main_urls)),
    # url(r'^accounts/login', auth_views.login, {'template_name': 'admin/login.html'}, name='login'),
    url(r'^accounts/login', auth_views.login, {'template_name': 'tally/login.html'}, name='login'),
    url(r'^accounts/logout', tally_views.logout_view, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^tally/', include(tally_urls)),
]
