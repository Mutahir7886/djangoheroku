from django.contrib import admin

from .models import Bio_data,Education,Experience,Project

# Register your models here.

admin.site.register(Bio_data)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Project)
