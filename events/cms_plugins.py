from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import Event, UpcomingEventsPluginModel


@plugin_pool.register_plugin
class UpcomingEventsPlugin(CMSPluginBase):
    model = UpcomingEventsPluginModel
    name = "Upcoming Events"
    render_template = "events/plugins/upcoming_events.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context["events"] = Event.objects.all()[: instance.number_of_events]
        return context
