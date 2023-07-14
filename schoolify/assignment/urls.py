from django.urls import path, include

from schoolify.assignment.views import AssignmentCookingCreateView, AssignmentMusicCreateView, \
    AssignmentEnglishCreateView, AssignmentMathematicsCreateView, AssignmentMathematicsListView, \
    AssignmentEnglishListView, AssignmentMusicListView, AssignmentCookingListView

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
)