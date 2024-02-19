from django.contrib import admin
from . models import Product,Order_item
admin.site.register(Product)


class OrderItemTubularinline(admin.TabularInline):
    model=Order_item

class OrderAdmin(admin.ModelAdmin):
    inlines=[OrderItemTubularinline]


from . models import slider
admin.site.register(slider)


from . models import Contact
admin.site.register(Contact)


from . models import Electronics
admin.site.register(Electronics)


from . models import Baner
admin.site.register(Baner)


from . models import Order
admin.site.register(Order,OrderAdmin)
# Register your models here.



