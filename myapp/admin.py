# myapp/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile,Member

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile Info'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile)

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    # Admin table me dikhne wale columns
    list_display = ('name', 'mobile', 'location', 'blood_donate', 'zimmedar_name','profession','joined_at')
    
    # Search bar enable karne ke liye
    search_fields = ('name', 'mobile', 'zimmedar_name', 'blood_donate')
    
    # Filter sidebar enable karne ke liye
    list_filter = ('location', 'joined_at')