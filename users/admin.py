from __future__ import unicode_literals

from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import UserProfile


class UserAdmin(SimpleHistoryAdmin):
    """User admin."""

    list_display = ('pk', 'username', 'email', 'status', 'type_user',)
    list_display_links = ('pk', 'username', 'email',)

    search_fields = (
        'email',
        'username',
        'first_name',
        'last_name',
    )

    list_filter = (
        'is_active',
        'is_staff',
        'type_user',
        'created_date',
        'modified_date',
    )

    ordering = ('email', 'status',)

    readonly_fields = ('created_date', 'modified_date',)


admin.site.register(UserProfile, UserAdmin)
