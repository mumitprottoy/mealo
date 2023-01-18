from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.landing, name='landing'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('loggedout', LogoutView.as_view(template_name='entrance/logout.html'), name='logout'),
]
