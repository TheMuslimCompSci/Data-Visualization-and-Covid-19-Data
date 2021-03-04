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

    # Check that method passes when class is initialised correctly.
    def test_init(self):
        self.assertIs(type(self.dashboard), Dashboard)
        self.assertIsInstance(self.root, type(tk.Tk()))

    # Check that method fails when it takes 0 positional arguments but 1 is given.
    def test_configure_widgets_style(self):
        with self.assertRaises(TypeError):
            self.dashboard.configure_widgets_style(None)

    # Check that method fails when argument object has no tkinter attributes.
    def test_create_frames(self):
        with self.assertRaises(AttributeError):
            self.dashboard.create_frames("frame")

    # Check that method fails when argument object has no tkinter attributes.
    def test_create_label(self):
        with self.assertRaises(AttributeError):
            self.dashboard.create_label("frame", "text")

    # Check that method fails when not enough values to unpack in argument object.
    def test_create_buttons_from_iterable(self):
        with self.assertRaises(ValueError):
            self.dashboard.create_buttons_from_iterable("frame", "buttons")

    # Check that method fails when argument object can't invoke "pack" command i.e. application has been destroyed.
    def test_initialize_frame(self):
        with self.assertRaises(tk.TclError):
            self.dashboard.initialize_frame("frame")

    # Check that method fails when it takes 0 positional arguments but 1 is given.
    def test_hide_all_frames(self):
        with self.assertRaises(TypeError):
            self.dashboard.hide_all_frames(None)

    # Check that method fails when argument object has no tkinter attributes.
    def test_configure_grid_layout(self):
        with self.assertRaises(AttributeError):
            self.dashboard.configure_grid_layout("frame")

    # Check that method fails when argument object has no tkinter attributes.
    def test_create_navigation_frame(self):
        with self.assertRaises(AttributeError):
            self.dashboard.create_navigation_frame("current_frame", "create_previous_dashboard",
                                                   "previous_dashboard_arg")

    # Check that method fails when it takes 0 positional arguments but 1 is given.
    def test_create_portal_dashboard(self):
        with self.assertRaises(TypeError):
            self.dashboard.create_portal_dashboard(None)

    # Check that method passes when return value equals the expected value.
    def test_get_main_dashboard_buttons_info(self):
        self.assertEqual(self.dashboard.get_main_dashboard_buttons_info(), self.expected_buttons_info)

    # Check that method fails when argument object can't invoke "pack" command i.e. application has been destroyed.
    def test_create_main_dashboard(self):
        with self.assertRaises(tk.TclError):
            self.dashboard.create_main_dashboard("buttons info")

    # Check that method fails when it takes 0 positional arguments but 1 is given.
    def test_create_data_by_board_dashboard(self):
        with self.assertRaises(TypeError):
            self.dashboard.create_data_by_board_dashboard(None)

    # Check that method fails when it takes 0 positional arguments but 1 is given.
    def test_create_deaths_data_dashboard(self):
        with self.assertRaises(TypeError):
            self.dashboard.create_deaths_data_dashboard(None)

    # Check that method fails when it takes 0 positional arguments but 1 is given.
    def test_create_trends_in_daily_data_dashboard(self):
        with self.assertRaises(TypeError):
            self.dashboard.create_trends_in_daily_data_dashboard(None)

    # Check that method fails when argument object can't invoke "pack" command i.e. application has been destroyed.
    def test_create_plots_dashboard(self):
        with self.assertRaises(tk.TclError):
            self.dashboard.create_plots_dashboard("frame")

    # Check that method fails when argument object has no tkinter attributes.
    def test_create_plots_dashboard_buttons(self):
        with self.assertRaises(AttributeError):
            self.dashboard.create_plots_dashboard_buttons("frame", self.expected_buttons_info)

    # Check that method fails when argument object can't invoke "pack" command i.e. application has been destroyed.
    def test_create_analytics_dashboard(self):
        with self.assertRaises(tk.TclError):
            self.dashboard.create_analytics_dashboard("plots")

    # Check that method fails when argument object can't invoke "pack" command i.e. application has been destroyed.
    def test_create_models_dashboard(self):
        with self.assertRaises(tk.TclError):
            self.dashboard.create_analytics_dashboard("plots")

    # Check that method fails when argument object can't invoke "pack" command i.e. application has been destroyed.
    def test_create_models_dashboard_plots_types_frame(self):
        with self.assertRaises(tk.TclError):
            self.dashboard.create_models_dashboard_plots_types_frame("plots")

    # Check that method fails when argument object can't invoke "pack" command i.e. application has been destroyed.
    def test_create_models_dashboard_plots_styles_frame(self):
        with self.assertRaises(tk.TclError):
            self.dashboard.create_models_dashboard_plots_styles_frame("plots")

    # Check that method fails when argument object can't invoke "pack" command i.e. application has been destroyed.
    def test_create_models_dashboard_plots_contexts_frame(self):
        with self.assertRaises(tk.TclError):
            self.dashboard.create_models_dashboard_plots_contexts_frame("plots")

    # Check that method fails when argument object can't invoke "pack" command i.e. application has been destroyed.
    def test_create_models_dashboard_plots_palettes_frame(self):
        with self.assertRaises(tk.TclError):
            self.dashboard.create_models_dashboard_plots_palettes_frame("plots")

    # Check that method fails when argument object has no tkinter attributes.
    def test_create_models_dashboard_radio_buttons(self):
        with self.assertRaises(AttributeError):
            self.dashboard.create_models_dashboard_radio_buttons("frame", "radio_buttons_var_default",
                                                                 "radio_buttons")

    # Check that method fails when argument object has no tkinter attributes.
    def test_create_radio_buttons_from_iterable(self):
        with self.assertRaises(AttributeError):
            self.dashboard.create_radio_buttons_from_iterable("frame", "text", "radio_buttons_var", "value")

    # Check that method fails when argument object has no tkinter attributes.
    def test_plots_button_clicked(self):
        with self.assertRaises(AttributeError):
            self.dashboard.plots_button_clicked("plots", "plots_type", "plots_style", "plots_context",
                                                "plots_palette")

    # Check that method fails when argument object can't invoke "pack" command i.e. application has been destroyed.
    def test_create_dynamic_dashboard(self):
        with self.assertRaises(tk.TclError):
            self.dashboard.create_dynamic_dashboard("plots")

    # Check that method fails when argument object can't invoke "pack" command i.e. application has been destroyed.
    def test_create_dynamic_dashboard_title_frame(self):
        with self.assertRaises(tk.TclError):
            self.dashboard.create_dynamic_dashboard_title_frame("plots")

    # Check that method fails when argument object can't invoke "pack" command i.e. application has been destroyed.
    def test_create_dynamic_dashboard_data_frame(self):
        with self.assertRaises(tk.TclError):
            self.dashboard.create_dynamic_dashboard_data_frame("plots")

    # Check that method fails when argument object can't invoke "pack" command i.e. application has been destroyed.
    def test_create_dynamic_dashboard_statistics_frame(self):
        with self.assertRaises(tk.TclError):
            self.dashboard.create_dynamic_dashboard_statistics_frame("plots")


if __name__ == "__main__":
    unittest.main()
