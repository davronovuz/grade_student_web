from django.contrib import admin
from .models import CustomUser,Subject,Grade,Teacher,Student


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display =["username","first_name","last_name","user_type"]
    search_fields = ["username","first_name","last_name"]
    list_filter = ["user_type"]





