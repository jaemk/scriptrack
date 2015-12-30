from django.conf.urls import url

from django.contrib.auth import views as auth_views
from . import views

app_name = 'tally'
urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^login', auth_views.login, {'template_name': 'admin/login.html'}, name='login'),
        url(r'^logout', views.logout_view, name='logout'),
        #url(r'^logout', auth_views.logout, {'next_page': '/'}, name='logout'),
        url(r'^students/$', views.students, name='students'),
        url(r'^businesses/$', views.businesses, name='businesses'),
        url(r'^purchases/$', views.purchases, name='purchases'),
        url(r'^students/(?P<student_id>[a-zA-Z0-9_]+)/$', 
            views.student_detail, name='student_detail'),

        url(r'^businesses/(?P<business_name>[a-zA-Z0-9_]+)/$', 
            views.business_detail, name='business_detail'),
        url(r'^purchases/(?P<purchase_id>[a-zA-Z0-9_]+)/$',
            views.purchase_detail, name='purchase_detail'),
        url(r'^add/student/$', views.add_student, name='add_student'),
        ]

