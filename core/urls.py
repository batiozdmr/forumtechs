from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("apps.forum.urls"), name="index"),
    path('admin/', admin.site.urls),
]
