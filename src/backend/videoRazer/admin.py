from django.contrib import admin

from .models import Profile, Video


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    model = Video