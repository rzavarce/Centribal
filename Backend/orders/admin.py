from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Orders, OrderDetail


class ProductsInline(admin.TabularInline):
    model = OrderDetail
    extra = 1


class OrdersAdmin(SimpleHistoryAdmin):

    list_display = ('reference', 'price_total_tax',
                    'created_date')

    search_fields = ('reference', 'price_total_tax',
                     'created_date')

    list_filter = ('reference', 'price_total_tax',
                   'created_date')

    inlines = (ProductsInline,)

    ordering = ('reference', 'price_total_tax', 'created_date',)

    readonly_fields = ('reference', 'created_date', 'modified_date',)
    """
    fieldsets = (
        (None, {
            'fields': ('reference', )
        }),
    )
    """


admin.site.register(Orders, OrdersAdmin)
