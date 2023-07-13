from django.urls import path, include

from schoolify.assignment.views import AssignmentCookingCreateView

urlpatterns = (
    path('cooking/', include([
        path('create/', AssignmentCookingCreateView.as_view(), name='assignment cooking create'),
    ])),
)