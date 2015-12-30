from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.http import HttpResponse as httpresp

from .models import Student, Business, Purchase


### Private Methods

def _get_name(request):
    if request.user.is_authenticated():
        name = request.user
    else:
        name = None

    return name


### General Views

def index(request):
    name = _get_name(request)
    return render(request, 'tally/index.html', {'loggedin_username':name})

def logout_view(request):
    name = request.user
    logout(request)
    return httpresp('''Goodbye {} !<br>
                    You\'ve successfully logged out!<br>
                    <a href="/">return to homepage</a>'''.format(name))


### Student Views

@login_required(login_url='/tally/login')
def students(request):
    name = _get_name(request)
    student_list = Student.objects.all()
    context = {'student_list':student_list, 'loggedin_username':name }
    return render(request, 'tally/students.html', context)

@login_required(login_url='/tally/login')
def student_detail(request, student_id):
    student = Student.objects.get(pk=student_id)
    total_spent = ''
    total_earned = ''
    spent_thisyear = ''
    earned_thisyear = ''
    purchases = ''
    context = {'student':student}
    return render(request, 'tally/student_detail.html', context)
    #return httpresp('welcome to {}\'s student-detail view'.format(student))

@login_required(login_url='/tally/login')
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



