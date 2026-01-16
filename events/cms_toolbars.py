from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from cms.utils.urlutils import admin_reverse


@toolbar_pool.register
class EventsToolbar(CMSToolbar):
    def populate(self):
        menu = self.toolbar.get_or_create_menu(
            key="events",
            verbose_name="Events",
        )

        menu.add_sideframe_item(
            name="Events",
            url=admin_reverse("events_event_changelist"),
        )

        menu.add_modal_item(
            name="Add Event",
            url=admin_reverse("events_event_add"),
        )
