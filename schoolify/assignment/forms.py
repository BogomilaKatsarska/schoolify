from django import forms

from schoolify.assignment.models import AssignmentCooking, AssignmentEnglish, AssignmentMathematics, AssignmentMusic

class AssignmentEnglishBaseForm(forms.ModelForm):
    class Meta:
        model = AssignmentEnglish
        fields = '__all__'


class AssignmentEnglishCreateForm(AssignmentEnglishBaseForm):
    pass


class AssignmentEnglishEditForm(AssignmentEnglishBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['school_subject'].disabled = True


class AssignmentCookingBaseForm(forms.ModelForm):
    class Meta:
        model = AssignmentCooking
        fields = '__all__'


class AssignmentCookingCreateForm(AssignmentCookingBaseForm):
    pass


class AssignmentCookingEditForm(AssignmentCookingBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['school_subject'].disabled = True


class AssignmentMathematicsBaseForm(forms.ModelForm):
    class Meta:
        model = AssignmentMathematics
        fields = '__all__'


class AssignmentMathematicsCreateForm(AssignmentMathematicsBaseForm):
    pass


class AssignmentMathematicsEditForm(AssignmentMathematicsBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['school_subject'].disabled = True


class AssignmentMusicBaseForm(forms.ModelForm):
    class Meta:
        model = AssignmentMusic
        fields = '__all__'


class AssignmentMusicCreateForm(AssignmentMusicBaseForm):
    pass


class AssignmentMusicEditForm(AssignmentMusicBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['school_subject'].disabled = True
