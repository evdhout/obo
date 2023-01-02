import tkinter as tk
from tkinter import Tk, Toplevel
from tkinter import ttk
from datetime import date

from models.persoon import Persoon
from models.nationaliteit import Nationaliteit
from models.inschrijving import Inschrijving
from models.inschrijvingsperiode import Inschrijvingsperiode
from models.vai import Vai
from models.elementcode_opleiding import ElementcodeOpleiding


class ResultView:
    def __init__(self, master: Toplevel or Tk):
        self.master = master

        self.result_canvas = tk.Canvas(master=master, background='grey')
        self.result_frame = ttk.Frame(self.result_canvas, padding=(5, 0))
        self.result_frame_row: int = 0
        self.result_frame.columnconfigure(1, weight=1)

        self.result_scroll = tk.Scrollbar(self.result_canvas, orient="vertical", command=self.result_canvas.yview)
        self.result_canvas.configure(yscrollcommand=self.result_scroll.set)
        self.result_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.result_canvas.create_window((4, 4), window=self.result_frame, anchor=tk.NW)
        self.result_frame.bind("<Configure>",
                               lambda _e, canvas=self.result_canvas: canvas.configure(scrollregion=canvas.bbox("all")))

        self.bold_font = tk.font.nametofont(ttk.Style().lookup(style='TLabel', option='font')).copy()
        self.bold_font.configure(weight='bold')

    def empty_result_frame(self):
        self.result_frame_row = 0
        for widget in self.result_frame.winfo_children():
            widget.destroy()

    def display_detail_row(self, label: str, value: str):
        row_label = f"{label}:" if label else ''
        ttk.Label(master=self.result_frame, text=row_label, width=25, anchor=tk.NE
                  ).grid(row=self.result_frame_row, column=0, padx=2, pady=2, sticky=tk.W)
        ttk.Label(master=self.result_frame, text=value, width=62, anchor=tk.NW
                  ).grid(row=self.result_frame_row, column=1, padx=2, pady=2, sticky=tk.W)
        self.result_frame_row += 1

    def display_detail_heading(self, label: str, anchor: str = tk.W):
        ttk.Label(master=self.result_frame, text=label, width=25, anchor=anchor, font=self.bold_font
                  ).grid(row=self.result_frame_row, column=0, padx=2, pady=2, sticky=tk.W)
        ttk.Label(master=self.result_frame, text='', width=62, anchor=tk.NW
                  ).grid(row=self.result_frame_row, column=1, padx=2, pady=2, sticky=tk.W)
        self.result_frame_row += 1

    def display_not_found(self, message: str):
        self.empty_result_frame()
        self.display_detail_heading(label="Leerling niet gevonden")
        self.display_detail_row(label="", value=message)

    def display_person(self, person: Persoon):
        self.empty_result_frame()
        self.display_detail_heading(label="Leerling")
        self.display_detail_row(label="BSN", value=person.bsn)
        self.display_detail_row(label="OWN", value=person.own)
        self.display_detail_row(label="Geboortedatum", value=ResultView.format_date(person.geboortedatum))
        self.display_detail_row(label="Vestiging in NL", value=ResultView.format_date(person.vestiging_in_nl))
        self.display_detail_row(label="Ingang verblijfstitel",
                                value=ResultView.format_date(person.binnenkomst_in_nl_volgens_instelling))
        self.display_detail_row(label="Binnenkomst NL instelling",
                                value=ResultView.format_date(person.ingang_verblijfstitel))
        self.display_detail_row(label="Geheim adres", value=self.format_boolean(person.indicatie_geheim_adres))
        self.display_detail_row(label="Postcodecijfers", value=str(person.postcodecijfers))

        nat: Nationaliteit
        for i, nat in enumerate(person.nationaliteit):
            self.display_detail_row(label=f"Nationaliteit {i + 1}", value=str(nat))

        isg: Inschrijving
        for i, isg in enumerate(person.inschrijvingen):
            self.display_detail_heading(label=f"Inschrijving {i + 1}")
            self.display_detail_row(label="Inschrijvingvolgnummer", value=isg.inschrijving_volgnummer)
            self.display_detail_row(label="Datum inschrijving", value=ResultView.format_date(isg.inschrijving))
            if isg.uitschrijving is not None:
                self.display_detail_row(label="Datum uitschrijving", value=ResultView.format_date(isg.uitschrijving))
            self.display_detail_row(label="Administratie OIN", value=isg.administratie_oin)
            self.display_detail_row(label="Geldig op",
                                    value=ResultView.format_geldig_op(jan=isg.geldig_op_1_jan,
                                                                      apr=isg.geldig_op_1_apr,
                                                                      jul=isg.geldig_op_1_jul,
                                                                      okt=isg.geldig_op_1_okt))

            isp: Inschrijvingsperiode
            for j, isp in enumerate(isg.inschrijvingsperioden):
                self.display_detail_heading(label=f"Inschrijvingsperiode {i + 1}.{j + 1}", anchor=tk.E)
                self.display_detail_row(label="Inschrijvingsvolgnummer", value=isp.inschrijvingsvolgnummer)
                self.display_detail_row(label="Datum begin", value=ResultView.format_date(isp.begin))
                self.display_detail_row(label="Opleiding",
                                        value=(f"{isp.opleidingscode} - "
                                               f"{ElementcodeOpleiding.get_opleiding(isp.opleidingscode)}"))
                self.display_detail_row(label="Vestiging",
                                        value=isp.vestiging)
                if isp.leerjaar and isp.fase:
                    self.display_detail_row(label="Leerjaar / fase", value=f"{isp.leerjaar} / {isp.fase}")
                elif isp.leerjaar:
                    self.display_detail_row(label="Leerjaar", value=str(isp.leerjaar))
                elif isp.fase:
                    self.display_detail_row(label="Fase", value=str(isp.fase))

                self.display_detail_row(label="Bekostigbaar", value=ResultView.format_boolean(isp.bekostigbaar))
                self.display_detail_row(label="Geldig op",
                                        value=ResultView.format_geldig_op(jan=isp.geldig_op_1_jan,
                                                                          apr=isp.geldig_op_1_apr,
                                                                          jul=isp.geldig_op_1_jul,
                                                                          okt=isp.geldig_op_1_okt))

            vai: Vai
            for j, vai in enumerate(isg.vais):
                self.display_detail_heading(label=f"VAI {i + 1}.{j + 1}", anchor=tk.E)
                self.display_detail_row(label="Inschrijvingsvolgnummer", value=vai.inschrijvingsvolgnummer)
                self.display_detail_row(label="Datum begin", value=ResultView.format_date(vai.begin))
                self.display_detail_row(label="Datum eind", value=ResultView.format_date(vai.eind))
                self.display_detail_row(label="BRIN", value=vai.brin)
                self.display_detail_row(label="Verblijfsoort", value=vai.verblijfsoort)

    @staticmethod
    def format_date(d: date or None):
        if d is None:
            return ''

        return d.strftime("%Y-%m-%d")

    @staticmethod
    def format_boolean(b: bool):
        return "Ja" if b else "Nee"

    @staticmethod
    def format_geldig_op(jan: bool, apr: bool, jul: bool, okt: bool):
        return (f"1-1 {'Ja' if jan else 'Nee'}, 1-4 {'Ja' if apr else 'Nee'}, "
                f"1-7 {'Ja' if jul else 'Nee'}, 1-10 {'Ja' if okt else 'Nee'}")
