from django.contrib import admin

# Register your models here.
from .models import Blog



class BlogAdmin(admin.ModelAdmin):
    list_display = ['__str__','writer','jpublish','active','visit_count']
    class Meta:
        model=Blog

admin.site.register(Blog,BlogAdmin)
