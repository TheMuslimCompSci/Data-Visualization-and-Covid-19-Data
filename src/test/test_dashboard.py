import unittest
import tkinter as tk
from src.main.dashboard import Dashboard


class TestDashboard(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.dashboard = Dashboard(self.root)
        self.root.mainloop()
        self.expected_buttons_info = {
            "Data By Board Dashboard": self.dashboard.create_data_by_board_dashboard,
            "Deaths Data Dashboard": self.dashboard.create_deaths_data_dashboard,
            "Trends In Daily Data Dashboard": self.dashboard.create_trends_in_daily_data_dashboard
        }

    def test_init(self):
        self.assertIs(type(self.dashboard), Dashboard)
        self.assertIsInstance(self.root, type(tk.Tk()))

    def test_configure_widgets_style(self):
        with self.assertRaises(TypeError):
            self.dashboard.configure_widgets_style(None)

    def test_create_frames(self):
        with self.assertRaises(AttributeError):
            self.dashboard.create_frames("frame")

    def test_create_label(self):
        with self.assertRaises(AttributeError):
            self.dashboard.create_label("frame", "text")

    def test_create_buttons_from_iterable(self):
        with self.assertRaises(ValueError):
            self.dashboard.create_buttons_from_iterable("frame", "buttons")

    def test_initialize_frame(self):
        with self.assertRaises(tk.TclError):
            self.dashboard.initialize_frame("frame")

    def test_hide_all_frames(self):
        with self.assertRaises(TypeError):
            self.dashboard.hide_all_frames(None)

    def test_configure_grid_layout(self):
        with self.assertRaises(AttributeError):
            self.dashboard.configure_grid_layout("frame")

    def test_create_navigation_frame(self):
        with self.assertRaises(AttributeError):
            self.dashboard.create_navigation_frame("current_frame", "create_previous_dashboard",
                                                   "previous_dashboard_arg")

    def test_create_portal_dashboard(self):
        with self.assertRaises(TypeError):
            self.dashboard.create_portal_dashboard(None)

    def test_get_main_dashboard_buttons_info(self):
        self.assertEqual(self.dashboard.get_main_dashboard_buttons_info(), self.expected_buttons_info)

    def test_create_main_dashboard(self):
        with self.assertRaises(tk.TclError):
            self.dashboard.create_main_dashboard("buttons info")

    def test_create_data_by_board_dashboard(self):
        with self.assertRaises(TypeError):
            self.dashboard.create_data_by_board_dashboard(None)

    def test_create_deaths_data_dashboard(self):
        with self.assertRaises(TypeError):
            self.dashboard.create_deaths_data_dashboard(None)

    def test_create_trends_in_daily_data_dashboard(self):
        with self.assertRaises(TypeError):
            self.dashboard.create_trends_in_daily_data_dashboard(None)

    def test_create_plots_dashboard(self):
        with self.assertRaises(tk.TclError):
            self.dashboard.create_plots_dashboard("frame")

    def test_create_plots_dashboard_buttons(self):
        with self.assertRaises(AttributeError):
            self.dashboard.create_plots_dashboard_buttons("frame", self.expected_buttons_info)

    def test_create_analytics_dashboard(self):
        with self.assertRaises(tk.TclError):
            self.dashboard.create_analytics_dashboard("plots")

    def test_create_models_dashboard(self):
        with self.assertRaises(tk.TclError):
            self.dashboard.create_analytics_dashboard("plots")

    def test_create_models_dashboard_plots_types_frame(self):
        with self.assertRaises(tk.TclError):
            self.dashboard.create_models_dashboard_plots_types_frame("plots")

    def test_create_models_dashboard_plots_styles_frame(self):
        with self.assertRaises(tk.TclError):
            self.dashboard.create_models_dashboard_plots_styles_frame("plots")

    def test_create_models_dashboard_plots_contexts_frame(self):
        with self.assertRaises(tk.TclError):
            self.dashboard.create_models_dashboard_plots_contexts_frame("plots")

    def test_create_models_dashboard_plots_palettes_frame(self):
        with self.assertRaises(tk.TclError):
            self.dashboard.create_models_dashboard_plots_palettes_frame("plots")

    def test_create_models_dashboard_radio_buttons(self):
        with self.assertRaises(AttributeError):
            self.dashboard.create_models_dashboard_radio_buttons("frame", "radio_buttons_var_default",
                                                                 "radio_buttons")

    def test_create_radio_buttons_from_iterable(self):
        with self.assertRaises(AttributeError):
            self.dashboard.create_radio_buttons_from_iterable("frame", "text", "radio_buttons_var", "value")

    def test_plots_button_clicked(self):
        with self.assertRaises(AttributeError):
            self.dashboard.plots_button_clicked("plots", "plots_type", "plots_style", "plots_context",
                                                "plots_palette")

    def test_create_dynamic_dashboard(self):
        with self.assertRaises(tk.TclError):
            self.dashboard.create_dynamic_dashboard("plots")

    def test_create_dynamic_dashboard_title_frame(self):
        with self.assertRaises(tk.TclError):
            self.dashboard.create_dynamic_dashboard_title_frame("plots")

    def test_create_dynamic_dashboard_data_frame(self):
        with self.assertRaises(tk.TclError):
            self.dashboard.create_dynamic_dashboard_data_frame("plots")

    def test_create_dynamic_dashboard_statistics_frame(self):
        with self.assertRaises(tk.TclError):
            self.dashboard.create_dynamic_dashboard_statistics_frame("plots")


if __name__ == "__main__":
    unittest.main()
