""" Url router for the periodic table module
"""
from django.conf.urls import url
from core_module_periodic_table_app.views import PeriodicTableModule

urlpatterns = [
    url(r'module-periodic-table', PeriodicTableModule.as_view(), name='core_module_periodic_table_view'),
]
