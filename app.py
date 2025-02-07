# =============== PUNKTY =============== 
class Point:
    def __inti__(self, x, y):
        self.x = x
        self.y = y

# =============== ZARZADZANIE PLIKIEM =============== 
def data_file_exists():
    print("Czy plik data.txt istnieje?")

def data_file_import():
    print("Import danych z pliku")

def data_manual_import():
    print("Dane manualnie wprowadzone")

def data_file_export():
    print("Eksport wyniku do pliku")

# =============== ZDEFINIOWANIE FIGURY =============== 
def polygon_calculate_points():
    print("Obliczenie ilosci punktow")

def polygon_is_triangle():
    print("Typ trójkąta")

def polygon_is_quadrilateral():
    print("Typ czworokąta")

def polygon_define_main():
    print("Zdefiniowanie figury")

# =============== OBLICZENIE POLA I OBWODU FIGURY =============== 
def polygon_calculate_area():
    print("Obliczenie pola figury")

def polygon_calculate_perimeter():
    print("Obliczenie obwodu figury")

def polygon_calculate_main():
    print("Wynikowe pole, figura i obwód")

# =============== MAIN =============== 
def main():
    print("Głowna funkcja")

if __name__ == "__main__":
    main()