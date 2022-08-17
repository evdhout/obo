from datetime import date

from models.codes_nationaliteiten import CodesNationaliteiten


class Nationaliteit:
    def __init__(self, code: str, ingang: date, eind: date or None = None):
        self.code: str = code
        self.nationaliteit: str or None = CodesNationaliteiten.get_nationaliteit(self.code)
        self.ingang: date = ingang
        self.eind: date or None = eind

    def __str__(self):
        if self.nationaliteit is None:
            nat = f"{self.code} (Onbekende code)"
        else:
            nat = f"{self.code} {self.nationaliteit}"
        if self.ingang is None and self.eind is None:
            return nat
        elif self.ingang is None:
            return f"{nat} geldig tot {str(self.eind)}"
        elif self.eind is None:
            return f"{nat} geldig vanaf {str(self.ingang)}"

        return f"{nat} geldig vanaf {str(self.ingang)} tot {str(self.eind)}"
