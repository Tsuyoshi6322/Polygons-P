import os

# =============== PUNKTY =============== 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x},{self.y})"

# =============== ZARZADZANIE PLIKIEM =============== 
def data_file_exists(file_path):
    #print("Czy plik data.txt istnieje?")
    if not os.path.exists(file_path):
        print(f"Błąd: Plik data.txt nie istnieje!")# PH


def data_file_import(file_path):
    #print("Import danych z pliku")
    labels = ["A", "B", "C", "D"]

    with open(file_path, "r") as file:
        data = list(map(int, file.read().strip().split(";")))

    return {labels[i]: Point(data[i * 2], data[i * 2 + 1]) for i in range(len(labels))}


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
    
    # Import funkcji
    script_dir = os.path.dirname(os.path.abspath(__file__))

    file_path = os.path.join(script_dir, "data.txt")

    points = data_file_import(file_path)

    print(", ".join(f"{label}{point}" for label, point in points.items()))

if __name__ == "__main__":
    main()