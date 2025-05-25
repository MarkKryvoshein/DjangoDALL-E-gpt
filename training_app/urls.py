
from django.urls import path
from .views import mainPage, signUp, logOut

urlpatterns = [
    path('', mainPage),
    path('signup', signUp, name='signup'),
    path('logout', logOut, name='logout')
]
