from django import forms
from blog.models import Comment

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message', 'author', 'jjal']

class CommentForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
    author = forms.CharField()
    jjal = forms.ImageField()

    def save(self, commit=True):
        comment = Comment(message=self.cleaned_data['message'], author=self.cleaned_data['author'], jjal=self.cleaned_data['jjal'])
        if commit:
            comment.save()
        return comment