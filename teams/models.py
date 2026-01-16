from cms.models.pluginmodel import CMSPlugin
from django.conf import settings
from django.db import models
from django.utils.text import slugify

from filer.fields.image import FilerImageField


class Team(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField(blank=True)
    team_leads = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="led_teams",
        blank=True,
    )
    image = FilerImageField(
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="team_images",
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    teams = models.ManyToManyField(
        Team,
        related_name="members",
        blank=True,
    )
    image = FilerImageField(
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="user_profile_images",
    )
    short_bio = models.TextField(blank=True)
    telephone = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username}"


class TeamPluginModel(CMSPlugin):
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="plugins",
    )

    def __str__(self):
        return self.team.name


class UserPluginModel(CMSPlugin):
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="plugins",
    )

    def __str__(self):
        return str(self.user_profile)
