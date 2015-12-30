from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.http import HttpResponse as httpresp

from .models import Student, Business, Purchase


###### Private Methods ######

def _get_username(request):
    if request.user.is_authenticated():
        username = request.user
    else:
        username = None

    return username


###### General Views ######

def index(request):
    username = _get_username(request)
    return render(request, 'tally/index.html', {'loggedin_username':username})

def logout_view(request):
    username = request.user
    logout(request)
    return httpresp('''Goodbye {} !<br>
                    You\'ve successfully logged out!<br>
                    <a href="/">return to homepage</a>'''.format(username))



######  Student Views ######

@login_required(login_url='/tally/login')
def students(request):
    username = _get_username(request)
    student_list = Student.objects.all()
    context = {'student_list':student_list, 'loggedin_username':username }
    return render(request, 'tally/students.html', context)

@login_required(login_url='/tally/login')
def student_detail(request, student_id):
    username = _get_username(request)
    student = Student.objects.get(pk=student_id)
    all_purchases = student.all_purchases()
    thisyear_purchases = student.year_purchases()
    total_spent = sum([p.amount for p in all_purchases])
    total_earned = sum([p.student_earned for p in all_purchases])
    spent_thisyear = sum([p.amount for p in thisyear_purchases])
    earned_thisyear = sum([p.student_earned for p in thisyear_purchases])

    context = {'student':student, 'purchases':all_purchases, 'total_spent':total_spent,
               'total_earned':total_earned, 'thisyear_spent':spent_thisyear,
               'thisyear_earned':earned_thisyear, 'loggedin_username':username}

    return render(request, 'tally/student_detail.html', context)

@login_required(login_url='/tally/login')
def add_student(request):
    return render(request, 'tally/add_student.html')



###### Business Views ######

def businesses(request):
    return httpresp('welcome to the business index')

def business_detail(request, business_name):
    return httpresp('welcome to {}\'s business-detail view'.format(business_name))



###### Purchase Views ######

def purchases(request):
    return httpresp('welcome to the purchase index')

def purchase_detail(request, purchase_id):
    purchase = Purchase.objects.get(pk=purchase_id)
    return httpresp('details for purchase -- {}'.format(purchase))

def add_purchase_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    return httpresp('form to add new purchase for student {}'.format(student.full_name))



