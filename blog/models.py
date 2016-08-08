import re, os
from uuid import uuid4
from django.core.urlresolvers import reverse
from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from .validators import MinLengthValidator, lnglat_validator, ZipCodeValidator
from .fields import PhoneNumberField, ZipCodeField
from django.core.files import File
from django.db.models.signals import pre_save
from blog.utils import square_image, thumbnail

def random_name_upload_to(instance, filename):
    name = uuid4().hex
    extension = os.path.splitext(filename)[-1].lower()
    return os.path.join(name[:3], name[3:6], name[6:] + extension)

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
    # tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50,
        validators=[lnglat_validator],
        help_text='경도,위도 포맷으로 입력')
    created_at = models.DateTimeField(auto_now_add=True)
    test_field = models.IntegerField(default=10)
    tag_set = models.ManyToManyField('Tag', blank=True)
    photo = models.ImageField(blank=True, upload_to=random_name_upload_to)

    def get_absolute_url(self):
       return reverse('blog:post_detail', args=[self.pk])

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('Post')
    message = models.TextField()
    author = models.CharField(max_length=20)
    jjal = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

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


def pre_on_post_save(sender, **kwargs):
    post = kwargs['instance']
    if post.photo:
        max_width = 300
        if post.photo.width > max_width or post.photo.height > max_width:
            processed_file = thumbnail(post.photo.file, max_width, max_width)
            # processed_file = square_image(post.image.file, max_width)
            post.photo.save(post.photo.name, File(processed_file))

pre_save.connect(pre_on_post_save, sender=Post)








