from django.urls import path

from schoolify.questions.views import QuestionCreateView, QuestionListView, answer_functionality

urlpatterns = (
    path('create/', QuestionCreateView.as_view(), name='question create'),
    path('all/', QuestionListView.as_view(), name='questions all'),
    path('answer/<int:question_id>', answer_functionality, name="answer"),
)