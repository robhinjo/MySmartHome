import tkinter as tk  # Uvoz tkinter modula za rad s grafičkim sučeljem
from tkinter import ttk  # Uvoz ttk modula za rad s naprednijim widgetima u tkinteru
from Meteo.meteo_gui import MeteoGUI  # Uvoz MeteoGUI klase iz meteo_gui modula

class MySmartHomeApp:
    def __init__(self, root):
        self.root = root  # Postavljanje glavnog prozora aplikacije
        self.root.title("My Smart Home")  # Postavljanje naslova glavnog prozora

        self.tab_control = ttk.Notebook(root)  # Stvaranje tab kontrole za kartice
        self.main_tab = ttk.Frame(self.tab_control)  # Kreiranje glavne kartice
        self.meteo_tab = ttk.Frame(self.tab_control)  # Kreiranje Meteo kartice

        self.tab_control.add(self.main_tab, text="Main")  # Dodavanje glavne kartice u tab kontrolu
        self.tab_control.add(self.meteo_tab, text="Meteo")  # Dodavanje Meteo kartice u tab kontrolu
        self.tab_control.pack(expand=1, fill="both")  # Postavljanje tab kontrole u glavni prozor

        self.meteo_gui = MeteoGUI(self.meteo_tab)  # Stvaranje instance MeteoGUI klase unutar Meteo kartice

if __name__ == "__main__":
    root = tk.Tk()  # Stvaranje glavnog prozora aplikacije
    app = MySmartHomeApp(root)  # Stvaranje instance MySmartHomeApp klase
    root.mainloop()  # Pokretanje glavne petlje aplikacije
