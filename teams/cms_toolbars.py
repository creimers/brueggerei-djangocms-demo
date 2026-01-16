from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from cms.utils.urlutils import admin_reverse


@toolbar_pool.register
class TeamsToolbar(CMSToolbar):
    def populate(self):
        menu = self.toolbar.get_or_create_menu(
            key="teams",
            verbose_name="Teams",
        )

        menu.add_sideframe_item(
            name="Users",
            url=admin_reverse("auth_user_changelist"),
        )

        menu.add_sideframe_item(
            name="Teams",
            url=admin_reverse("teams_team_changelist"),
        )
