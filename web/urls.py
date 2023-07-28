from django.urls import path
from . import views

urlpatterns = [
#    path('', views.HomePage.as_view(), name="HomePage"),
    path('', views.Products_View.as_view(), name="Products"),
    path('submit/user/', views.NewUser, name="new_user")
]