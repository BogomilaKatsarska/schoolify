from django.urls import path, include

from schoolify.auth_app.views import SignUpView, SignInView, SignOutView, ProfileEditView, ProfileDetailsView, \
    ProfileDeleteView

urlpatterns = (
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-out/', SignOutView.as_view(), name='sign out'),
    path('profile/', include([
        path('details/<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
        path('edit/<int:pk>/', ProfileEditView.as_view(), name='profile edit'),
        path('delete/<int:pk>/', ProfileDeleteView.as_view(), name='profile delete'),
    ])),
)
