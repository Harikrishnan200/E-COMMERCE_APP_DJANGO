from django.contrib import admin
from orders.models import Order,OrderedItem

class OrderAdmin(admin.ModelAdmin):   # to customize the default admin in Order
    list_filter = [
        "owner",
        "order_status"
    ]

    search_fields = [
        "owner",
        "id"
    ]

admin.site.register(Order,OrderAdmin)  #here change the default admin class and pass the customized admin class named OrderAdmin