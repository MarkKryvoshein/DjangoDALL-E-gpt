
from django.urls import path
from .views import mainPage, signUp

urlpatterns = [
    path('', mainPage),
    path('signup', signUp, name='signup')
]
