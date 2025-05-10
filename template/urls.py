
from django.contrib import admin
from django.urls import path, include

from training_app.views import mainPage, signUp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('training_app.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]
