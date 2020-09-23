from django.db import models

# Create your models here.
class notes_api_model(models.Model):
    title = models.CharField(max_length=128, null=True)
    content = models.CharField(max_length=512, null=True)

    def __str__(self):
        return self.title
