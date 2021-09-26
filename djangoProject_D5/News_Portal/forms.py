from django.forms import ModelForm
from .models import News
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group

# Создаём модельную форму
class NewsForm(ModelForm):
    # в класс мета, как обычно, надо написать модель, по которой будет строится форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = News
        fields = ['name', 'description', 'category', 'time']


class CommonSignupForm(SignupForm):

    def save(self, request):
        user = super(CommonSignupForm, self).save(request)
        basic_group = Group.objects.get(name='Common')
        basic_group.user_set.add(user)
        return user