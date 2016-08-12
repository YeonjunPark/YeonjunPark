from django import forms
from django.forms import Textarea
from blog.models import Comment

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message', 'jjal']
        widgets = {
        'message': Textarea(attrs={'cols': 40, 'rows': 2}),
    }

class CommentForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
    author = forms.CharField()
    jjal = forms.ImageField(required=False)

    def save(self, commit=True):
        comment = Comment(message=self.cleaned_data['message'], author=self.cleaned_data['author'], jjal=self.cleaned_data['jjal'])
        if commit:
            comment.save()
        return comment

class CommentForm2(forms.Form):
    message = forms.CharField(widget=forms.Textarea) # 클래스만 넘겨줘도 되고 인스턴스를 넘겨줘도 된다.
    author = forms.CharField()
    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop('instance', None)
        super(CommentForm2, self).__init__(*args, **kwargs) # super().__init__(*args, **kwargs)도 지원한다.(파이썬 3)
        if self.instance:
            self.fields['message'].initial = self.instance.message
            self.fields['author'].initial = self.instance.author
        else:
            self.instance = Comment()

    def save(self, commit=True):
        self.instance.message = self.cleaned_data['message']
        self.instance.author = self.cleaned_data['author']
        if commit:
            self.instance.save()
        return self.instance
