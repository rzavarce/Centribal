from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Products


class ProductsAdmin(SimpleHistoryAdmin):

    list_display = ('reference', 'name', 'price', 'tax', 'status',
                    'created_date')

    search_fields = ('reference', 'name', 'price', 'tax', 'status',
                     'created_date')

    list_filter = ('reference', 'name', 'price', 'tax', 'status',
                   'created_date')

    ordering = ('name', 'status', 'created_date',)

    readonly_fields = ('created_date', 'modified_date',)


admin.site.register(Products, ProductsAdmin)
