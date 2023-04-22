from django import forms

from blog.models import Comments


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('message',)
