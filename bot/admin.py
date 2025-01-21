from django.contrib import admin
from .models import InfoText, TelegramUser


@admin.register(InfoText)
class InfoTextAdmin(admin.ModelAdmin):
    list_display = ("id", "text")


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ("telegram_id", "first_interaction")
