from django.contrib import admin
from home.models import University, Department, Year, DepName

# Register your models here.

admin.site.register(University)
admin.site.register(Department)
admin.site.register(Year)
admin.site.register(DepName)
