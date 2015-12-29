from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse as httpresp


def index(request):
    #return httpresp('welcome to the index!\n From here you can view students or businesses')
    #context = {'my_response': 'generic response'}
    return render(request, 'tally/index.html')


def students(request):
    return httpresp('welcome to the students index')


def businesses(request):
    return httpresp('welcome to the business index')


def purchases(request):
    return httpresp('welcome to the purchase index')


def student_detail(request, student_name):
    return httpresp('welcome to {}\'s student-detail view'.format(student_name))


def business_detail(request, business_name):
    return httpresp('welcome to {}\'s business-detail view'.format(business_name))

