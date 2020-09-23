from django.contrib import admin

# Register your models here.
from .models import notes_api_model

admin.site.register(notes_api_model)