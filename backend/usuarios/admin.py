# UD5.1.d
from django.contrib import admin
from .models import MyUser

# Register your models here.
class MyUserAdmin(admin.ModelAdmin):
    list_display = list_display_links = ('email', 'username', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'username')
    preserve_filters = True
    
admin.site.register(MyUser, MyUserAdmin)