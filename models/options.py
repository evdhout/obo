from models.file_helper import FileHelper


class Options:
    BSN = "BSN"
    OWN = "OWN"

    def __init__(self):
        self.debug: bool = False
        self.obo: str or None = None
        self.path: str or None = None
        self.version = "augustus 2022"
        self.default_search_type: str = Options.BSN
        self.source_url = "https://github.com/evdhout/obo"

    def __str__(self):
        return(f"OBO                 = {self.obo}\n"
               f"Path                = {self.path}\n"
               f"Standaard zoeken op = {self.default_search_type}\n"
               f"Debug               = {self.debug}\n"
               )

    def message(self, message: str):
        if self.debug:
            print(message)

    def get(self, option: str, default=None):
        value = getattr(self, option, None)
        if value is None:
            return default
        else:
            return value

    def set_path(self, path: str or None):
        if path is not None:
            try:
                self.path = FileHelper.get_expanded_path(path)
            except NotADirectoryError:
                self.path = None

    def set_obo(self, obo: str or None):
        if obo is not None:
            try:
                self.obo = FileHelper.get_expanded_filename(obo)
            except FileNotFoundError:
                self.obo = None

    def set_default_search_type(self, default: str or None):
        if default is not None and default.upper() in [Options.BSN, Options.OWN]:
            self.default_search_type = default.upper()

    def is_default_bsn_search(self):
        return self.default_search_type == Options.BSN

    def is_default_own_search(self):
        return self.default_search_type == Options.OWN
