from django.contrib import admin

from apps.forum.models import *

admin.site.register(Question)
admin.site.register(Answer)
