from django import forms

from blog.models import Comments, Contact


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('message',)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
