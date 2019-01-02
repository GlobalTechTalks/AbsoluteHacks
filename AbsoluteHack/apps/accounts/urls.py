from django.conf.urls import url,path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.userLoginView , name = 'login')
    path('signin/', views.userSignupView , name = 'signin')
    path('logout/', views.userLoginView , name = 'logout')
    path('checkLogin/' , views.isUserLoggedIn , name = 'check-login')
]