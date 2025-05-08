import os  # Uvoz os modula za rad s operacijskim sustavom
import random  # Uvoz random modula za generiranje slučajnih brojeva
from sense_emu import SenseHat  # Uvoz SenseHat emulatora za simulaciju podataka senzora
import sqlite3  # Uvoz sqlite3 modula za rad s SQLite bazom podataka
from datetime import datetime  # Uvoz datetime modula za rad s datumima i vremenima

class Meteo:
    def __init__(self):
        # Apsolutna putanja do baze podataka
        base_dir = os.path.join(os.path.expanduser('~'), 'Desktop', 'MySmartHome')  
        # Definiranje baznog direktorija koristeći funkciju os.path.join za pravilno spajanje putanja.

        db_path = os.path.join(base_dir, 'meteo_data.db')  
        # Definiranje apsolutne putanje do SQLite baze podataka 'meteo_data.db' unutar direktorija 'MySmartHome'.

        self.sense = SenseHat()  
        # Stvaranje instancije SenseHat objekta za čitanje podataka senzora.

        self.conn = sqlite3.connect(db_path)  
        # Uspostavljanje veze s bazom podataka na navedenoj putanji.

        self.create_table()  
        # Pozivanje metode create_table() za kreiranje tablice u bazi podataka ako ne postoji.

    def create_table(self):
        cursor = self.conn.cursor()  
        # Stvaranje cursor objekta za izvršavanje SQL upita.

        cursor.execute('''CREATE TABLE IF NOT EXISTS meteo (
                          id INTEGER PRIMARY KEY,
                          timestamp TEXT,
                          sensor_type TEXT,
                          value REAL)''')  
        # SQL upit za kreiranje tablice 'meteo' s poljima:
        # id - cijeli broj, primarni ključ,
        # timestamp - tekst, za pohranu vremena očitanja,
        # sensor_type - tekst, za vrstu senzora (npr. temperatura, vlažnost, tlak),
        # value - realni broj, za vrijednost očitanja.
        # Tablica se kreira samo ako već ne postoji u bazi podataka.

        self.conn.commit()  
        # Potvrđivanje promjena u bazi podataka.

    def get_inside_temperature(self):
        return round(self.sense.get_temperature(), 2)  
        # Dohvaćanje trenutne temperature s SenseHat senzora i zaokruživanje na 2 decimale.

    def get_outside_temperature(self):
        return round(self.sense.get_temperature() - random.uniform(1, 5), 2)  
        # Simulacija vanjske temperature oduzimanjem slučajne vrijednosti između 1 i 5 od trenutne temperature sa senzora.

    def get_city_temperature(self):
        return round(self.sense.get_temperature() + random.uniform(1, 5), 2)  
        # Simulacija gradske temperature dodavanjem slučajne vrijednosti između 1 i 5 trenutnoj temperaturi sa senzora.

    def get_humidity(self):
        return round(self.sense.get_humidity(), 2)  
        # Dohvaćanje trenutne vlažnosti zraka s SenseHat senzora i zaokruživanje na 2 decimale.

    def get_pressure(self):
        return round(self.sense.get_pressure(), 2)  
        # Dohvaćanje trenutnog tlaka zraka s SenseHat senzora i zaokruživanje na 2 decimale.

    def log_data(self, sensor_type, value):
        cursor = self.conn.cursor()  
        # Stvaranje cursor objekta za izvršavanje SQL upita.

        cursor.execute("INSERT INTO meteo (timestamp, sensor_type, value) VALUES (?, ?, ?)",
                       (datetime.now(), sensor_type, value))  
        # SQL upit za umetanje novog očitanja u tablicu 'meteo'.
        # Umetanje trenutnog vremena (datetime.now()), vrste senzora (sensor_type) i vrijednosti očitanja (value).

        self.conn.commit()  
        # Potvrđivanje promjena u bazi podataka.

    def get_data(self):
        data = {
            "inside_temp": self.get_inside_temperature(),
            "outside_temp": self.get_outside_temperature(),
            "city_temp": self.get_city_temperature(),
            "humidity": self.get_humidity(),
            "pressure": self.get_pressure()
        }  
        # Kreiranje rječnika s podacima o trenutnim očitanjima senzora.

        for sensor_type, value in data.items():
            self.log_data(sensor_type, value)  
            # Logiranje svakog očitanja u bazu podataka.

        return data  
        # Vraćanje rječnika s podacima o trenutnim očitanjima senzora.
