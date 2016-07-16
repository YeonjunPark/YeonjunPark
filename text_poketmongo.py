import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'programming.settings')
import django
django.setup()

from poketmongo.models import User
from poketmongo.models import Poketmon
