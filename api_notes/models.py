from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class notes_api_model(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=128, null=True)
    author = models.CharField(max_length=128, null=True)
    content = models.CharField(max_length=512, null=True)

    def __str__(self):
        return str(self.user)
