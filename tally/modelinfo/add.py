from ..models import Student, Business, Purchase
import os

location = os.path.dirname(os.path.realpath(__file__))
business_file = 'businesses.csv'
students_file = 'students.csv'

def show_location():
    print(location)


def _get_student_info(s_file):
    file_path = os.path.join(location, s_file)

    return {'name':['james']}


def add_all_students(s_file=students_file):
    s_info = _get_student_info(s_file)

    for key, val in s_info.items():
        print('\n{}:\n{}'\
                .format(key, '\n'.join(val)))


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
            new_b = Business(name=b_info['name'][line],
                             percentage=round(float(b_info['percentage'][line]), 2),
                             amounts=[round(float(i), 2) for i in b_info['amounts'][line]])
            new_b.save()
            print('{:>50} added'.format(b_info['name'][line]))

    # for key, val in b_info.items():
    #     print('\n{}:\n{}'\
    #           .format(key, '\n'.join([', '.join(i) if isinstance(i, list) else i\
    #                                                for i in val])))
 
