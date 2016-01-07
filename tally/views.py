from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.http import HttpResponse as httpresp
from django.http import HttpResponseRedirect as httprespred

from .models import Student, Business, Purchase
from .forms import StudentForm
import string

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
    return render(request, 'tally/index.html', {'username':username})

def logout_view(request):
    username = request.user
    logout(request)
    return httpresp('''Goodbye {} !<br>
                    You\'ve successfully logged out!<br>
                    <a href="/">return to homepage</a>'''.format(username))



######  Student Views ######

@login_required(login_url='/accounts/login')
def students(request):
    username = _get_username(request)
    student_list = Student.objects.all().order_by('first_name')
    context = {'student_list':student_list, 'username':username }
    return render(request, 'tally/students.html', context)

@login_required(login_url='/accounts/login')
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
               'thisyear_earned':earned_thisyear, 'username':username }

    return render(request, 'tally/student_detail.html', context)

def _add_student(username, formdat):
    full = ' '.join([formdat['first_name'].strip().lower(),
                    formdat['last_name'].strip().lower()])
    first = formdat['first_name'].strip().lower()
    last = formdat['last_name'].strip().lower()
    phone = formdat['phone'].strip().lower() if formdat['phone'].strip().lower() else None
    email = formdat['email'].strip().lower() if formdat['email'].strip().lower() else None
    school = formdat['school']
    enrolled = formdat['enrolled'] if formdat['enrolled'] else None
    adultsraw = formdat['adults'].strip().lower()
    adults = None
    if adultsraw:
        adults = [name.strip().lower() for name in adultsraw.split(',') if name.strip() != '']

    new_st = Student(full_name=full, first_name=first, last_name=last, phone=phone,
                     email=email, school=school, adults=adults, enrolled=enrolled,
                     added_by=username)
    new_st.save()
    return full

@login_required(login_url='/accounts/login')
def add_student(request):
    username = _get_username(request)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            full_name = _add_student(username, form.cleaned_data)
            student = Student.objects.get(full_name=full_name)

            # return httpresp('Your Post Info: ' + ', '.join([form.cleaned_data['first_name'], 
            #                 form.cleaned_data['last_name'],
            #                 str(form.cleaned_data['enrolled']),
            #                 form.cleaned_data['adults'],
            #                 form.cleaned_data['phone'],
            #                 form.cleaned_data['email']]))
        return httprespred('/tally/students/{}'.format(student.id))
    else:
        form = StudentForm()

    context = {'username':username, 'form':form.as_table()}
    return render(request, 'tally/add_student.html', context)



###### Business Views ######

@login_required(login_url='/accounts/login')
def businesses(request):
    username = _get_username(request)
    businesses = Business.objects.all()
    context = {'username':username, 'businesses':businesses, 'btitle':'one'}
    return render(request, 'tally/businesses.html', context)

@login_required(login_url='/accounts/login')
def business_detail(request, business_id):
    business = Business.objects.get(pk=business_id)
    context = {'business':business}
    return render(request, 'tally/business_detail.html', context)
    # return httpresp('welcome to {}\'s business-detail view'.format(business.name))



###### Purchase Views ######

@login_required(login_url='/accounts/login')
def purchases(request):
    username = _get_username(request)
    purchases = Purchase.objects.all()
    context = {'username':username, 'purchases':purchases}
    return render(request, 'tally/purchases.html', context)

@login_required(login_url='/accounts/login')
def purchase_detail(request, purchase_id):
    username = _get_username(request)
    purchase = Purchase.objects.get(pk=purchase_id)
    perc = str(round(purchase.business.percentage * 100, 2)) if purchase.business.percentage else 'N/A'
    percentage = '{}%'.format(perc)
    context = {'username':username, 'purchase':purchase, 'percentage':percentage}
    return render(request, 'tally/purchase_detail.html', context)

@login_required(login_url='/accounts/login')
def add_purchase_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    return httpresp('form to add new purchase for student {}'.format(student.full_name))



