from django.contrib import admin
from .models import Task
from .models import Tag


admin.site.register(Task)
admin.site.register(Tag)
