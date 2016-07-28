import re
from django.forms import ValidationError

def valiate_phone_number(number):
    if re.match(r'^01[016789][1-9]\d{6,7}$', number):
        return True
    return False

def phone_number_validator(value):
    if not re.match(r'^01[016789][1-9]\d{6,7}$', value):
        raise ValidationError('{}글자 이상 입력해주세요.'.format(min_lentgh))

print(valiate_phone_number('01012312343'))  # True
print(valiate_phone_number('0101231123'))  # True
print(valiate_phone_number('010123112')) # False
print(valiate_phone_number('0101231234a')) # False
