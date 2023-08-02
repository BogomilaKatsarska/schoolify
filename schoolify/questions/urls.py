from django.urls import path

from schoolify.questions.views import QuestionCreateView, QuestionListView, answer_functionality, QuestionEditView, \
    QuestionDeleteView, AnswerEditView, AnswerDeleteView

urlpatterns = (
    path('create/', QuestionCreateView.as_view(), name='question create'),
    path('all/', QuestionListView.as_view(), name='questions all'),
    path('edit/<int:pk>/', QuestionEditView.as_view(), name='question edit'),
    path('delete/<int:pk>/', QuestionDeleteView.as_view(), name='question delete'),
    path('answer/<int:question_id>', answer_functionality, name="answer"),
    path('edit-answer/<int:question_id>/<int:pk>/', AnswerEditView.as_view(), name="edit answer"),
    path('delete-answer/<int:question_id>/<int:pk>/', AnswerDeleteView.as_view(), name="delete answer"),
)