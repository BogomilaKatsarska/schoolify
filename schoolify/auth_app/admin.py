from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from schoolify.auth_app.forms import SignUpForm
from schoolify.auth_app.models import AppUser

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    ordering = ('personal_number',)
    list_display = [AppUser.USERNAME_FIELD, 'date_joined', 'last_login']
    readonly_fields = ["date_joined", "last_login"]
    list_filter = ('date_joined',)
    search_fields = ("personal_number", )
    add_form = SignUpForm
    #TODO: check petstagram form =
    fieldsets = (
        (None, {'fields': ('personal_number', 'password')}),
        ('Permissions', {
            'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("personal_number", "password1", "password2"),
            },
        ),
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("first_name", "last_name", "school_grade"),
            },
        ),
    )

