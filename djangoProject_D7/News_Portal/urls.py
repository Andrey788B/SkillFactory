from django.urls import path
from django.views.generic import TemplateView
from .views import AllNewsList, NewsDetail, Filters, AdNews, NewsUpdate, NewsDelete, BaseRegisterView, IndexView, Upgrade_me, MyView, ContactView, AppointmentView, IndexViewC
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='flatpages/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='flatpages/logout.html'), name='logout'),
    path('', AllNewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view()),
    path('search/', Filters.as_view(), name="flatpages/search.html"),
    path('adnews/', AdNews.as_view(), name="flatpages/adnews.html"),
    path('update/<int:pk>', NewsUpdate.as_view(), name='news_update'),
    path('delete/<int:pk>', NewsDelete.as_view(), name='news_delete'),
    path('login/', LoginView.as_view(template_name='flatpages/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='flatpages/logout.html'), name='logout'),
    path('signup/', BaseRegisterView.as_view(template_name='flatpages/signup.html'), name='signup'),
    path('index/', IndexView.as_view(template_name='flatpages/index.html'), name='index'),
    path('upgrade/', Upgrade_me, name='upgrade'),
    path('view/', MyView.as_view()),
    path("", ContactView.as_view(), name="contact"),
    path('appointment/', AppointmentView.as_view(template_name='flatpages/make_appointment.html'), name='appointment'),
    path('', IndexViewC.as_view()),


]