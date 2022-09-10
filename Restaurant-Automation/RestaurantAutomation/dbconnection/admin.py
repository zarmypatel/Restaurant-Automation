from django.contrib import admin

# Register your models here.
from .models import Chef
from .models import MenuItem
from .models import Staff

admin.site.register(Chef)
admin.site.register(MenuItem)
admin.site.register(Staff)