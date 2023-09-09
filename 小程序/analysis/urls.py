from django.urls import path, include
from .views import show
urlpatterns = [
   path('analysis_templates/<str:report_link>/', show, name='analysis_template'),
]