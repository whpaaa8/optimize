from django.urls import path, include
from .views import collect_list, write_collection, add_collection, test_1

urlpatterns = [
   path('list/', collect_list),
   path('write', write_collection),
   path('add', add_collection),
   path('test', test_1),
]
