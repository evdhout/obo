from models.options import Options
from views.app_view import AppView


class WindowController:
    def __init__(self, options: Options):
        self.options = options
        self.app_view = AppView(options=self.options)
        self.app_view.mainloop()
