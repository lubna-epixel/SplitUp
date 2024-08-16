from django.urls import path
from .views import (
    LoginPage,LogoutPage,RegistrationPage,DashboardView
)
urlpatterns = [
    path('login/',LoginPage.as_view(),name='login'),
    path('registration/',RegistrationPage.as_view(),name='registration'),
    path('logout/',LogoutPage.as_view(),name='logout'),
    path('dashboard/',DashboardView.as_view(),name='dashboard')
]