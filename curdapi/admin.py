from django.contrib import admin

from curdapi.models import Category
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
