from django.contrib import admin

from spaceapp.models import KeplerUser, Font


@admin.register(KeplerUser)
class ConstAdmin(admin.ModelAdmin):
    list_display = ("user_name", "font")


@admin.register(Font)
class ConstAdmin(admin.ModelAdmin):
    list_display = ("font_name",)
