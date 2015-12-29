from ..models import Student, Business, Purchase

def show_bs():
    print(Business.objects.all())

def show_ps():
    print(Purchase.objects.all())

def show_st():
    print(Student.objects.all())


## Clear Businesses
def _clear_all_businesses():
    businesses = Business.objects.all()
    for b in businesses:
        b.delete()

def _clear_specific_business(bname):
    bus = Business.objects.filter(name__contains=bname)
    for b in bus:
        b.delete()

def clear_businesses(name=''):
    if not name:
        print('keyword argument name=\'all\' or a business name')
        return
    
    if name.lower().strip() == 'all':
        _clear_all_businesses()

    else:
        _clear_specific_business(name.lower().strip())


## Clear Students
def _clear_all_students():
    students = Student.objects.all()
    for s in students:
        s.delete()

def _clear_specific_student(sname):
    st = Student.objects.filter(name__contains=sname)
    for s in st:
        s.delete()

def clear_students(name=''):
    if not name:
        print('keyword argument name=\'all\' or a student\'s name')
        return
    
    if name.lower().strip() == 'all':
        _clear_all_students()

    else:
        _clear_specific_student(name.lower().strip())


## Clear Purchases
def _clear_all_purchases():
    purchases = Purchase.objects.all()
    for p in purchases:
        p.delete()

def _clear_specific_purchase(p_id):
    pur = Purchase.objects.get(pk=p_id)
    pur.delete()

def clear_purchases(pid=''):
    if not pid:
        print('keyword argument pid=\'all\' or a purchases\'s id')
        return
    
    if pid.lower().strip() == 'all':
        _clear_all_purchases()

    else:
        _clear_specific_purchase(pid.lower().strip())


