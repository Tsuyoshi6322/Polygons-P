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
    if not os.path.exists(file_path):
        print("Ostrzeżenie: Plik data.txt nie istnieje.")
        return 0
        
    else:
        print("Plik data.txt istnieje.")
        return 1


def data_file_import(file_path):
    
    # TODO: Wyprowadzenie liczby punktów uzyskanych z pliku

    labels = ["A", "B", "C", "D"]
    labels_3 = ["A", "B", "C", "D"]

    with open(file_path, "r") as file:
        data = list(map(int, file.read().strip().split(";")))

    if len(data) == 8:    
        return {labels[i]: Point(data[i * 2], data[i * 2 + 1]) for i in range(4)}
    elif len (data) == 6:
        return {labels_3[i]: Point(data[i * 2], data[i * 2 + 1]) for i in range(3)}
    else:
        print("Błąd: Plik musi zawierać współrzędne dla 3 lub 4 punktów!")


def data_manual_import(file_path):

    # TODO: Warunek aby user wprowadził dane x;x;y;y;z;z;a;a a nie xxyyzzaa

    user_choice = input("Czy chcesz wprowadzić dane manualnie? (Y/N): ")
    if user_choice == 'Y':
        data_manual = input("Wprowadź współrzędne: ")
        with open(file_path, "w") as file:
            file.write(data_manual)
    else:
        print("nie tworzenie pliku")


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
    
    # Deklaracja pliku data.txt
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "data.txt")

    # Czy plik istnieje?
    exists = data_file_exists(file_path)

    if exists == 0:
        data_manual_import(file_path)

    points = data_file_import(file_path)
    print(", ".join(f"{label}{point}" for label, point in points.items()))

if __name__ == "__main__":
    main()