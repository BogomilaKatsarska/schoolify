from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from schoolify.assignment.forms import AssignmentEnglishEditForm, AssignmentMusicEditForm, \
    AssignmentMathematicsEditForm, AssignmentCookingEditForm
from schoolify.assignment.models import AssignmentCooking, AssignmentMathematics, AssignmentEnglish, AssignmentMusic


class AssignmentCookingCreateView(LoginRequiredMixin, CreateView):
    template_name = 'assignment/assignment-cooking-create.html'
    model = AssignmentCooking
    fields = ('recipe_name', 'dish_image', 'ingredients', 'preparation_time', 'assignment_name')
    success_url = reverse_lazy('assignment cooking list')

    def form_valid(self, form):
        form.instance.school_subject = AssignmentCooking.COOKING
        form.instance.created_by = self.request.user

        return super().form_valid(form)


class AssignmentMathematicsCreateView(LoginRequiredMixin, CreateView):
    template_name = 'assignment/assignment-mathematics-create.html'
    model = AssignmentMathematics
    fields = ('assignment_name', 'solution',)
    success_url = reverse_lazy('assignment mathematics list')

    def form_valid(self, form):
        form.instance.school_subject = AssignmentMathematics.MATHEMATICS
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class AssignmentEnglishCreateView(LoginRequiredMixin, CreateView):
    template_name = 'assignment/assignment-english-create.html'
    model = AssignmentEnglish
    fields = ('assignment_name', 'essay', 'external_resources_used',)
    success_url = reverse_lazy('assignment english list')

    def form_valid(self, form):
        form.instance.school_subject = AssignmentEnglish.ENGLISH
        form.instance.created_by = self.request.user

        return super().form_valid(form)


class AssignmentMusicCreateView(LoginRequiredMixin, CreateView):
    template_name = 'assignment/assignment-music-create.html'
    model = AssignmentMusic
    fields = ('assignment_name', 'song',)
    success_url = reverse_lazy('assignment music list')

    def form_valid(self, form):
        form.instance.school_subject = AssignmentMusic.MUSIC
        form.instance.created_by = self.request.user

        return super().form_valid(form)


class AssignmentMusicListView(LoginRequiredMixin, ListView):
    model = AssignmentMusic
    template_name = 'assignment/assignment-music-list.html'
    paginate_by = 3
    extra_context = {
        'assignmentmusics_count': AssignmentMusic.objects.count(),
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('assignment_name')
        return queryset


class AssignmentMathematicsListView(LoginRequiredMixin, ListView):
    model = AssignmentMathematics
    template_name = 'assignment/assignment-mathematics-list.html'
    paginate_by = 3
    extra_context = {
        'assignmentmathematics_count': AssignmentMathematics.objects.count(),
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('assignment_name')
        return queryset


class AssignmentEnglishListView(LoginRequiredMixin, ListView):
    model = AssignmentEnglish
    template_name = 'assignment/assignment-english-list.html'
    paginate_by = 3
    extra_context = {
        'assignmentenglish_count': AssignmentEnglish.objects.count(),
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('assignment_name')
        return queryset


class AssignmentCookingListView(LoginRequiredMixin, ListView):
    model = AssignmentCooking
    template_name = 'assignment/assignment-cooking-list.html'
    paginate_by = 3
    extra_context = {
        'assignmentcooking_count': AssignmentCooking.objects.count(),
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('assignment_name')
        return queryset


class AssignmentMusicDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = AssignmentMusic
    template_name = "assignment/assignment-music-delete.html"
    success_url = reverse_lazy('assignment music list')

    def test_func(self):
        assignment_obj = self.get_object()
        user_obj = self.request.user
        if assignment_obj.created_by == user_obj:
            return True
        return False


class AssignmentEnglishDeleteView(LoginRequiredMixin, UserPassesTestMixin,  DeleteView):
    model = AssignmentEnglish
    template_name = "assignment/assignment-english-delete.html"
    success_url = reverse_lazy('assignment english list')

    def test_func(self):
        assignment_obj = self.get_object()
        user_obj = self.request.user
        if assignment_obj.created_by == user_obj:
            return True
        return False


class AssignmentMathematicsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = AssignmentMathematics
    template_name = "assignment/assignment-mathematics-delete.html"
    success_url = reverse_lazy('assignment mathematics list')

    def test_func(self):
        assignment_obj = self.get_object()
        user_obj = self.request.user
        if assignment_obj.created_by == user_obj:
            return True
        return False


class AssignmentCookingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = AssignmentCooking
    template_name = "assignment/assignment-cooking-delete.html"
    success_url = reverse_lazy('assignment cooking list')

    def test_func(self):
        assignment_obj = self.get_object()
        user_obj = self.request.user
        if assignment_obj.created_by == user_obj:
            return True
        return False


class AssignmentMusicEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = AssignmentMusic
    form_class = AssignmentMusicEditForm
    template_name = "assignment/assignment-music-edit.html"
    success_url = reverse_lazy('assignment music list')

    def test_func(self):
        assignment_obj = self.get_object()
        user_obj = self.request.user
        if assignment_obj.created_by == user_obj:
            return True
        return False


class AssignmentEnglishEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = AssignmentEnglish
    form_class = AssignmentEnglishEditForm
    template_name = "assignment/assignment-english-edit.html"
    success_url = reverse_lazy('assignment english list')

    def test_func(self):
        assignment_obj = self.get_object()
        user_obj = self.request.user
        if assignment_obj.created_by == user_obj:
            return True
        return False


class AssignmentMathematicsEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = AssignmentMathematics
    form_class = AssignmentMathematicsEditForm
    template_name = "assignment/assignment-mathematics-edit.html"
    success_url = reverse_lazy('assignment mathematics list')

    def test_func(self):
        assignment_obj = self.get_object()
        user_obj = self.request.user
        if assignment_obj.created_by == user_obj:
            return True
        return False


class AssignmentCookingEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = AssignmentCooking
    form_class = AssignmentCookingEditForm
    template_name = "assignment/assignment-cooking-edit.html"
    success_url = reverse_lazy('assignment cooking list')

    def test_func(self):
        assignment_obj = self.get_object()
        user_obj = self.request.user
        if assignment_obj.created_by == user_obj:
            return True
        return False


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
