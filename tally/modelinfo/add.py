from ..models import Student, Business, Purchase
import os

location = os.path.dirname(os.path.realpath(__file__))
business_file = 'businesses.csv'

def show_location():
    print(location)


def _get_bus_info(b_file):
    file_path = os.path.join(location, b_file)
    with open(file_path, 'r') as bfile:
        info_raw = [line.strip('\n') for line in bfile if line.strip() and line.strip() != '\n']

    headers_raw = info_raw.pop(0)
    headers = [i.strip().lower() for i in headers_raw.split(',')]
    info = {key:[] for key in headers}
    for line in info_raw:
        line_items = line.split(',')
        for i, key in enumerate(headers):
            items = line_items[i].split(':')
            if len(items) > 1:
                items = [j for j in items[:]]
            info[key].append(items)
            #print(i, key, items)
    return info


def add_all_businesses(b_file=business_file):
    b_info = _get_bus_info(b_file)
    
    for key, val in b_info.items():
        print('\n{}:\n{}'.format(key, '\n'.join([', '.join(i) if isinstance(i, list) else i for i in val])))
       
