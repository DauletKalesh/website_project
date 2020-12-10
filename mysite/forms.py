# coding=utf-8
from django import forms
from mysite.models import Profile, Post


class RegisterForm(forms.Form):
    username = forms.CharField(label=u"Username")
    first_name = forms.CharField(label=u"Name")
    last_name = forms.CharField(label=u"Surname")
    email = forms.EmailField(label=u"Email", required=False)
    password = forms.CharField(label=u"Password", widget=forms.PasswordInput)
    password_confirm = forms.CharField(label=u"Confirm password", widget=forms.PasswordInput)

    def is_valid(self):
        valid = super(RegisterForm, self).is_valid()
        if 'password' in self.cleaned_data and 'password_confirm' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password_confirm']:
                self.add_error("password_confirm", u"Password don't match")
                return False
            elif len(self.cleaned_data['password']) < 5:
                self.add_error('password', u"Password is too short")
        return valid


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author']
