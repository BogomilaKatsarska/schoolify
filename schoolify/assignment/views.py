from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView

from schoolify.assignment.forms import AssignmentCookingCreateForm
from schoolify.assignment.models import AssignmentCooking, AssignmentMathematics, AssignmentEnglish, AssignmentMusic


#TODO: make prepopulated school_subject field


class AssignmentCookingCreateView(LoginRequiredMixin, CreateView):
    template_name = 'assignment/assignment-cooking-create.html'
    model = AssignmentCooking
    #TODO: DISABLE SUBJECT FOR EDIT - fix assignment
    fields = ('recipe_name', 'dish_image', 'ingredients', 'preparation_time', 'assignment_name')
    success_url = reverse_lazy('assignment cooking list')

    def form_valid(self, form):
        form.instance.school_subject = AssignmentCooking.COOKING
        form.instance.submitted_by = self.request.user

        return super().form_valid(form)


class AssignmentMathematicsCreateView(LoginRequiredMixin, CreateView):
    template_name = 'assignment/assignment-mathematics-create.html'
    model = AssignmentMathematics
    fields = ('assignment_name', 'solution',)
    success_url = reverse_lazy('assignment mathematics list')

    def form_valid(self, form):
        form.instance.school_subject = AssignmentMathematics.MATHEMATICS

        return super().form_valid(form)


class AssignmentEnglishCreateView(LoginRequiredMixin, CreateView):
    template_name = 'assignment/assignment-english-create.html'
    model = AssignmentEnglish
    fields = ('assignment_name', 'essay', 'external_resources_used',)
    success_url = reverse_lazy('assignment english list')

    def form_valid(self, form):
        form.instance.school_subject = AssignmentEnglish.ENGLISH

        return super().form_valid(form)


class AssignmentMusicCreateView(LoginRequiredMixin, CreateView):
    template_name = 'assignment/assignment-music-create.html'
    model = AssignmentMusic
    fields = ('assignment_name', 'song',)
    success_url = reverse_lazy('assignment music list')

    def form_valid(self, form):
        form.instance.school_subject = AssignmentMusic.MUSIC

        return super().form_valid(form)


class AssignmentMusicListView(LoginRequiredMixin, ListView):
    model = AssignmentMusic
    template_name = 'assignment/assignment-music-list.html'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('assignment_name')
        return queryset


class AssignmentMathematicsListView(LoginRequiredMixin, ListView):
    model = AssignmentMathematics
    template_name = 'assignment/assignment-mathematics-list.html'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('assignment_name')
        return queryset


class AssignmentEnglishListView(LoginRequiredMixin, ListView):
    model = AssignmentEnglish
    template_name = 'assignment/assignment-english-list.html'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('assignment_name')
        return queryset


class AssignmentCookingListView(LoginRequiredMixin, ListView):
    model = AssignmentCooking
    template_name = 'assignment/assignment-cooking-list.html'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('assignment_name')
        return queryset


class AssignmentMusicDeleteView(LoginRequiredMixin, DeleteView):
    model = AssignmentMusic
    template_name = "assignment/assignment-music-delete.html"
    success_url = reverse_lazy('assignment music list')


class AssignmentEnglishDeleteView(LoginRequiredMixin, DeleteView):
    model = AssignmentEnglish
    template_name = "assignment/assignment-english-delete.html"
    success_url = reverse_lazy('assignment english list')


class AssignmentMathematicsDeleteView(LoginRequiredMixin, DeleteView):
    model = AssignmentMathematics
    template_name = "assignment/assignment-mathematics-delete.html"
    success_url = reverse_lazy('assignment mathematics list')


class AssignmentCookingDeleteView(LoginRequiredMixin, DeleteView):
    model = AssignmentCooking
    template_name = "assignment/assignment-cooking-delete.html"
    success_url = reverse_lazy('assignment cooking list')


class AssignmentMusicEditView(LoginRequiredMixin, UpdateView):
    model = AssignmentMusic
    template_name = "assignment/assignment-music-edit.html"
    fields = '__all__'
    success_url = reverse_lazy('assignment music list')


class AssignmentEnglishEditView(LoginRequiredMixin, UpdateView):
    model = AssignmentEnglish
    template_name = "assignment/assignment-english-edit.html"
    fields = '__all__'
    success_url = reverse_lazy('assignment english list')


class AssignmentMathematicsEditView(LoginRequiredMixin, UpdateView):
    model = AssignmentMathematics
    template_name = "assignment/assignment-mathematics-edit.html"
    fields = '__all__'
    success_url = reverse_lazy('assignment mathematics list')


class AssignmentCookingEditView(LoginRequiredMixin, UpdateView):
    model = AssignmentCooking
    template_name = "assignment/assignment-cooking-edit.html"
    fields = '__all__'
    success_url = reverse_lazy('assignment cooking list')


class AssignmentMusicDetailsView(LoginRequiredMixin, DetailView):
    model = AssignmentMusic
    template_name = "assignment/assignment-music-details.html"


class AssignmentEnglishDetailsView(LoginRequiredMixin, DetailView):
    model = AssignmentEnglish
    template_name = "assignment/assignment-english-details.html"


class AssignmentMathematicsDetailsView(LoginRequiredMixin, DetailView):
    model = AssignmentMathematics
    template_name = "assignment/assignment-mathematics-details.html"


class AssignmentCookingDetailsView(LoginRequiredMixin, DetailView):
    model = AssignmentCooking
    template_name = "assignment/assignment-cooking-details.html"


