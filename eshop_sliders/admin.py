from django.contrib import admin

# Register your models here.
from .models import Slider



# class productAdmin(admin.ModelAdmin):
#     list_display = ['__str__','link','price','active']
#     class Meta:
#         model=Slider


admin.site.register(Slider)