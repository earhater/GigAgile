from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Space)
admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(Sprint)
admin.site.register(Stage)