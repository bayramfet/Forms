from django.urls import path
from .views import *

urlpatterns = [
    path('view_simple/', view_simple, name='view_simple'),
    path('view_template/', view_template, name='view_template'),
    path('view_template_form/', view_template_form, name='view_template_form'),
]