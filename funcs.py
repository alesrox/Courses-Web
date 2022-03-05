from airtable import *
from config import *

def falsename():
    for page in datatable.get_iter():
        for record in page:
            value = record['fields']['id']
            if value == 1:
                falsename = record['fields']['Name']
                return falsename

def get_logo():
    for page in datatable.get_iter():
        for record in page:
            value = record['fields']['id']
            if value == 1:
                value = record['fields']['Logo']
                alpha = str(value)
                start_url = alpha.find('url') + 7
                end_url = alpha.find('.png') + 4
                url = alpha[start_url:end_url]
                return url

def get_logo_white():
    for page in datatable.get_iter():
        for record in page:
            value = record['fields']['id']
            if value == 1:
                value = record['fields']['Logo White']
                alpha = str(value)
                start_url = alpha.find('url') + 7
                end_url = alpha.find('.png') + 4
                url = alpha[start_url:end_url]
                return url