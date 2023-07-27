from django.contrib import admin

from schoolify.assignment.models import AssignmentCooking, AssignmentMusic, AssignmentEnglish, AssignmentMathematics


@admin.register(AssignmentCooking)
class AssignmentCookingAdmin(admin.ModelAdmin):
    pass


@admin.register(AssignmentMathematics)
class AssignmentMathematicsAdmin(admin.ModelAdmin):
    pass


@admin.register(AssignmentEnglish)
class AssignmentEnglishAdmin(admin.ModelAdmin):
    pass


@admin.register(AssignmentMusic)
class AssignmentMusicAdmin(admin.ModelAdmin):
    pass
