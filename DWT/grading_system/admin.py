from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Subject)
admin.site.register(Class)
admin.site.register(Test)
admin.site.register(AssignedPupil)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'email', 'password', 'first_name', 'last_name', 'user_type']