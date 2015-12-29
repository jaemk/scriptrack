from ..models import Student, Business, Purchase
import os

location = os.path.dirname(os.path.realpath(__file__))
business_file = 'businesses.csv'
students_file = 'students.csv'
past_purchases_file = 'past_purchases.csv'

def show_location():
    print(location)

## Add all past purchases from past_purchases.csv
def _get_past_purchases_info(p_file):
    file_path = os.path.join(location, p_file)
    with open(file_path, 'r') as pfile:
        info_raw = [line.strip('\n') for line in pfile\
                    if line.strip() and line.strip() != '\n']

    headers_raw = info_raw.pop(0)
    headers = [i.strip().lower() for i in headers_raw.split(',')]
    info ={key:[] for key in headers}
    for line in info_raw:
        line_items = line.split(',')
        for i, key in enumerate(headers):
            info[key].append(line_items[i].strip().lower())

                    
    keys = ['firstname', 'lastname', 'fullname', 'wk 1-16', 'wk 17-22']
    items = [ [], [], [], {'spent':[], 'earned':[]}, {'spent':[], 'earned':[]} ]
    info_format = dict(zip(keys, items))
    for i in range(len(info['firstname'])):
        info_format['firstname'].append(info['firstname'][i])
        info_format['lastname'].append(info['lastname'][i])
        info_format['fullname'].append('{} {}'.format(info['firstname'][i], info['lastname'][i]))
        info_format['wk 1-16']['spent'].append(info['spent:wk 1-16'][i])
        info_format['wk 1-16']['earned'].append(info['earned:wk1-16'][i])
        info_format['wk 17-22']['spent'].append(info['spent:wk 17-22'][i])
        info_format['wk 17-22']['earned'].append(info['earned:wk17-22'][i])

    return info_format

 
def add_all_past_purchases(p_file=past_purchases_file):
    p_info = _get_past_purchases_info(p_file)

    for i in range(len(p_info['fullname'])):
        if Purchase.objects.filter(student__full_name=p_info['fullname'][i]):
            print('past purchase already found for {}'.format(p_info['fullname'][i]))
            print(Purchase.objects.filter(student__full_name=p_info['fullname'][i]))
            continue
        
        else:
            # wk 1-16
            # print(p_info['fullname'])
            # print(Student.objects.filter(full_name=p_info['fullname'][i]))
            newp = Purchase(student=Student.objects.get(full_name=p_info['fullname'][i]),
                            business=Business.objects.get(name='wk 1-16'),
                            amount=round(float(p_info['wk 1-16']['spent'][i]), 2),
                            student_earned=round(float(p_info['wk 1-16']['earned'][i]), 2),
                            school_earned=round(float(p_info['wk 1-16']['earned'][i]), 2) )
            newp.save()
            
            print('saved {} with {} - {}, {}, {}'.format(newp.student,
                                                         newp.business,
                                                         newp.amount,
                                                         newp.student_earned,
                                                         newp.school_earned))

            # wk 17-22
            newp = Purchase(student=Student.objects.get(full_name=p_info['fullname'][i]),
                            business=Business.objects.get(name='wk 17-22'),
                            amount=round(float(p_info['wk 17-22']['spent'][i]), 2),
                            student_earned=round(float(p_info['wk 17-22']['earned'][i]), 2),
                            school_earned=round(float(p_info['wk 17-22']['earned'][i]), 2) )
            newp.save()

            print('saved {} with {} - {}, {}, {}'.format(newp.student,
                                                         newp.business,
                                                         newp.amount,
                                                         newp.student_earned,
                                                         newp.school_earned))



    # for i in range(len(p_info['fullname'])):
    #     for key, val in p_info.items():
    #         if isinstance(val, dict):
    #             item = 'spent'
    #         else:
    #             item = i
    #         print('{}: {}'.format(key, val[item]))




