1. Wczytaj dane z pliku “dane.txt”
    - “dane.txt” zawiera cztery punkty (x,y), z których można utworzyć figury trapezoidalne.
    - format tych danych to (x1;y1 x2;y2 x3;y3 x4; y4).
    - plik można tworzyć, edytować, lub usunąć w programie.
2. Przeanalizuj punkty w pliku dane.txt i dodaj do niego nazwę figury
    - edycja danych w pliku dane.txt
    - do formatu (x1;y1 x2;y2 x3;y3 x4;y4 | figura)
    - Dostępne figury:
    trapez, prostokąt, kwadrat,
    trójkąt równoboczny, równoramienny, różnoboczny
3. Oblicz pola powierzchni i obwody figur zgodnie z wymiarami
    - Długości wektorów pomiędzy Px1 a Px2 etc.
    - Wyprowadź dane do konsoli
    - Zapisz dane do pliku ‘output.txt’
    

Przykład wejścia  - Format (x1;y1;x2;y2;x3;y3;x4;y4)

<span style="color:blue;">Data.txt <br></span>
<span style="color:blue;">1;1;2;1;1;2;2;2 <br></span>
<span style="color:blue;">1;1;2;1;1;2;2;20 <br></span>

Przykład wyjścia w formacie (x1;y1;x2;y2;x3;y3;x4;y4; pole; obwód; figura)

<span style="color:red;">1;1;2;1;1;2;2;2;1;4; kwadrat<br></span>
<span style="color:red;">1;1;2;1;1;2;2;20;0;0; figura nie poprawna<br></span>
###