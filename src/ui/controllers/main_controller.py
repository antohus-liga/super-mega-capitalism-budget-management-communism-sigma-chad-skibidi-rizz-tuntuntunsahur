from ui.widgets.main_window import MainWindow # this import is needed for the /
# type annotation


class MainController:
    def __init__(self, window: MainWindow) -> None: 
        self.window: MainWindow = window # this fixes the unknown /
        # parameter type warning that pyright throws
        _ = self.window.quit_button.clicked.connect(self.on_button_clicked_quit)
        # _ is needed here otherwise pyright throws a warning

    def on_button_clicked_quit(self) -> None:
        _ = self.window.close() # _ is needed here otherwise pyright throws a /
        # warning about call expression result not being used