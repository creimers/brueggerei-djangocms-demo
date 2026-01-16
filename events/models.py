from datetime import datetime

from cms.models.pluginmodel import CMSPlugin
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from filer.fields.image import FilerImageField
from recurrence.fields import RecurrenceField

from teams.models import Team


class Event(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    organizing_team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="events",
    )
    organizing_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="organized_events",
    )
    location = models.CharField(max_length=255, default="Brüggerei")
    short_description = models.TextField(blank=True)
    full_description = models.TextField(blank=True)
    image = FilerImageField(
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="event_images",
    )
    auto_advertise = models.BooleanField(default=True)
    recurrences = RecurrenceField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            # Ensure unique slug
            original_slug = self.slug
            counter = 1
            while Event.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    def get_next_occurrence(self):
        """Get the next occurrence date from the recurrence field."""
        now = timezone.now()
        dtstart = datetime(2020, 1, 1, 0, 0, 0, tzinfo=now.tzinfo)
        return self.recurrences.after(now, inc=True, dtstart=dtstart)


class UpcomingEventsPluginModel(CMSPlugin):
    number_of_events = models.PositiveIntegerField(default=3)

    def __str__(self):
        return f"Upcoming Events ({self.number_of_events})"
