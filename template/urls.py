
from django.contrib import admin
from django.urls import path

from training_app.views import registration_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', registration_form)
]
