from django import forms

from schoolify.assignment.models import AssignmentCooking, AssignmentEnglish, AssignmentMathematics, AssignmentMusic


class AssignmentCookingCreateForm(forms.ModelForm):
    class Meta:
        model = AssignmentCooking
        fields = '__all__'



class AssignmentEnglishCreateForm(forms.ModelForm):
    class Meta:
        model = AssignmentEnglish
        fields = '__all__'



class AssignmentMathematicsCreateForm(forms.ModelForm):
    class Meta:
        model = AssignmentMathematics
        fields = '__all__'


class AssignmentMusicCreateForm(forms.ModelForm):
    class Meta:
        model = AssignmentMusic
        fields = '__all__'
