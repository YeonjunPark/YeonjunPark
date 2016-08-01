import re
from django.db import models
from .validators import phone_number_validator, zip_code_validator

class PhoneNumberField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 20)
        kwargs.setdefault('validators', [])
        kwargs['validators'].append(phone_number_validator)
        super().__init__(*args, **kwargs)

class ZipCodeField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 7)
        kwargs.setdefault('validators', [])
        kwargs['validators'].append(zip_code_validator)
        super().__init__(*args, **kwargs)