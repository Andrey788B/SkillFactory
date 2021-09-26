from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class News(models.Model):

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

    name = models.CharField(
        max_length=50,
        unique=True,
    )
    description = models.TextField()

    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='news',
    )
    time = models.CharField(validators=[MinValueValidator(0.0)], max_length=50, blank=True, )

    def __str__(self):
        return f'{self.name.title()}: {self.description[:100]}'

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/news/{self.id}'


class Category(models.Model):

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name.title()}'

class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    first_name = forms.CharField(label = "Имя")
    last_name = forms.CharField(label = "Фамилия")

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2", )


