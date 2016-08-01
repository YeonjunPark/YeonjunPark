import re, sqlite3
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'programming.settings')
from django.forms import ValidationError
from django.core.validators import MinLengthValidator
from django.utils.deconstruct import deconstructible
import sys
from poketmongo.models import Zipcode


@deconstructible
class MinLengthValidator(object):
    def __init__(self, min_length):
        self.min_length = min_length

    def __call__(self, value):
        if len(value) < self.min_length:
            raise ValidationError('{}글자 이상 입력해주세요.'.format(self.min_length))

def phone_number_validator(value):
    '휴대폰 번호를 검사하는 Validator'
    if not re.match(r'^01[016789][1-9]\d{6,7}$', value):
        # if not re.match(r'^\d$', value):
        raise ValidationError('휴대폰 번호를 입력해주세요.')

def zip_code_validator(zip_code):
    '우편번호를 검사하는 Validator'
    if not re.match(r'^\d{3}-\d{3}$', zip_code):
        if not re.match(r'^\d{5}$', zip_code):
            raise ValidationError('우편번호를 입력해주세요.')
    if not Zipcode.objects.filter(zipcode=zip_code).exists():
        raise ValidationError('존재하는 우편번호가 아닙니다.')

def lnglat_validator(lnglat):
    if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$', lnglat):
        raise ValidationError('Invalid LngLat Type')