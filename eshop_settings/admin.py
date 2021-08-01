from django.contrib import admin
from .models import SiteSetting ,SiteImageSetting
# Register your models here.

class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ['__str__','phone','mobile','email']
    class Meta:
        model=SiteSetting

admin.site.register(SiteSetting,SiteSettingAdmin)
admin.site.register(SiteImageSetting)