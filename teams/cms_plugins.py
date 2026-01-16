from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import TeamPluginModel, UserPluginModel


@plugin_pool.register_plugin
class TeamPlugin(CMSPluginBase):
    model = TeamPluginModel
    name = "Team"
    render_template = "teams/plugins/team.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context["team"] = instance.team
        context["team_leads"] = instance.team.team_leads.all()
        return context


@plugin_pool.register_plugin
class UserPlugin(CMSPluginBase):
    model = UserPluginModel
    name = "User"
    render_template = "teams/plugins/user.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context["user_profile"] = instance.user_profile
        return context
