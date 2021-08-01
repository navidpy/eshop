from django.contrib import admin
from .models import ContactUs ,CommentsProduct


# Register your models here.


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'full_name', 'email', 'is_read']
    list_filter = ['is_read']
    list_editable = ['is_read']
    search_fields = ['subject', 'full_name', 'text']

    class Meta:
        model = ContactUs


admin.site.register(ContactUs, ContactUsAdmin)


class CommentsProductAdmin(admin.ModelAdmin):
    list_display = ['user','product', 'jpublish', 'accepted']
    list_filter = ['accepted']
    list_editable = ['accepted']
    # search_fields = [ 'full_name']

    class Meta:
        model = CommentsProduct


admin.site.register(CommentsProduct, CommentsProductAdmin)
