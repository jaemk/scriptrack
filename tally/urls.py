from django.conf.urls import url

from . import views

app_name = 'tally'
urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^students/$', views.students, name='students'),
        url(r'^businesses/$', views.businesses, name='businesses'),
        url(r'^students/(?P<student_name>[a-zA-Z0-9_]+)/$', 
            views.student_detail, name='student_detail'),

        url(r'^businesses/(?P<business_name>[a-zA-Z0-9_]+)/$', 
            views.business_detail, name='business_detail'),
        ]

