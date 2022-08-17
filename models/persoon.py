from datetime import date
from models.nationaliteit import Nationaliteit
from models.inschrijving import Inschrijving

from models.obo_exceptions import PersonWithoutBSNandOWN


class Persoon:
    BSN = 1
    OWN = 2

    def __init__(self,
                 bsn: str,
                 own: str,
                 geboortedatum: date,
                 vestiging_in_nl: date or None,
                 ingang_verblijfstitel: date or None,
                 binnenkomst_in_nl_volgens_instelling: date or None,
                 indicatie_geheim_adres: bool or None,
                 postcodecijfers: int or None
                 ):
        self.persoon_id: str = ''
        self.persoon_id_type: int = self.BSN
        self.bsn: str or None = bsn if bsn else None
        self.own: str or None = own if own else None
        self.geboortedatum: date = geboortedatum
        self.vestiging_in_nl: date or None = vestiging_in_nl
        self.ingang_verblijfstitel: date or None = ingang_verblijfstitel
        self.binnenkomst_in_nl_volgens_instelling: date or None = binnenkomst_in_nl_volgens_instelling
        self.indicatie_geheim_adres: bool or None = indicatie_geheim_adres
        self.postcodecijfers: int or None = postcodecijfers

        self.nationaliteit: [Nationaliteit] = []
        self.inschrijvingen: [Inschrijving] = []

        if self.bsn is not None:
            self.persoon_id = Persoon.generate_id_from_bsn(self.bsn)
            self.persoon_id_type = Persoon.BSN
        elif self.own is not None:
            self.persoon_id = Persoon.generate_id_from_own(self.own)
            self.persoon_id_type = Persoon.OWN
        else:
            raise PersonWithoutBSNandOWN

    def __str__(self):
        return (f"{self.get_id_string()}\n"
                f"Geboortedatum = {self.geboortedatum}\n"
                f"Datum vestiging in Nederland = {self.vestiging_in_nl}\n")

    def add_nat(self, nat: Nationaliteit):
        self.nationaliteit.append(nat)

    def add_isg(self, isg: Inschrijving):
        self.inschrijvingen.append(isg)

    def get_id_string(self):
        if self.persoon_id_type == Persoon.BSN:
            return f"BSN = {self.bsn}"
        else:
            return f"OWN = {self.own}"

    @staticmethod
    def generate_id_from_own(own: str):
        return f"OWN{own}"

    @staticmethod
    def generate_id_from_bsn(bsn: str):
        return f"BSN{bsn}"
