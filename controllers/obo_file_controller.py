import datetime
from datetime import date
from typing import IO

from models.obo import OBO

from models.obo_exceptions import *
from models.persoon import Persoon
from models.nationaliteit import Nationaliteit
from models.inschrijving import Inschrijving
from models.inschrijvingsperiode import Inschrijvingsperiode
from models.vai import Vai


class OboFileController:
    VLP = "VLP"
    PER = "PER"
    NAT = "NAT"
    ISG = "ISG"
    ISP = "ISP"
    VAI = "VAI"
    CTR = "CTR"
    STR = "STR"

    STATE = {
        "STR": ["VLP"],
        "VLP": ["PER", "CTR"],
        "PER": ["NAT", "ISG"],
        "NAT": ["NAT", "ISG"],
        "ISG": ["ISP"],
        "ISP": ["ISP", "VAI", "ISG", "PER", "CTR"],
        "VAI": ["VAI", "ISG", "PER", "CTR"],
        "CTR": []
    }

    RECORDSOORT = {"VLP": "Voorlooprecord",
                   "PER": "Persoon",
                   "NAT": "Nationaliteit",
                   "ISG": "Inschrijving",
                   "ISP": "Inschrijvingsperiode",
                   "VAI": "Verblijf Andere Instelling",
                   "CTR": "Controletotalen"}

    def __init__(self):
        self._obo_file: IO or None = None
        self._state: str = ''
        self._obo_line: str = ''
        self._obo_line_number: int = 0
        self._obo_line_fields: [str] = []
        self.obo: OBO or None = None

    def init(self, filename: str):
        try:
            self._obo_file = open(filename, "r")
        except OSError:
            raise OboFileOpenError(filename=filename)

        self._state = OboFileController.STR
        self._obo_line = ''
        self._obo_line_number = 0
        self._obo_line_fields = []
        self.obo = None

    def process_obo(self, filename: str):
        self.init(filename)

        self._read_obo_line()

        self.obo = OBO(controlejaar=int(self._obo_line_fields[1]),
                       brin=self._obo_line_fields[2],
                       sector=self._obo_line_fields[3],
                       datum_aanvraag=self._convert_date(self._obo_line_fields[4]),
                       datum_aanmaak_obo=self._convert_date(self._obo_line_fields[4]))

        cur_person: Persoon or None = None
        cur_inschrijving: Inschrijving or None = None
        while self._obo_file:
            self._read_obo_line()
            if self._state == OboFileController.PER:
                cur_person = Persoon(
                    bsn=self._obo_line_fields[1],
                    own=self._obo_line_fields[2],
                    geboortedatum=self._convert_date(self._obo_line_fields[3]),
                    vestiging_in_nl=self._convert_date(self._obo_line_fields[4], required=False),
                    ingang_verblijfstitel=self._convert_date(self._obo_line_fields[5], required=False),
                    binnenkomst_in_nl_volgens_instelling=self._convert_date(self._obo_line_fields[6], required=False),
                    indicatie_geheim_adres=self._convert_boolean(self._obo_line_fields[7], required=False),
                    postcodecijfers=self._convert_number(self._obo_line_fields[8], required=False)
                )
                self.obo.add_person(cur_person)
            elif self._state == OboFileController.NAT:
                cur_person.add_nat(Nationaliteit(code=self._obo_line_fields[3],
                                                 ingang=self._convert_date(self._obo_line_fields[4]),
                                                 eind=self._convert_date(self._obo_line_fields[5], required=False))
                                   )
            elif self._state == OboFileController.ISG:
                cur_inschrijving = Inschrijving(
                    inschrijving_volgnummer=self._obo_line_fields[3],
                    inschrijving=self._convert_date(self._obo_line_fields[4]),
                    uitschrijving=self._convert_date(self._obo_line_fields[5], required=False),
                    administratie_oin=self._obo_line_fields[6],
                    geldig_op_1_jan=self._convert_boolean(self._obo_line_fields[7]),
                    geldig_op_1_apr=self._convert_boolean(self._obo_line_fields[8]),
                    geldig_op_1_jul=self._convert_boolean(self._obo_line_fields[9]),
                    geldig_op_1_okt=self._convert_boolean(self._obo_line_fields[10]),
                )
                cur_person.add_isg(cur_inschrijving)
            elif self._state == OboFileController.ISP:
                cur_inschrijving.add_inschrijvingsperiode(
                    Inschrijvingsperiode(inschrijvingsvolgnummer=self._obo_line_fields[3],
                                         begin=self._convert_date(self._obo_line_fields[4]),
                                         opleidingscode=self._obo_line_fields[5],
                                         bekostigbaar=self._convert_boolean(self._obo_line_fields[6]),
                                         vestiging=self._obo_line_fields[7],
                                         leerjaar=self._convert_number(self._obo_line_fields[8], required=False),
                                         fase=self._obo_line_fields[9],
                                         geldig_op_1_jan=self._convert_boolean(self._obo_line_fields[10]),
                                         geldig_op_1_apr=self._convert_boolean(self._obo_line_fields[11]),
                                         geldig_op_1_jul=self._convert_boolean(self._obo_line_fields[12]),
                                         geldig_op_1_okt=self._convert_boolean(self._obo_line_fields[10]),
                                         ),
                )
            elif self._state == OboFileController.VAI:
                cur_inschrijving.add_vai(Vai(inschrijvingsvolgnummer=self._obo_line_fields[3],
                                             begin=self._convert_date(self._obo_line_fields[4]),
                                             eind=self._convert_date(self._obo_line_fields[5], required=False),
                                             brin=self._obo_line_fields[6],
                                             verblijfsoort=self._obo_line_fields[7]
                                             )
                                         )
            elif self._state == OboFileController.CTR:
                self.obo.add_ctr(inschrijvingen=int(self._obo_line_fields[1]),
                                 inschrijvingsperiodes=int(self._obo_line_fields[2]),
                                 inschrijvingsperiodes_bekostigbaar=int(self._obo_line_fields[3]),
                                 opleidingscodes=int(self._obo_line_fields[4]),
                                 generaal=int(self._obo_line_fields[5])
                                 )
                break

        self._obo_file.close()

    def _read_obo_line(self):
        self._obo_line = self._obo_file.readline().rstrip()
        self._obo_line_fields = self._obo_line.split('|')
        self._obo_line_number += 1
        line_state = self._obo_line_fields[0]
        if line_state in OboFileController.STATE[self._state]:
            self._state = line_state
        else:
            raise UnexpectedOboRecordType(recordtype=line_state,
                                          line=self._obo_line,
                                          line_number=self._obo_line_number,
                                          expected=','.join(OboFileController.STATE[self._state]))

    def _convert_date(self, date_string: str, required: bool = True) -> date or None:
        try:
            return datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
        except ValueError as _e:
            if not required:
                if not date_string:
                    return None
            elif date_string == '0000-00-00':
                return None
            raise InvalidDateFormat(date_string=date_string, line_number=self._obo_line_number, line=self._obo_line)

    def _convert_boolean(self, bool_string: str, required: bool = True) -> bool or None:
        if bool_string == 'J':
            return True
        elif bool_string == 'N':
            return False
        elif not bool_string and not required:
            return None
        else:
            raise InvalidBooleanFormat(bool_string=bool_string, line=self._obo_line, line_number=self._obo_line_number)

    def _convert_number(self, number_string: str, required: bool = True) -> int or None:
        try:
            return int(number_string)
        except ValueError:
            if not required:
                return None
            else:
                raise InvalidNumberFormat(number_string=number_string,
                                          line=self._obo_line,
                                          line_number=self._obo_line_number)
