""" Periodic table module view
"""

from core_parser_app.tools.modules.views.builtin.popup_module import (
    AbstractPopupModule,
)
from core_parser_app.tools.modules.views.module import AbstractModule


class PeriodicTableModule(AbstractPopupModule):
    """Periodic Table Module"""

    def __init__(self):
        AbstractPopupModule.__init__(
            self,
            button_label="Select Element",
            styles=["core_module_periodic_table_app/css/periodic.css"],
            scripts=["core_module_periodic_table_app/js/periodic.js"],
        )

    def _retrieve_data(self, request):
        """Retrieve module's data

        Args:
            request:

        Returns:

        """
        data = ""
        if request.method == "GET":
            if "data" in request.GET:
                data = request.GET["data"]
        elif request.method == "POST":
            if "selectedElement" in request.POST:
                data = request.POST["selectedElement"]
        return data

    def _render_data(self, request):
        """Return module's data rendering

        Args:
            request:

        Returns:

        """
        if len(self.data) > 0:
            return "Chosen element: " + self.data

        return "No selected element."

    def _get_popup_content(self):
        """Return module's data rendering"""
        selected_elements = [self.data]
        template = AbstractModule.render_template(
            "core_module_periodic_table_app/periodic.html",
            {"selected_elements": selected_elements},
        )
        return AbstractModule.render_template(
            "core_module_periodic_table_app/periodic_simple.html",
            {"periodic_table": template},
        )
