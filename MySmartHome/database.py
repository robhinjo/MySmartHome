import os  # Uvoz os modula za rad s operacijskim sustavom
import sqlite3  # Uvoz sqlite3 modula za rad s SQLite bazom podataka

def create_db():
    # Kreiranje direktorija ako ne postoji
    base_dir = os.path.join(os.path.expanduser('~'), 'Desktop', 'MySmartHome')  # Definiranje baznog direktorija (Desktop/MySmartHome)
    if not os.path.exists(base_dir):  # Provjera postoji li bazni direktorij; ako ne postoji,
        os.makedirs(base_dir)  # kreiraj ga

    # Apsolutna putanja do baze podataka
    db_path = os.path.join(base_dir, 'meteo_data.db')  # Definiranje apsolutne putanje do SQLite baze podataka

    conn = sqlite3.connect(db_path)  # Uspostavljanje veze s bazom podataka na navedenoj putanji
    cursor = conn.cursor()  # Stvaranje cursor objekta za izvršavanje SQL upita

    # Kreiranje tablice 'meteo' ako već ne postoji
    cursor.execute('''CREATE TABLE IF NOT EXISTS meteo (
                      id INTEGER PRIMARY KEY,
                      timestamp TEXT,
                      sensor_type TEXT,
                      value REAL)''')

    conn.commit()  # Potvrđivanje promjena u bazi podataka
    conn.close()  # Zatvaranje veze s bazom podataka nakon završetka operacija

if __name__ == "__main__":
    create_db()  # Ako se skripta pokreće izravno, pozovi funkciju create_db() za kreiranje baze podataka
