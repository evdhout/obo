from datetime import date


# Vai = verblijf andere instelling
class Vai:
    def __init__(
            self,
            inschrijvingsvolgnummer: str,
            begin: date,
            eind: date or None,
            brin: str,
            verblijfsoort: str
    ):
        self.inschrijvingsvolgnummer: str = inschrijvingsvolgnummer
        self.begin: date = begin
        self.eind: date or None = eind
        self.brin: str = brin
        self.verblijfsoort: str = verblijfsoort
