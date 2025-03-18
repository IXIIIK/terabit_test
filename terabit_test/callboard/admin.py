from django.contrib import admin
from .models import Advertisment, Requests, Comments, Category

# Register your models here.
admin.site.register(Advertisment)
admin.site.register(Requests)
admin.site.register(Comments)
admin.site.register(Category)
