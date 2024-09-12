from django.contrib import admin
from .models import Channel, Movie, User
from django.conf import settings


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('channel_id', 'name', 'url')

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'genre', 'language', 'code')



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('telegram_id', 'username')
