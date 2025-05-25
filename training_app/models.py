from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)

    def __str__(self):
        return self.username

class QueryHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='query_histories')
    query = models.TextField()
    response_text = models.TextField()
    response_image = models.ImageField(upload_to="training_app/img", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __self__(self):
        return f"Запит був від {self.user.username} - {self.created_at.strftime("%d.%m.%Y %H:%M:%S")}"
