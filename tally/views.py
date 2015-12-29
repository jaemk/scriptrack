from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse as httpresp

from .models import Student, Business, Purchase

def index(request):
    return render(request, 'tally/index.html')


## Student Views
def students(request):
    #return httpresp('welcome to the students index')
    student_list = Student.objects.all()
    context = {'student_list':student_list}
    return render(request, 'tally/students.html', context)

def student_detail(request, student_id):
    student_name = Student.objects.get(pk=student_id).full_name
    return httpresp('welcome to {}\'s student-detail view'.format(student_name))

def add_student(request):
    return render(request, 'tally/add_student.html')


## Business Views
def businesses(request):
    return httpresp('welcome to the business index')

def business_detail(request, business_name):
    return httpresp('welcome to {}\'s business-detail view'.format(business_name))


## Purchase Views
def purchases(request):
    return httpresp('welcome to the purchase index')

def purchase_detail(request, purchase_id):
    return httpresp('details for purchase id {}'.format(purchase_id))



