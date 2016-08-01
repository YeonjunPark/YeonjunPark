import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'programming.settings')
import django
django.setup()

from poketmongo.models import Zipcode
import re

f = open("new_서울특별시.txt", 'r')
# print(zipcode)
zipcode = f.readlines()
zipcode_list = []
for i in zipcode:
    zipcode_list.append(Zipcode(zipcode=i))
    # zipcodes = [ Zipcode(zipcode=i)]
# zipcodes.append(Zipcode(zipcode=zipcode[-1])
# print(zipcodes)

Zipcode.objects.bulk_create(zipcode_list)
# Zipcode.objects.all().delete()
f.close()
