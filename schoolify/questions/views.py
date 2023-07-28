from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from schoolify.questions.forms import AnswerForm, QuestionForm
from schoolify.questions.models import Question


class QuestionCreateView(LoginRequiredMixin, CreateView):
    template_name = 'questions/questions.html'
    form_class = QuestionForm
    success_url = reverse_lazy('questions all')

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)


class QuestionListView(LoginRequiredMixin, ListView):
    template_name = 'questions/questions.html'
    model = Question
    paginate_by = 4
    extra_context = {
        'question_form': QuestionForm(),
        'answerform': AnswerForm(),
        'all_questions': Question.objects.all(),
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-created_on')

        pattern = self.__get_pattern()
        if pattern:
            queryset = queryset.filter(question__icontains=pattern.lower())

        return queryset

    def __get_pattern(self):
        return self.request.GET.get('pattern', None)


@login_required
def answer_functionality(request, question_id):
    question = Question.objects.get(pk=question_id)

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():

            new_answer_instance = form.save(commit=False)
            new_answer_instance.user_id = request.user.pk
            new_answer_instance.to_question = question
            new_answer_instance.save()

        return redirect(request.META['HTTP_REFERER'] + f"#{question_id}")
