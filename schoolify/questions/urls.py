from django.urls import path

from schoolify.questions.views import QuestionCreateView, QuestionListView

urlpatterns = (
    path('create/', QuestionCreateView.as_view(), name='question create'),
    path('all/', QuestionListView.as_view(), name='questions all'),
)