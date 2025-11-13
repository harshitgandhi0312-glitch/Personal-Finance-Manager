from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login_page),
    path('signup/',views.signup_page),
    path('logout/', views.logout),
    path('home/', views.show_home_page),
]