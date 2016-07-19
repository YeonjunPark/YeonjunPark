from django.db import models
from django.core.exceptions import ValidationError

class User(models.Model):
    male ='M'
    female = 'F'

    sex = ((male, 'Male'), (female, 'Female'),)

    name = models.CharField(max_length=50, unique=True, help_text='50자 이내로 영어, 한글, 숫자만 입력하세요.',
        # validators=[
            # validators.RegexValidator(
            #     r'^[a-zA-Z"ㄱ-힣\d]+$',
            #     ('잘못된 이름입니다. 영어, 한글, 숫자만 입력하세요.')
            # ),
        # ],
        error_messages={
            'unique': ("동일한 이름이 존재합니다. 다시 입력하세요"),
        },
    )
    age = models.PositiveSmallIntegerField(null=False)
    sex = models.CharField(max_length = 1, choices = sex, default = male)
    email = models.EmailField(blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Poketmon(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=50)
    level = models.PositiveSmallIntegerField(default=1, null=False)

class Capture(models.Model):
    user = models.ForeignKey(User)
    poketmon = models.ForeignKey(Poketmon)
    location = models.CharField(max_length = 100)
