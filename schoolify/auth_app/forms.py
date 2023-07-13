from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from schoolify.auth_app.models import Profile
from schoolify.auth_app.validators import validate_capitalized, validate_school_year_range

UserModel = get_user_model()


class SignUpForm(UserCreationForm):
    MAX_FIRST_NAME = 15
    MAX_LAST_NAME = 15
    first_name = forms.CharField(
        max_length=MAX_FIRST_NAME,
        validators=(validate_capitalized,),
    )
    last_name = forms.CharField(
        max_length=MAX_LAST_NAME,
        validators=(validate_capitalized,),
    )
    school_grade = forms.IntegerField(
        validators=(validate_school_year_range,),
    )

    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password1', 'password2', 'first_name', 'last_name', 'school_grade')

    def save(self, commit=True):
        user = super().save(commit=commit)

        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        school_grade = self.cleaned_data['school_grade']
        profile = Profile(
            first_name=first_name,
            last_name=last_name,
            school_grade=school_grade,
        )
        if commit:
            profile.save()
        return user

