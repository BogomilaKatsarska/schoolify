from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from schoolify.auth_app.forms import SignUpForm

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    #TODO: admin does not work properly - can't edit existing users and add new ones
    ordering = ('personal_number',)
    list_display = ['personal_number', 'date_joined', 'last_login']
    list_filter = ()
    #TODO: try below when admin is working
    #list_filter = ('school_grade')
    #search_fields = ("personal_number__startswith", )
    add_form = SignUpForm
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
