from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from schoolify.auth_app.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('auth/', include('schoolify.auth_app.urls')),
    path('assignment/', include('schoolify.assignment.urls')),
    path('questions/', include('schoolify.questions.urls')),
    path('books/', include('schoolify.book.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# http://127.0.0.1:8000/auth/sign-up/ --> hide field widgets
# http://127.0.0.1:8000/auth/profile/details/32/ - cannot add picture + school_grade doesn't have validation