from datetime import date


class Inschrijvingsperiode:
    def __init__(
            self,
            inschrijvingsvolgnummer: str,
            begin: date,
            opleidingscode: str,
            bekostigbaar: bool,
            vestiging: str,
            leerjaar: int or None,
            fase: str or None,
            geldig_op_1_jan: bool,
            geldig_op_1_apr: bool,
            geldig_op_1_jul: bool,
            geldig_op_1_okt: bool
    ):
        self.inschrijvingsvolgnummer: str = inschrijvingsvolgnummer
        self.begin: date = begin
        self.opleidingscode: str = opleidingscode
        self.bekostigbaar: bool = bekostigbaar
        self.vestiging: str = vestiging
        self.leerjaar: int = leerjaar
        self.fase: str or None = fase
        self.geldig_op_1_jan = geldig_op_1_jan
        self.geldig_op_1_apr = geldig_op_1_apr
        self.geldig_op_1_jul = geldig_op_1_jul
        self.geldig_op_1_okt = geldig_op_1_okt
