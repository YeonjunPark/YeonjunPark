import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'programming.settings')
import django
django.setup()

from poketmongo.models import Zipcode
import re

f = open("new_서울특별시.txt", 'r')

zipcode = f.readlines()
zipcode_list = []

for i in zipcode:
    zipcode_list.append(Zipcode(zipcode=i))

Zipcode.objects.bulk_create(zipcode_list, 100)

f.close()
