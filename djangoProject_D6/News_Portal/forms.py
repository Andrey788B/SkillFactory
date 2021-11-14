from django.forms import ModelForm
from .models import News, Contact
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django import forms


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['name', 'description', 'category', 'time']


class CommonSignupForm(SignupForm):

    def save(self, request):
        user = super(CommonSignupForm, self).save(request)
        basic_group = Group.objects.get(name='Common')
        basic_group.user_set.add(user)
        return user


class ContactForm(forms.ModelForm):
        """форма подписки по email"""
        """captcha = ReCaptchaField(public_key='76wtgdfsjhsydt7r5FFGFhgsdfytd656sad75fgh',
            private_key='98dfg6df7g56df6gdfgdfg65JHJH656565GFGFGs',
        )"""

        class Meta:
            model = Contact
            fields = ("email",)
            widgets = {
                "email": forms.TextInput(attrs={"class": "editContent", "placeholder": "Your Email..."})
            }
            labels = {
                "email": ""
            }