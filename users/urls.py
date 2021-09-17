"""Define padrões de URL para users"""
from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views


urlpatterns = [
    # Página de login
    url(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),

    # Página de logout
    url(r'^logout/$', views.logout_view, name='logout'),

    # Página de cadastro
    url(r'^register/$', views.register, name='register'),
]
