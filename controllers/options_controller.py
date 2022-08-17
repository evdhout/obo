import configparser
from models.options import Options


class OptionsController:
    def __init__(self):
        self.options = Options()
        self.read_ini()

        self.options.message(message=str(self.options))

    def read_ini(self):
        config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
        config.read('obo.ini')

        self.options.debug = config.getboolean('DEBUG', 'debug', fallback=False)
        self.options.set_path(path=config.get('OBO', 'initial directory', fallback=None))
        self.options.set_obo(obo=config.get('OBO', 'obo', fallback=None))
        self.options.set_default_search_type(default=config.get('STANDAARD', 'zoeken op', fallback=None))

