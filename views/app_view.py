import os.path
import platform
import tkinter as tk
from tkinter import Tk, Toplevel, StringVar, IntVar, filedialog, font
from tkinter import ttk
import webbrowser

from models.obo import OBO
from models.options import Options
from models.file_helper import FileHelper
from models.persoon import Persoon
from views.messagebox import MessageBox
from controllers.obo_file_controller import OboFileController
from models.obo_exceptions import OboException, OboFileException
from views.result_view import ResultView


class AppView(Tk):
    BSN: int = 0
    OWN: int = 1

    def __init__(self, options: Options):
        super().__init__()
        self.options = options
        self.title("OBO")
        self.geometry("800x600")

        self.obo_file_controller: OboFileController = OboFileController()
        self.obo: OBO or None = None

        # interface variables
        self.obo_search_id_string = StringVar(self, name='ID')
        self.obo_filename_string = StringVar(self, name='OBO')
        self.obo_path_string = StringVar(self, name='PATH')
        if self.options.get('obo') is not None:
            self.process_obo_file(filename=self.options.get('obo'))
        else:
            self.obo_filename_string.set('Geen bestand gekozen')
        self.obo_path_string.set(self.options.path)

        self.obo_search_type_int = IntVar()
        self.obo_search_type_int.set(AppView.BSN if self.options.is_default_bsn_search() else AppView.OWN)

        # main keyboard bindings
        self.bind("<Control-Key-o>", self.open_obo_file)
        self.bind("<Control-Key-O>", self.open_obo_file)
        self.bind("<Return>", self.search)

        # setup styling
        style = ttk.Style()

        # use classic theme if not on windows
        if platform.system != 'Windows':
            style.theme_use('classic')

        # set up table layout, with striping.
        table_font = font.nametofont(style.lookup(style='TLabel', option='font')).copy()
        table_font.configure(weight='bold')
        style.configure('TableHeader.TLabel', background='grey', foreground='white',
                        font=table_font, padding=[2, 5, 2, 5])
        style.configure('TableDataOdd.TLabel', padding=[2, 5, 2, 5], background='white')
        style.configure('TableDataEven.TLabel', padding=[2, 5, 2, 5], background='#ccc')
        style.configure('Table.TFrame', background="black")

        # set up treeview layout
        style.configure("Treeview",
                        background="white",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="white")
        style.map('Treeview',
                  background=[('selected', '#3677A8')],
                  foreground=[('selected', 'white')])

        # set up the menu
        app_menu = tk.Menu(self)
        self.config(menu=app_menu)

        file_menu = tk.Menu(app_menu)
        app_menu.add_cascade(label="Bestand", menu=file_menu)
        file_menu.add_command(label="Open OBO", command=self.open_obo_file)
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=self.quit)

        info_menu = tk.Menu(app_menu)
        app_menu.add_cascade(label="Over", menu=info_menu)
        info_menu.add_command(label="Over OBO", command=self.show_program_info)

        # set up the main window
        self.app_frame = ttk.Frame(self)
        self.app_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.obo_search_frame = ttk.LabelFrame(self.app_frame, text='Zoeken naar', width=790, height=200)
        self.obo_search_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        self.obo_result_frame = ttk.LabelFrame(self.app_frame, text='Resultaten', width=790, height=600)
        self.obo_result_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.obo_result_view = ResultView(self.obo_result_frame)
        self.obo_result_view.result_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.obo_filename_label = ttk.Label(master=self.obo_search_frame, textvariable=self.obo_filename_string)
        self.obo_filename_label.bind("<Double-Button-1>", self.open_obo_file)
        self.obo_filename_label.pack(side=tk.TOP, fill=tk.X, expand=False, padx=5, pady=5)

        self.obo_search_id_frame = ttk.Frame(self.obo_search_frame, width=790, height=100)
        self.obo_search_id_frame.pack(side=tk.TOP, fill=tk.X, expand=False, padx=5, pady=5)
        self.obo_search_id_label = ttk.Label(master=self.obo_search_id_frame, text="Leerling ID: ")
        self.obo_search_id_label.grid(column=0, row=1, sticky=tk.N, padx=5, pady=5)
        self.obo_search_id_entry = ttk.Entry(master=self.obo_search_id_frame, width=25,
                                             textvariable=self.obo_search_id_string)
        self.obo_search_id_entry.grid(column=1, row=1, sticky=tk.N, padx=5, pady=5)

        self.obo_search_type_bsn_radio = ttk.Radiobutton(master=self.obo_search_id_frame,
                                                         text="BSN", variable=self.obo_search_type_int,
                                                         value=AppView.BSN)
        self.obo_search_type_own_radio = ttk.Radiobutton(master=self.obo_search_id_frame,
                                                         text="OWN", variable=self.obo_search_type_int,
                                                         value=AppView.OWN)
        self.obo_search_type_bsn_radio.grid(column=2, row=1, sticky=tk.N, padx=5, pady=5)
        self.obo_search_type_own_radio.grid(column=3, row=1, sticky=tk.N, padx=5, pady=5)

        self.obo_search_button = ttk.Button(master=self.obo_search_id_frame, text="Zoek")
        self.obo_search_button.bind("<Button-1>", self.search)
        self.obo_search_button.grid(column=4, row=1, sticky=tk.EW)

    def fake_command(self):
        pass

    def open_obo_file(self, _event=None):
        filename = filedialog.askopenfilename(initialdir=self.obo_path_string.get(),
                                              title="Selecteer OBO.csv",
                                              filetypes=[('OBO', '.csv'), ('Alle bestanden', "*.*")])
        self.process_obo_file(filename=filename)

    def process_obo_file(self, filename: str):
        if filename:
            try:
                expanded_filename = FileHelper.get_expanded_filename(filename)
                self.obo_path_string.set(os.path.abspath(expanded_filename))
                self.obo_file_controller.process_obo(filename=expanded_filename)
                self.obo = self.obo_file_controller.obo
                self.obo_filename_string.set(f"{expanded_filename} ({len(self.obo.personen)} leerlingen)")
            except OboFileException as oe:
                MessageBox.show_error(message=oe.message,
                                      title="Foutmelding bij verwerken OBO bestand",
                                      detail=f"{oe.line_number}: {oe.line}")
            except OboException as oe:
                MessageBox.show_error(message=oe.message)
            except FileNotFoundError as fe:
                MessageBox.show_error(message=fe.strerror)
            except NotADirectoryError as de:
                MessageBox.show_error(message=de.strerror)

    def search(self, _event):
        try:
            if self.obo_search_type_int.get() == AppView.BSN:
                p = self.obo.personen[Persoon.generate_id_from_bsn(self.obo_search_id_string.get())]
            else:
                p = self.obo.personen[Persoon.generate_id_from_own(self.obo_search_id_string.get())]
            print(p)
            self.obo_result_view.display_person(p)
        except KeyError:
            self.obo_result_view.display_not_found(
                message=(f"Leerling met {'BSN' if self.obo_search_type_int.get() == AppView.BSN else 'OWN'} "
                        f"{self.obo_search_id_string.get()} niet gevonden")
            )

    def show_program_info(self):
        about_view = Toplevel(master=self.master)
        about_view.geometry("300x100")
        about_view.configure(background="white")
        about_view.title("Over OBO")

        ttk.Label(about_view, text=f"OBO versie {self.options.version}", background="white").pack(pady=10)
        github_source = ttk.Label(about_view, text=self.options.source_url, background="white")
        github_source.bind("<Button-1>", lambda e: webbrowser.open_new(self.options.source_url))
        github_source.pack(pady=10)

        about_view.mainloop()
