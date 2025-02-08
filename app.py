import os
import re

# =============== PUNKTY =============== 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x},{self.y})"

# =============== ZARZADZANIE PLIKIEM =============== 
# Czy plik istnieje? Jeśli nie, to utwórz go
def data_file_exists(file_path):
    if not os.path.exists(file_path):
        print("Warning: Plik data.txt nie istnieje.")
        return 0
    
    else:
        print("Plik data.txt istnieje.")

        with open(file_path, "r") as file:
            content = file.read().strip()
            print("Sprawdzanie zawartości pliku...")

        if re.fullmatch(r"(\d+;)*\d+", content):
            print("Plik data.txt zawiera tylko liczby... OK")
            return 1
        else:
            print("Error: Plik data.txt zawiera niepoprawne znaki!")
            return -1

# Import danych z pliku
def data_file_import(file_path):
    labels = ["A", "B", "C", "D"]
    labels_3 = ["A", "B", "C", "D"]

    with open(file_path, "r") as file:
        data = list(map(int, file.read().strip().split(";")))

    if len(data) == 8:    
        return {labels[i]: Point(data[i * 2], data[i * 2 + 1]) for i in range(4)}, len(data)
    elif len (data) == 6:
        return {labels_3[i]: Point(data[i * 2], data[i * 2 + 1]) for i in range(3)}, len(data)
    else:
        print("Error: Plik musi zawierać współrzędne dla 3 lub 4 punktów!")
        return None, len(data)

# Warunek aby user wprowadził dane x;x;y;y;z;z; a nie xxyyzz
def data_manual_get_valid_input(user_input_prompt):
    while True:
        user_input = input(user_input_prompt).strip()

        # Wymagana poprawność formatu (6 lub 8 liczb oddzielonych średnikami)
        if re.fullmatch(r"(\d+;){5}\d+" , user_input) or re.fullmatch(r"(\d+;){7}\d+", user_input):
            return user_input
        else:
            print("Error: Proszę podać 6 lub 8 liczb oddzielonych średnikami (np. 1;1;2;2;3;3;4;4)")

# Manualne wprowadzenie danych przez użytkownika i wprowadzenie ich do pliku
def data_manual_import(file_path):
    user_choice = input("Czy chcesz wprowadzić dane manualnie? (Y/N): ")
    if user_choice == 'Y':
        data_manual = data_manual_get_valid_input("Wprowadź dane: ")

        with open(file_path, "w") as file:
            file.write(data_manual)

    else:
        print("nie tworzenie pliku")

# Eksport danych do pliku - dopisanie wartości
def data_file_export(file_path, *values):
    with open(file_path, "r") as file:
        lines = file.readlines()

    if lines:
        lines[-1] = lines[-1].strip() + ";" + ";".join(map(str, values)) + "\n"
    else:
        lines.append(";".join(map(str, values)) + "\n")

    with open(file_path, "w") as file:
        file.writelines(lines)        

# =============== ZDEFINIOWANIE FIGURY =============== 

# Typ figury
def polygon_calculate_points(file_path):
    points, pointsCount = data_file_import(file_path)

    if pointsCount == 6 or pointsCount == 8:
        polygon = "valid" # Placeholder value
        point_a = points.get("A")
        point_b = points.get("B")
        point_c = points.get("C")
        point_d = points.get("D")

    else:
        print("Error: Out of scope")
        exit()

    # Czy występuje kolinearność?
    def polygon_are_collinear(p1, p2, p3, p4=None):
        collinear = p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y)
        return collinear

    if point_d is None:
        collinear = polygon_are_collinear(point_a, point_b, point_c)
    else:
        collinear = polygon_are_collinear(point_a, point_b, point_c)
        + polygon_are_collinear(point_a, point_b, point_d)
        + polygon_are_collinear(point_a, point_c, point_d)
        + polygon_are_collinear(point_b, point_c, point_d)
    
    if collinear == 0:
        print("Error: To nie jest figura!")
        polygon = "Brak"
    else:
        if pointsCount == 6:
            polygon = "trójkąt"
        elif pointsCount == 8:
            polygon = "czworokąt"
        else:
            print("Error: Out of scope")
            polygon = "inny wielokąt"

    return polygon

# Typ trójkąta    
def polygon_is_triangle():
    print("Typ trójkąta")

# Typ czworokąta
def polygon_is_quadrilateral():
    print("Typ czworokąta")

# Wynikowa figura
def polygon_define_main(file_path):
    print("Zdefiniowanie figury")
    polygonDefined = "Zdefiniowana figura"
    data_file_export(file_path, polygonDefined)

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

    if exists == 0: # Gdy plik data.txt nie istnieje
        data_manual_import(file_path)
    elif exists == 1: # Gdy istnieje
        pass
    else: # Gdy są w nim błędy
        exit()


# =============== TEST FUNCTIONS =============== 
    points,_ = data_file_import(file_path)
    print(", ".join(f"{label}{point}" for label, point in points.items()))

    text =polygon_calculate_points(file_path)
    print(text)

# =============== MAIN EXEC =============== 
if __name__ == "__main__":
    main()