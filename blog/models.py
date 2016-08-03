import re
from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from .validators import MinLengthValidator, lnglat_validator, ZipCodeValidator
from .fields import PhoneNumberField, ZipCodeField


'''
def min_length_validator(min_lentgh):
    def wrap(value):
        if len(value) < min_lentgh:
            raise ValidationError('{}글자 이상 입력해주세요.'.format(min_lentgh))
    return wrap

def max_length_validator(max_length):
    def wrap(value):
        if len(value) > max_length:
            raise ValidationError('{}글자 이하로 입력해주세요.'.format(max_length))
    return wrap
'''
# class MinLengthValidator(object):
#     def __init__(self, min_length):
#         self.min_length = min_length

#     def __call__(self, value):
#         if len(value) < min_length:
     # raise ValidationError('{}글자 이상 입력해주세요.'.format(min_length)) 이렇게 해도 되지만 .validators 에서 import 해서 하는 것이 좋다. 이유는 모델들과 validators 가 같이 있으면 보기 안좋으니까


class Post(models.Model):
    title = models.CharField(max_length=100, validators=[MinLengthValidator(4)], verbose_name='제목')
    content = models.TextField(help_text='Markdown 문법을 써주세요.', validators=[MinLengthValidator(10)])
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50,
        validators=[lnglat_validator],
        help_text='경도,위도 포맷으로 입력')
    created_at = models.DateTimeField(default=timezone.now)
    test_field = models.IntegerField(default=10)
    tag_set = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('Post')
    message = models.TextField()
    author = models.CharField(max_length=20)

    def __str__(self):
        return self.message

class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=20, validators=[ZipCodeValidator(True)])
    phone_number = PhoneNumberField()

    def __str__(self):
        return self.name

class Zipcode(models.Model):
    zipcode = ZipCodeField()

    def __str__(self):
        return self.zipcode








