""" Module periodic table testing
"""
from unittest.case import TestCase

from django.http.request import HttpRequest
from unittest.mock import patch

from core_module_periodic_table_app.views import PeriodicTableModule


class TestPeriodicTableModuleRetrieveData(TestCase):
    """Test Periodic Table Module Retrieve Data"""

    @patch(
        "core_parser_app.tools.modules.views.module.AbstractModule.render_template"
    )
    def test_periodic_table_module_retrieve_data_returns_element_if_data_given(
        self, render_template
    ):
        """test_periodic_table_module_retrieve_data_returns_element_if_data_given"""

        # Arrange
        request = HttpRequest()
        element = "AC"
        request.method = "GET"
        request.GET = {
            "data": element,
        }
        my_module = PeriodicTableModule()
        # Act
        result = my_module._retrieve_data(request)
        self.assertEqual(True, result == element)

    @patch(
        "core_parser_app.tools.modules.views.module.AbstractModule.render_template"
    )
    def test_periodic_table_module_retrieve_data_returns_empty_if_no_data_given(
        self, render_template
    ):
        """test_periodic_table_module_retrieve_data_returns_empty_if_no_data_given"""

        # Arrange
        request = HttpRequest()
        request.method = "GET"
        request.GET = {}
        my_module = PeriodicTableModule()
        # Act
        result = my_module._retrieve_data(request)
        self.assertEqual(True, result == "")

    @patch(
        "core_parser_app.tools.modules.views.module.AbstractModule.render_template"
    )
    def test_periodic_table_module_retrieve_data_returns_element_if_selected_data_given(
        self, render_template
    ):
        """test_periodic_table_module_retrieve_data_returns_element_if_selected_data_given"""

        # Arrange
        request = HttpRequest()
        element = "AC"
        request.method = "POST"
        request.POST = {
            "selectedElement": element,
        }
        my_module = PeriodicTableModule()
        # Act
        result = my_module._retrieve_data(request)
        self.assertEqual(True, result == element)

    @patch(
        "core_parser_app.tools.modules.views.module.AbstractModule.render_template"
    )
    def test_periodic_table_module_retrieve_data_returns_empty_if_no_selected_data_given(
        self, render_template
    ):
        """test_periodic_table_module_retrieve_data_returns_empty_if_no_selected_data_given"""

        # Arrange
        request = HttpRequest()
        request.method = "POST"
        request.POST = {}
        my_module = PeriodicTableModule()
        # Act
        result = my_module._retrieve_data(request)
        self.assertEqual(True, result == "")


class TestPeriodicTableModuleRenderData(TestCase):
    """Test Periodic Table Module Render Data"""

    @patch(
        "core_parser_app.tools.modules.views.module.AbstractModule.render_template"
    )
    def test_periodic_table_module_render_data_returns_the_chosen_element_if_given(
        self, render_template
    ):
        """test_periodic_table_module_render_data_returns_the_chosen_element_if_given"""

        # Arrange
        request = HttpRequest()
        element = "AC"
        my_module = PeriodicTableModule()
        my_module.data = element
        # Act
        result = my_module._render_data(request)
        self.assertEqual(True, result == "Chosen element: " + element)

    @patch(
        "core_parser_app.tools.modules.views.module.AbstractModule.render_template"
    )
    def test_periodic_table_module_render_data_returns_no_selected_element_if_not_given(
        self, render_template
    ):
        """test_periodic_table_module_render_data_returns_no_selected_element_if_not_given"""

        # Arrange
        request = HttpRequest()
        element = ""
        my_module = PeriodicTableModule()
        my_module.data = element
        # Act
        result = my_module._render_data(request)
        self.assertEqual(True, result == "No selected element.")
