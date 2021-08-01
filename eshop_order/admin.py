from django.contrib import admin

# Register your models here.


from .models import Order ,OrderDetail , Discount



class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__','order_number','owner','is_paiy','jpublish']
    list_filter = ['is_paiy']
    search_fields = ['id']
    class Meta:
        model=Order

admin.site.register(Order,OrderAdmin)

class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['__str__','order','product','price','count']
    class Meta:
        model=OrderDetail

admin.site.register(OrderDetail ,OrderDetailAdmin)

class DiscountAdmin(admin.ModelAdmin):
    list_display = ['__str__','percentage','total','count','active']
    class Meta:
        model=Discount

admin.site.register(Discount ,DiscountAdmin)