## Add all Students in students.csv
def _get_student_info(s_file):
    file_path = os.path.join(location, s_file)
    with open(file_path, 'r') as sfile:
        info_raw = [line.strip('\n') for line in sfile\
                    if line.strip() and line.strip() != '\n']

    headers_raw = info_raw.pop(0)
    headers = [i.strip().lower() for i in headers_raw.split(',')]
    info = {key:[] for key in headers}
    for line in info_raw:
        line_items = line.split(',')
        for i, key in enumerate(headers):
            info[key].append(line_items[i].strip().lower())

    info['fullname'] = []
    for i in range(len(info['firstname'])):
        info['fullname'].append('{} {}'.format(info['firstname'][i], info['lastname'][i]))

    #return {'name':['james']}
    return info


def add_all_students(s_file=students_file):
    s_info = _get_student_info(s_file)

    #firstname, lastname, phone, homeroom, adults
    for line in range(len(s_info['fullname'])):
        first = s_info['firstname'][line] if s_info['firstname'][line] != 'none' else None 
        last = s_info['lastname'][line] if s_info['lastname'][line] != 'none' else None
        namelast = last if not last else ''
        full = '{} {}'.format(first, namelast)
        phone = s_info['phone'][line] if s_info['phone'][line] != 'none' else None
        homeroom = s_info['homeroom'][line] if s_info['homeroom'][line] != 'none' else None
        adults = [i.strip() for i in s_info['adults'][line].split(':')] if s_info['adults'][line] != 'none' else None
        
        if Student.objects.filter(full_name=s_info['fullname'][line]):
            print('{:>20} already in db'.format(s_info['fullname'][line]))
            continue
        else: 
            new_s = Student(full_name=full,
                            first_name=first,
                            last_name=last,
                            phone=phone,
                            homeroom=homeroom,
                            adults=adults)
            new_s.save()

            print('added {:>20} to db'.format(full))

    #for key, val in s_info.items():
    #    print('\n{}:\n{}'\
    #            .format(key, '\n'.join(val)))


## Add all businesses in businesses.csv
def _get_business_info(b_file):
    file_path = os.path.join(location, b_file)
    with open(file_path, 'r') as bfile:
        info_raw = [line.strip('\n') for line in bfile \
                    if line.strip() and line.strip() != '\n']

    headers_raw = info_raw.pop(0)
    headers = [i.strip().lower() for i in headers_raw.split(',')]
    info = {key:[] for key in headers}

    for line in info_raw:
        line_items = line.split(',')
        for i, key in enumerate(headers):
            if key == 'amounts':
                items = line_items[i].split(':')
                if len(items) > 1:
                    items = [j for j in items[:]]
                info[key].append(items)
            else:
                info[key].append(line_items[i])
    
    return info


def add_all_businesses(b_file=business_file):
    b_info = _get_business_info(b_file)

    # name, percentage, amounts
    for line in range(len(b_info['name'])):
        if Business.objects.filter(name=b_info['name'][line]):
            print('{:>15} already in db'.format(b_info['name'][line]))
            continue
        else:
            # print('\n------------')
            # print(b_info['name'][line])
            # print(b_info['percentage'][line])
            # print(b_info['amounts'][line])
            if b_info['percentage'][line].lower() != 'none':
                perc = round(float(b_info['percentage'][line]), 2)
            else:
                perc = None
            if b_info['amounts'][line][0].lower() != 'none':
                amnt = [round(float(i), 2) for i in b_info['amounts'][line]]
            else:
                amnt = None
            
            new_b = Business(name=b_info['name'][line],
                             percentage=perc,
                             amounts=amnt)
            new_b.save()
            print('{:>50} added'.format(b_info['name'][line]))

    # for key, val in b_info.items():
    #     print('\n{}:\n{}'\
    #           .format(key, '\n'.join([', '.join(i) if isinstance(i, list) else i\
    #                                                for i in val])))
 
