from tkinter import *
from data_by_board_plots import DataByBoardPlots


class DataByBoardDashboard(object):

    def __init__(self):
        frame = Frame()
        frame.pack()
        self.plots = DataByBoardPlots()
        self.plots_info = self.plots.get_plots_info()
        self.create_widgets(frame, self.plots_info)

    def create_widgets(self, frame, buttons):
        for button_text, button_command_values in buttons.items():
            button = Button(frame)
            button["text"] = button_text
            button_plots = DataByBoardPlots(
                button_command_values[0], button_command_values[1],
                button_command_values[2], button_command_values[3])
            button["command"] = button_plots.create_visualization
            button.pack(side="top")

        self.quit = Button(frame, text="QUIT", fg="red",
                              command=frame.quit)
        self.quit.pack(side="bottom")