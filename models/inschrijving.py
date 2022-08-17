from datetime import date
from models.inschrijvingsperiode import Inschrijvingsperiode
from models.vai import Vai


class Inschrijving:
    def __init__(
            self,
            inschrijving_volgnummer: str,
            inschrijving: date,
            uitschrijving: date or None,
            administratie_oin: str,
            geldig_op_1_jan: bool,
            geldig_op_1_apr: bool,
            geldig_op_1_jul: bool,
            geldig_op_1_okt: bool
    ):
        self.inschrijving_volgnummer: str = inschrijving_volgnummer
        self.inschrijving: date = inschrijving
        self.uitschrijving: date or None = uitschrijving
        self.administratie_oin: str = administratie_oin
        self.geldig_op_1_jan = geldig_op_1_jan
        self.geldig_op_1_apr = geldig_op_1_apr
        self.geldig_op_1_jul = geldig_op_1_jul
        self.geldig_op_1_okt = geldig_op_1_okt

        self.inschrijvingsperioden: [Inschrijvingsperiode] = []
        self.vais: [Vai] = []

    def __str__(self):
        return f"{self.inschrijving_volgnummer} - {str(self.inschrijving)} - {self.administratie_oin}"

    def add_inschrijvingsperiode(self, inschrijvingsperiode: Inschrijvingsperiode):
        self.inschrijvingsperioden.append(inschrijvingsperiode)

    def add_vai(self, vai: Vai):
        self.vais.append(vai)

