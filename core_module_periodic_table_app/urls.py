""" Url router for the periodic table module
"""

from django.urls import re_path

from core_module_periodic_table_app.views import PeriodicTableModule

urlpatterns = [
    re_path(
        r"module-periodic-table",
        PeriodicTableModule.as_view(),
        name="core_module_periodic_table_view",
    ),
]
