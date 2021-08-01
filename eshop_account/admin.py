from django.contrib import admin

# Register your models here.

from .models import UserInformation ,ForgetPassword



class UserInformationAdmin(admin.ModelAdmin):
    list_display = ['__str__','phone']
    class Meta:
        model=UserInformation

admin.site.site_header = "پنل ادمین سایت"
admin.site.register(UserInformation,UserInformationAdmin)
