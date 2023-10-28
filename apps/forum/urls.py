from django.urls import path

from apps.forum.views import index

urlpatterns = [
    path('', index, name="forum")
]
