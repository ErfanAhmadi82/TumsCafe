from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
#    path('', views.HomePage.as_view(), name="HomePage"),
    path('', views.Type_View.as_view(), name="Products"),
    path('submit/user/', views.NewUser, name="new_user"),
    path('accounts/', include("django.contrib.auth.urls")),
]