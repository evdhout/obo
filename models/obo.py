from datetime import date
from models.persoon import Persoon
from models.obo_exceptions import DuplicatePerson


class OBO:
    def __init__(self,
                 controlejaar: int,
                 brin: str,
                 sector: str,
                 datum_aanvraag: date,
                 datum_aanmaak_obo: date
                 ):

        # VLP Voorlooprecord
        self.vlp_controlejaar: int = controlejaar
        self.vlp_brin: str = brin
        self.vlp_sector: str = sector
        self.vlp_datum_aanvraag: date = datum_aanvraag
        self.vlp_datum_aanmaak_obo: date = datum_aanmaak_obo

        # CTR Controletotalen
        self.ctr_inschrijvingen: int = 0
        self.ctr_inschrijvingsperiodes: int = 0
        self.ctr_inschrijvingsperiodes_bekostigbaar: int = 0
        self.ctr_opleidingscodes: int = 0
        self.ctr_generaal: int = 0

        self.personen: {str: Persoon} = {}

    def add_person(self, persoon: Persoon):
        if persoon.persoon_id in self.personen:
            raise DuplicatePerson

        self.personen[persoon.persoon_id] = persoon

    def add_ctr(self,
                inschrijvingen: int,
                inschrijvingsperiodes: int,
                inschrijvingsperiodes_bekostigbaar: int,
                opleidingscodes: int,
                generaal: int
                ):
        self.ctr_inschrijvingen = inschrijvingen
        self.ctr_inschrijvingsperiodes = inschrijvingsperiodes
        self.ctr_inschrijvingsperiodes_bekostigbaar = inschrijvingsperiodes_bekostigbaar
        self.ctr_opleidingscodes = opleidingscodes
        self.ctr_generaal = generaal



