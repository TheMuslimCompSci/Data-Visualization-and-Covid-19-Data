import tkinter as tk
from tkinter import ttk
from data_by_board_plots import DataByBoardPlots
from deaths_data_plots import DeathsDataPlots
from trends_in_daily_data_plots import TrendsInDailyDataPlots
from functools import partial


class Dashboard(object):

    def __init__(self, master, button_plots):
        master.title("COVID-19 Data Visualization App")
        master.state("zoomed")
        self.configure_widgets_style()
        self.create_frames(master)
        self.create_portal_dashboard()

    def configure_widgets_style(self):
        widgets_style = ttk.Style()
        widgets_style.theme_use("clam")
        widgets_style.configure(".", font=("Arial", 12))
        widgets_style.configure("TFrame", background="cyan")
        widgets_style.configure("TButton", background="white")
        widgets_style.configure("TLabel", background="cyan")
        widgets_style.configure("TRadiobutton", background="cyan")
        widgets_style.configure("Treeview",
                                background="white",
                                foreground="black",
                                fieldbackground="white")
        widgets_style.map("Treeview", background=[("selected", "blue")])
        widgets_style.configure("Horizontal.TScrollbar", background="white")
        widgets_style.configure("Vertical.TScrollbar", background="white")

    def create_frames(self, master):
        self.main_frame = ttk.Frame(master)
        self.main_frame.pack(fill="both", expand=True)
        self.portal_dashboard_frame = ttk.Frame(self.main_frame)
        self.main_dashboard_frame = ttk.Frame(self.main_frame)
        self.data_by_board_dashboard_frame = ttk.Frame(self.main_frame)
        self.deaths_data_dashboard_frame = ttk.Frame(self.main_frame)
        self.trends_in_daily_data_dashboard_frame = ttk.Frame(self.main_frame)
        self.analytics_dashboard_frame = ttk.Frame(self.main_frame)
        self.dynamic_dashboard_frame = ttk.Frame(self.main_frame)
        self.models_dashboard_frame = ttk.Frame(self.main_frame)

    def create_portal_dashboard(self):
        self.initialize_frame(self.portal_dashboard_frame)
        welcome_text = "COVID-19 Data Visualization App"
        welcome_label = ttk.Label(self.portal_dashboard_frame)
        welcome_label["text"] = welcome_text
        welcome_label.grid(row=0, column=0)
        main_dashboard_buttons_info = self.get_main_dashboard_buttons_info()
        start_button = ttk.Button(self.portal_dashboard_frame)
        start_button["text"] = "START"
        start_button["command"] = partial(self.create_main_dashboard, main_dashboard_buttons_info)
        start_button.grid(padx=10, pady=10, row=1, column=0, sticky="nesw")
        self.configure_grid_layout(self.portal_dashboard_frame)
    
    def create_navigation_frame(self, current_frame, create_previous_dashboard, previous_dashboard_arg):
        navigation_frame = ttk.Frame(current_frame)
        navigation_frame.pack()
        back_button = ttk.Button(navigation_frame)
        back_button["text"] = "BACK"
        if previous_dashboard_arg is None:
            back_button["command"] = partial(create_previous_dashboard)
        else:
            back_button["command"] = partial(create_previous_dashboard, previous_dashboard_arg)
        back_button.pack(side="left")
        quit_button = ttk.Button(navigation_frame)
        quit_button["text"] = "QUIT"
        quit_button["command"] = current_frame.quit
        quit_button.pack(side="right")

    def get_main_dashboard_buttons_info(self):
        buttons_info = {
            "Data By Board Dashboard": self.create_data_by_board_dashboard,
            "Deaths Data Dashboard": self.create_deaths_data_dashboard,
            "Trends In Daily Data Dashboard": self.create_trends_in_daily_data_dashboard
        }
        return buttons_info

    def create_main_dashboard(self, buttons_info):
        self.initialize_frame(self.main_dashboard_frame)
        buttons_frame = ttk.Frame(self.main_dashboard_frame)
        buttons_frame.pack(fill="both", expand=True)
        self.create_buttons_from_iterable(buttons_frame, buttons_info.items())
        self.create_navigation_frame(self.main_dashboard_frame, self.create_portal_dashboard, None)

    def create_buttons_from_iterable(self, frame, buttons):
        row_index = 0
        column_index = 0
        counter = 0
        for button_text, button_command in buttons:
            button = ttk.Button(frame)
            button["text"] = button_text
            button["command"] = button_command
            button.grid(padx=5, pady=5, row=row_index, column=column_index, sticky="nesw")
            counter += 1
            if counter % 2 == 0:
                row_index += 1
            if column_index == 1:
                column_index = 0
            else:
                column_index = 1
        self.configure_grid_layout(frame)

    def create_plots_dashboard(self, frame):
        self.initialize_frame(frame)
        plots_buttons_frame = ttk.Frame(frame)
        plots_buttons_frame.pack(fill="both", expand=True, side="top")
        if frame == self.data_by_board_dashboard_frame:
            plots = DataByBoardPlots()
        elif frame == self.deaths_data_dashboard_frame:
            plots = DeathsDataPlots()
        elif frame == self.trends_in_daily_data_dashboard_frame:
            plots = TrendsInDailyDataPlots()
        plots_buttons_info = plots.get_plots_info()
        self.create_plots_dashboard_buttons(plots_buttons_frame, plots_buttons_info)
        self.create_navigation_frame(frame, self.create_main_dashboard, self.get_main_dashboard_buttons_info())

    def create_plots_dashboard_buttons(self, frame, buttons):
        row_index = 0
        column_index = 0
        counter = 0
        for button_text, button_command_values in buttons.items():
            button = ttk.Button(frame)
            button["text"] = button_text
            if len(buttons) == 5:
                button_plots = DataByBoardPlots(button_command_values[0], button_command_values[1],
                                                button_command_values[2], button_command_values[3],
                                                button_command_values[4], button_command_values[5])
            elif len(buttons) == 9:
                button_plots = DeathsDataPlots(button_command_values[0], button_command_values[1],
                                               button_command_values[2], button_command_values[3],
                                               button_command_values[4], button_command_values[5],
                                               button_command_values[6])
            elif len(buttons) == 12:
                button_plots = TrendsInDailyDataPlots(button_command_values[0], button_command_values[1],
                                                      button_command_values[2], button_command_values[3],
                                                      button_command_values[4], button_command_values[5],
                                                      button_command_values[6], button_command_values[7])
            button["command"] = partial(self.create_analytics_dashboard, button_plots)
            button.grid(padx=5, pady=5, row=row_index, column=column_index, sticky="nesw")
            counter += 1
            if counter % 2 == 0:
                row_index += 1
            if column_index == 1:
                column_index = 0
            else:
                column_index = 1
        self.configure_grid_layout(frame)

    def create_analytics_dashboard(self, plots):
        self.initialize_frame(self.analytics_dashboard_frame)
        buttons_info = {
            "Plot": partial(self.create_models_dashboard, plots),
            "Data": partial(self.create_dynamic_dashboard, plots),
        }
        buttons_frame = ttk.Frame(self.analytics_dashboard_frame)
        buttons_frame.pack(fill="both", expand=True, side="top")
        self.create_buttons_from_iterable(buttons_frame, buttons_info.items())
        create_plots_dashboard = None
        if type(plots) is DataByBoardPlots:
            create_plots_dashboard = self.create_data_by_board_dashboard
        elif type(plots) is DeathsDataPlots:
            create_plots_dashboard = self.create_deaths_data_dashboard
        elif type(plots) is TrendsInDailyDataPlots:
            create_plots_dashboard = self.create_trends_in_daily_data_dashboard
        self.create_navigation_frame(self.analytics_dashboard_frame, create_plots_dashboard, None)

    def create_models_dashboard(self, plots):
        self.initialize_frame(self.models_dashboard_frame)
        plots_type = self.create_models_dashboard_plots_types_frame(plots)
        plots_style = self.create_models_dashboard_plots_styles_frame(plots)
        plots_context = self.create_models_dashboard_plots_contexts_frame(plots)
        plots_palette = self.create_models_dashboard_plots_palettes_frame(plots)
        plots_button_frame = ttk.Frame(self.models_dashboard_frame)
        plots_button_frame.pack(fill="both", expand=True, side="top")
        plots_button = ttk.Button(plots_button_frame)
        plots_button["text"] = "Plot"
        plots_button["command"] = lambda: self.plots_button_clicked(plots, plots_type.get(), plots_style.get(), plots_context.get(), plots_palette.get())
        plots_button.pack()
        self.create_navigation_frame(self.models_dashboard_frame, self.create_analytics_dashboard, plots)

    def plots_button_clicked(self, plots, plots_type, plots_style, plots_context, plots_palette):
        if plots_style == "None":
            plots_style = None
        if plots_palette == "None":
            plots_palette = None
        return plots.create_visualization(plots_type, plots_style, plots_context, plots_palette)

    def create_models_dashboard_plots_types_frame(self, plots):
        plots_types_frame = ttk.Frame(self.models_dashboard_frame)
        plots_types_frame.pack(fill="both", expand=True, side="top")
        self.create_label(plots_types_frame, "Select a plot type:")
        plots_types = plots.get_plots_types_list()
        plots_type = self.create_models_dashboard_radio_buttons(plots_types_frame, "default", plots_types)
        return plots_type

    def create_models_dashboard_plots_styles_frame(self, plots):
        plots_styles_frame = ttk.Frame(self.models_dashboard_frame)
        plots_styles_frame.pack(fill="both", expand=True, side="top")
        self.create_label(plots_styles_frame, "Select a plot style:")
        PLOTS_STYLES = plots.get_plots_styles_list()
        plots_style = self.create_models_dashboard_radio_buttons(plots_styles_frame, "notebook",  PLOTS_STYLES)
        return plots_style

    def create_models_dashboard_plots_contexts_frame(self, plots):
        plots_contexts_frame = ttk.Frame(self.models_dashboard_frame)
        plots_contexts_frame.pack(fill="both", expand=True, side="top")
        self.create_label(plots_contexts_frame, "Select a plot context:")
        PLOTS_CONTEXTS = plots.get_plots_contexts_list()
        plots_context = self.create_models_dashboard_radio_buttons(plots_contexts_frame, "notebook",  PLOTS_CONTEXTS)
        return plots_context

    def create_models_dashboard_plots_palettes_frame(self, plots):
        plots_palettes_frame = ttk.Frame(self.models_dashboard_frame)
        plots_palettes_frame.pack(fill="both", expand=True, side="top")
        self.create_label(plots_palettes_frame, "Select a plot palette:")
        PLOTS_PALETTES = plots.get_plots_palettes_list()
        plots_palette = self.create_models_dashboard_radio_buttons(plots_palettes_frame, "notebook",  PLOTS_PALETTES)
        return plots_palette

    def create_label(self, frame, text):
        label = ttk.Label(frame)
        label["text"] = text
        label.pack(side="top")

    def create_models_dashboard_radio_buttons(self, frame, radio_buttons_var_default, radio_buttons):
        radio_buttons_var = tk.StringVar()
        radio_buttons_var.set(radio_buttons_var_default)
        if type(radio_buttons[0]) is tuple:
            for text, value in radio_buttons:
                self.create_radio_buttons_from_iterable(frame, text, radio_buttons_var, value)
        else:
            for text in radio_buttons:
                self.create_radio_buttons_from_iterable(frame, text, radio_buttons_var, text)
        return radio_buttons_var

    def create_radio_buttons_from_iterable(self, frame, text, radio_buttons_var, value):
        radio_button = ttk.Radiobutton(frame)
        radio_button["text"] = text
        radio_button["variable"] = radio_buttons_var
        radio_button["value"] = value
        radio_button.pack(side="left")

    def create_dynamic_dashboard(self, plots):
        self.initialize_frame(self.dynamic_dashboard_frame)
        self.create_dynamic_dashboard_title_frame(plots)
        self.create_dynamic_dashboard_data_frame(plots)
        self.create_dynamic_dashboard_statistics_frame(plots)
        self.create_navigation_frame(self.dynamic_dashboard_frame, self.create_analytics_dashboard, plots)

    def create_dynamic_dashboard_title_frame(self, plots):
        title_frame = ttk.Frame(self.dynamic_dashboard_frame)
        title_frame.pack()
        plots_title = plots.get_plots_title()
        self.create_label(title_frame, plots_title)

    def create_dynamic_dashboard_data_frame(self, plots):
        data_frame = ttk.Frame(self.dynamic_dashboard_frame)
        data_frame.pack(fill="both", expand=True, side="top")
        y_scrollbar = ttk.Scrollbar(data_frame, orient="vertical")
        y_scrollbar.pack(side="right", fill="y")
        x_scrollbar = ttk.Scrollbar(data_frame, orient="horizontal")
        x_scrollbar.pack(side="bottom", fill="x")
        data = ttk.Treeview(data_frame, yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)
        y_scrollbar.config(command=data.yview)
        x_scrollbar.config(command=data.xview)
        plots_data = plots.get_plots_data()
        plots_axis_column_index = plots.get_plots_axis_column_index()
        data["column"] = list(plots_data.columns)
        data["show"] = "headings"
        data.tag_configure("<10", background="green")
        data.tag_configure("<100", background="yellow")
        data.tag_configure("<1000", background="orange")
        data.tag_configure(">=1000", background="red")
        for column in data["column"]:
            data.heading(column, text=column)
        plots_data_rows = plots_data.to_numpy().tolist()
        for row in plots_data_rows:
            if row[plots_axis_column_index] < 10:
                data.insert(parent="", index="end", values=row, tags=("<10",))
            elif 10 <= row[plots_axis_column_index] < 100:
                data.insert(parent="", index="end", values=row, tags=("<100",))
            elif 100 <= row[plots_axis_column_index] < 1000:
                data.insert(parent="", index="end", values=row, tags=("<1000",))
            elif row[plots_axis_column_index] >= 1000:
                data.insert(parent="", index="end", values=row, tags=(">=1000",))
        data.pack(fill="both", expand=True)

    def create_dynamic_dashboard_statistics_frame(self, plots):
        statistics_frame = ttk.Frame(self.dynamic_dashboard_frame)
        statistics_frame.pack(fill="both", expand=True, side="top")
        plots_statistics = plots.get_plots_statistics()
        row_index = 0
        column_index = 0
        counter = 0
        for statistic in plots_statistics:
            statistic_label = ttk.Label(statistics_frame)
            statistic_label["text"] = statistic
            statistic_label.grid(padx=5, pady=5, row=row_index, column=column_index, sticky="nesw")
            counter += 1
            if counter % 2 == 0:
                row_index += 1
            if column_index == 1:
                column_index = 0
            else:
                column_index = 1
        self.configure_grid_layout(statistics_frame)

    def initialize_frame(self, frame):
        self.hide_all_frames()
        frame.pack(fill="both", expand=True)

    def hide_all_frames(self):
        frames = [self.portal_dashboard_frame, self.main_dashboard_frame, self.data_by_board_dashboard_frame, 
                  self.deaths_data_dashboard_frame, self.trends_in_daily_data_dashboard_frame, 
                  self.analytics_dashboard_frame, self.dynamic_dashboard_frame, self.models_dashboard_frame]
        for frame in frames:
            frame.pack_forget()
            for widget in frame.winfo_children():
                widget.destroy()

    def configure_grid_layout(self, frame):
        grid_size = tk.Grid.size(frame)
        for i in range(grid_size[0]):
            tk.Grid.columnconfigure(frame, index=i, weight=1)
        for i in range(grid_size[1]):
            tk.Grid.rowconfigure(frame, index=i, weight=1)

    def create_data_by_board_dashboard(self):
        self.create_plots_dashboard(self.data_by_board_dashboard_frame)

    def create_deaths_data_dashboard(self):
        self.create_plots_dashboard(self.deaths_data_dashboard_frame)

    def create_trends_in_daily_data_dashboard(self):
        self.create_plots_dashboard(self.trends_in_daily_data_dashboard_frame)
