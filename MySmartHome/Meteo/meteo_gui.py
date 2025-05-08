import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from Meteo.meteo import Meteo
import os  # Dodavanje uvoza os modula

# Klasa MeteoGUI koja stvara GUI za Meteo podatke
class MeteoGUI:
    def __init__(self, parent):
        self.parent = parent  # Spremanje referencije na roditeljski widget
        self.meteo = Meteo()  # Stvaranje instance Meteo klase

        self.create_widgets()  # Pozivanje funkcije za stvaranje GUI elemenata
        self.update_values()  # Pozivanje funkcije za ažuriranje vrijednosti u GUI-u

    def create_widgets(self):
        # Kreiranje labela za prikaz različitih podataka
        self.inside_temp_label = ttk.Label(self.parent, text="Inside Temperature:")  # Label za temperaturu unutra
        self.inside_temp_value = ttk.Label(self.parent, text="")  # Label za vrijednost temperature unutra
        self.outside_temp_label = ttk.Label(self.parent, text="Outside Temperature:")  # Label za temperaturu vani
        self.outside_temp_value = ttk.Label(self.parent, text="")  # Label za vrijednost temperature vani
        self.city_temp_label = ttk.Label(self.parent, text="City Temperature:")  # Label za temperaturu u gradu
        self.city_temp_value = ttk.Label(self.parent, text="")  # Label za vrijednost temperature u gradu
        self.humidity_label = ttk.Label(self.parent, text="Humidity:")  # Label za vlažnost zraka
        self.humidity_value = ttk.Label(self.parent, text="")  # Label za vrijednost vlažnosti zraka
        self.pressure_label = ttk.Label(self.parent, text="Pressure:")  # Label za tlak zraka
        self.pressure_value = ttk.Label(self.parent, text="")  # Label za vrijednost tlaka zraka
        
        self.clothing_label = ttk.Label(self.parent, text="Recommended Clothing:")  # Label za preporučenu odjeću
        self.clothing_icon = ttk.Label(self.parent)  # Label za prikaz ikone odjeće

        # Postavljanje labela u grid layout
        self.inside_temp_label.grid(row=0, column=0, sticky=tk.W)  # Postavljanje labela za temperaturu unutra
        self.inside_temp_value.grid(row=0, column=1, sticky=tk.E)  # Postavljanje vrijednosti temperature unutra
        self.outside_temp_label.grid(row=1, column=0, sticky=tk.W)  # Postavljanje labela za temperaturu vani
        self.outside_temp_value.grid(row=1, column=1, sticky=tk.E)  # Postavljanje vrijednosti temperature vani
        self.city_temp_label.grid(row=2, column=0, sticky=tk.W)  # Postavljanje labela za temperaturu u gradu
        self.city_temp_value.grid(row=2, column=1, sticky=tk.E)  # Postavljanje vrijednosti temperature u gradu
        self.humidity_label.grid(row=3, column=0, sticky=tk.W)  # Postavljanje labela za vlažnost zraka
        self.humidity_value.grid(row=3, column=1, sticky=tk.E)  # Postavljanje vrijednosti vlažnosti zraka
        self.pressure_label.grid(row=4, column=0, sticky=tk.W)  # Postavljanje labela za tlak zraka
        self.pressure_value.grid(row=4, column=1, sticky=tk.E)  # Postavljanje vrijednosti tlaka zraka

        self.clothing_label.grid(row=5, column=0, sticky=tk.W)  # Postavljanje labela za preporučenu odjeću
        self.clothing_icon.grid(row=5, column=1, sticky=tk.E)  # Postavljanje ikone za preporučenu odjeću

    def update_values(self):
        # Dohvaćanje podataka i postavljanje u label widgete
        data = self.meteo.get_data()  # Dohvaćanje podataka iz Meteo instance
        self.inside_temp_value.config(text=str(data["inside_temp"]))  # Ažuriranje vrijednosti temperature unutra
        self.outside_temp_value.config(text=str(data["outside_temp"]))  # Ažuriranje vrijednosti temperature vani
        self.city_temp_value.config(text=str(data["city_temp"]))  # Ažuriranje vrijednosti temperature u gradu
        self.humidity_value.config(text=str(data["humidity"]))  # Ažuriranje vrijednosti vlažnosti zraka
        self.pressure_value.config(text=str(data["pressure"]))  # Ažuriranje vrijednosti tlaka zraka

        # Prikazivanje ikone za odjeću ovisno o temperaturi
        temperature = data["inside_temp"]  # Dohvaćanje trenutne temperature
        image_dir = os.path.join(os.path.expanduser('~'), 'Desktop', 'MySmartHome', 'images')  # Definiranje putanje do direktorija sa slikama
        
        if temperature > 22:
            icon_path = os.path.join(image_dir, "kratki_rukavi.png")  # Putanja do ikone za kratke rukave
        elif 12 <= temperature <= 22:
            icon_path = os.path.join(image_dir, "lagana_jakna.png")  # Putanja do ikone za laganu jaknu
        elif 0 <= temperature < 12:
            icon_path = os.path.join(image_dir, "zimska_jakna.png")  # Putanja do ikone za zimsku jaknu
        else:
            icon_path = os.path.join(image_dir, "kapa_sal_zimska_jakna.png")  # Putanja do ikone za kapu, šal i zimsku jaknu

        if os.path.exists(icon_path):  # Provjera postoji li datoteka s ikonom
            icon = PhotoImage(file=icon_path)  # Učitavanje slike ikone
            self.clothing_icon.config(image=icon)  # Postavljanje slike u Label widget
            self.clothing_icon.image = icon  # Sprečavanje uklanjanja slike od strane garbage collectora
        else:
            print(f"Slika ne postoji: {icon_path}")  # Ispis upozorenja ako datoteka ne postoji

        self.parent.after(1000, self.update_values)  # Planiranje ponovnog poziva update_values metode nakon 1 sekunde (1000 ms)
