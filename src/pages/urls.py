from django.urls import path

from .views import frontPage, logIn, signUp, loggedUser, logOut

urlpatterns = [
    path('', frontPage, name='home'),
    path('login', logIn, name='login'),
    path('signup', signUp, name='signup'),
    path('user', loggedUser, name='user'),
    path('logout', logOut, name='logout')
]
