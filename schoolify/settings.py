"""
pip freeze > requirements.txt
1:48 starts abstractbaseuser
2:20 starts AppUser Admin
2:45 - lecture to continue

Django settings for schoolify project.

Generated by 'django-admin startproject' using Django 3.2.20.

"""
import os
from pathlib import Path

from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-*w7rzs_u7$cqg^r59px-7v7-m1#_8j@tghhx$q9c*%=24v#auz'

DEBUG = True
ALLOWED_HOSTS = [
    '127.0.0.1',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'schoolify.auth_app',
    'schoolify.assignment',
    'schoolify.questions',
    'schoolify.book',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'schoolify.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'schoolify.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'schoolify_db',
        'USER': 'postgres',
        'PASSWORD': 'Bogi1995',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'auth_app.AppUser'

LOGIN_URL = reverse_lazy('index')
LOGIN_REDIRECT_URL = reverse_lazy('index')
LOGOUT_REDIRECT_URL = reverse_lazy('sign in')

# STATIC_ROOT = '/tmp/schoolify/staticfiles'

STATIC_URL = 'static/'

STATICFILES_DIRS = (
    BASE_DIR / 'staticfiles',
)

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'mediafiles'


#TODO: fix mediafiles
#extra_context --> static context
#template_name
#model
#modelform_factory
# def get_context_data - method, which returns context --> dynamic context
#       context = super().get_context_data(**kwargs)
#       context['employees'] = Employee.objects.all()
#       return context
#get_queryset
#object_list when we use ListView
#CTRL + TAB -> to switch between diff files
#form_class
# def get_form()

# def get_form(self, form_class = None):
#     form = super().get_form(form_class=form_class)
#     for name, field in form.fields.items():
#         field.widgets.attrs['placeholder'] = 'Enter ' + name
#     return form

# def get_form_class(self):
#     --> dynamic way go do form_class = EmployeeCreateForm

# def get_absolute_url():
#     pass

# def get_success_url(self):
#     created_object = self.object
#     return reverse_lazy('employee details', kwargs={
#         'pk':created_object.pk,
#     })

# dispatch() -->decides whether to get/post; we override it when we want to change access

# def dispatch(self, request, *args, **kwargs):
#     if profile to update is the same as user logged in => continue
#     else:
#         401, unauthorized
#     return dispatch(request, args, **kwargs)
#
#
# def get_object():
#     pass
#
# def get_object_list():
#     pass

#with alt we can mark many rows in diff places


'''
GIT COMMANDS:
git clone git@github.com:BogomilaKatsarska/pet_stagram.git --> clones what is in GitHub to your local
git pull --> takes the changes from GitHub repo and applies them to yours
git status --> show the newly created files on your pc
git add to_delete.txt --> adds files that we would like to commit to github. Should be followed by git commit
git add . --> adds the current directory
git commit -m "added to_delete files"((-m means message)) --> commit locally
git push --> adds to GitHub
'''
#TODO: check GitHub and GitBash
#TODO: env should not be included in GitHub