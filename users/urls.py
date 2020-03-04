from django.urls import path
from rest_framework import routers

from users import views

urlpatterns = [
    path('login/', views.login_view),
    path('create-account/', views.create_account_view),
]