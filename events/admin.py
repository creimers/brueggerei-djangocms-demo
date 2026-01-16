from django.contrib import admin

from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "organizing_team",
        "organizing_user",
        "location",
        "start_time",
        "end_time",
        "auto_advertise",
    ]
    list_filter = ["organizing_team", "auto_advertise"]
    search_fields = ["title", "short_description", "full_description", "location"]
    prepopulated_fields = {"slug": ("title",)}
    autocomplete_fields = ["organizing_team", "organizing_user"]
    fieldsets = [
        (None, {"fields": ["title", "slug", "image"]}),
        (
            "Organization",
            {"fields": ["organizing_team", "organizing_user", "location"]},
        ),
        ("Description", {"fields": ["short_description", "full_description"]}),
        (
            "Schedule",
            {"fields": ["start_time", "end_time", "recurrences"]},
        ),
        ("Settings", {"fields": ["auto_advertise"]}),
    ]
