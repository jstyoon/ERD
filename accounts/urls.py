from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.signup_view, name='sign-up'),
    path('sign-in/', views.login_view, name='sign-in'),
    path('logout/', views.logout_view, name='logout'),
]