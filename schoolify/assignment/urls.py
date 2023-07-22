from django.urls import path, include

from schoolify.assignment.views import AssignmentCookingCreateView, AssignmentMusicCreateView, \
    AssignmentEnglishCreateView, AssignmentMathematicsCreateView, AssignmentMathematicsListView, \
    AssignmentEnglishListView, AssignmentMusicListView, AssignmentCookingListView, AssignmentCookingDeleteView, \
    AssignmentMusicDeleteView, AssignmentEnglishDeleteView, AssignmentMathematicsDeleteView, AssignmentCookingEditView, \
    AssignmentMusicEditView, AssignmentEnglishEditView, AssignmentMathematicsEditView, AssignmentCookingDetailsView, \
    AssignmentMusicDetailsView, AssignmentMathematicsDetailsView, AssignmentEnglishDetailsView

urlpatterns = (
    path('create/', include([
        path('cooking/', AssignmentCookingCreateView.as_view(), name='assignment cooking create'),
        path('music/', AssignmentMusicCreateView.as_view(), name='assignment music create'),
        path('english/', AssignmentEnglishCreateView.as_view(), name='assignment english create'),
        path('mathematics/', AssignmentMathematicsCreateView.as_view(), name='assignment mathematics create'),
    ])),
    path('list/', include([
            path('cooking/', AssignmentCookingListView.as_view(), name='assignment cooking list'),
            path('music/', AssignmentMusicListView.as_view(), name='assignment music list'),
            path('english/', AssignmentEnglishListView.as_view(), name='assignment english list'),
            path('mathematics/', AssignmentMathematicsListView.as_view(), name='assignment mathematics list'),
    ])),
    path('delete/', include([
            path('cooking/<int:pk>/', AssignmentCookingDeleteView.as_view(), name='assignment cooking delete'),
            path('music/<int:pk>/', AssignmentMusicDeleteView.as_view(), name='assignment music delete'),
            path('english/<int:pk>/', AssignmentEnglishDeleteView.as_view(), name='assignment english delete'),
            path('mathematics/<int:pk>/', AssignmentMathematicsDeleteView.as_view(), name='assignment mathematics delete'),
    ])),
    path('edit/', include([
            path('cooking/<int:pk>/', AssignmentCookingEditView.as_view(), name='assignment cooking edit'),
            path('music/<int:pk>/', AssignmentMusicEditView.as_view(), name='assignment music edit'),
            path('english/<int:pk>/', AssignmentEnglishEditView.as_view(), name='assignment english edit'),
            path('mathematics/<int:pk>/', AssignmentMathematicsEditView.as_view(), name='assignment mathematics edit'),
    ])),
    path('details/', include([
            path('cooking/<int:pk>/', AssignmentCookingDetailsView.as_view(), name='assignment cooking details'),
            path('music/<int:pk>/', AssignmentMusicDetailsView.as_view(), name='assignment music details'),
            path('english/<int:pk>/', AssignmentEnglishDetailsView.as_view(), name='assignment english details'),
            path('mathematics/<int:pk>/', AssignmentMathematicsDetailsView.as_view(), name='assignment mathematics details'),
    ])),
)