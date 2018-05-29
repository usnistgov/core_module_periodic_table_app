core_module_periodic_table_app
==============================

Periodic Table module for the parser core project.

Quick start
===========

1. Add "core_module_periodic_table_app" to your INSTALLED_APPS setting
----------------------------------------------------------------------

.. code:: python

    INSTALLED_APPS = [
      ...
      'core_module_periodic_table_app',
    ]

2. Include the core_module_periodic_table_app URLconf in your project urls.py
-----------------------------------------------------------------------------

.. code:: python

    url(r'^', include('core_module_periodic_table_app.urls')),