from django.contrib import admin
from .models import Order, OrderProduct

# Register your models here.


class OrderProductInlineAdmin(admin.TabularInline):
    model = OrderProduct
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [OrderProductInlineAdmin]
    list_display = ["user", "order_date", "is_active"]
    list_filter = ["is_active"]
    search_fields = ["user__username"]


admin.site.register(Order, OrderAdmin)
