from django.contrib import admin

from schoolify.assignment.models import AssignmentCooking, AssignmentMusic, AssignmentEnglish, AssignmentMathematics


@admin.register(AssignmentCooking)
class AssignmentCookingAdmin(admin.ModelAdmin):
    ordering = ('assignment_name',)
    list_display = ['assignment_name', 'created_by']
    search_fields = ("assignment_name",)


@admin.register(AssignmentMathematics)
class AssignmentMathematicsAdmin(admin.ModelAdmin):
    ordering = ('assignment_name',)
    list_display = ['assignment_name', 'created_by']
    search_fields = ("assignment_name",)


@admin.register(AssignmentEnglish)
class AssignmentEnglishAdmin(admin.ModelAdmin):
    ordering = ('assignment_name',)
    list_display = ['assignment_name', 'created_by']
    search_fields = ("assignment_name",)


@admin.register(AssignmentMusic)
class AssignmentMusicAdmin(admin.ModelAdmin):
    ordering = ('assignment_name',)
    list_display = ['assignment_name', 'created_by']
    search_fields = ("assignment_name",)
