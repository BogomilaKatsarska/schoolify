from django import forms

from schoolify.assignment.models import AssignmentCooking, AssignmentEnglish, AssignmentMathematics, AssignmentMusic


class AssignmentCookingCreateForm(forms.ModelForm):
    class Meta:
        model = AssignmentCooking
        fields = '__all__'
        widgets = {
            'assignment_name': forms.TextInput(
                attrs={
                    'placeholder': 'Please fill in the name of your assignment as per homework.',
                }
            ),
            'recipe_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name',
                }
            ),
            'dish_image': forms.ImageField(
                attrs={
                    'placeholder': 'Please upload a picture of your dish.',
                }
            ),
            'ingredients': forms.TextInput(
                attrs={
                    'placeholder': 'Please fill in the ingredients of your dish.',
                }
            ),
            'preparation_time': forms.DateField(
                attrs={
                    'placeholder': 'Please fill in the full reparation time, together with cooking time.',
                }
            ),
        }


class AssignmentEnglishCreateForm(forms.ModelForm):
    class Meta:
        model = AssignmentEnglish
        fields = '__all__'
        widgets = {
            'assignment_name': forms.TextInput(
                attrs={
                    'placeholder': 'Please fill in the name of your assignment as per homework.',
                }
            ),
            'essay': forms.TextInput(
                attrs={
                    'placeholder': 'Please write your essay here.',
                }
            ),
            'external_resources_used': forms.URLInput(
                attrs={
                    'placeholder': 'Please list the URL of the external resource used for your essay.',
                }
            ),
        }


class AssignmentMathematicsCreateForm(forms.ModelForm):
    class Meta:
        model = AssignmentMathematics
        fields = '__all__'
        widgets = {
            'assignment_name': forms.TextInput(
                attrs={
                    'placeholder': 'Please fill in the name of your assignment as per homework.',
                }
            ),
            'solution': forms.TextInput(
                attrs={
                    'placeholder': 'Please write your solution here.',
                }
            ),
        }


class AssignmentMusicCreateForm(forms.ModelForm):
    class Meta:
        model = AssignmentMusic
        fields = '__all__'
        widgets = {
            'assignment_name': forms.TextInput(
                attrs={
                    'placeholder': 'Please fill in the name of your assignment as per homework.',
                }
            ),
            'song': forms.FileField(
                attrs={
                    'placeholder': 'Please upload your song here.',
                }
            ),
        }