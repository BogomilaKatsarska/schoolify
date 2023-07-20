from django.urls import path

from schoolify.questions.views import QuestionCreateView

urlpatterns = (
    path('create/', QuestionCreateView.as_view(), name='question create'),
)