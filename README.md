# Polygons-P (Uni project)
---
## Main functionality
Calculate the area and perimeter of trapezoidal figures specified by the user with four points (*x*, *y*). 
The data is read from an input file "data.txt" or entered by the user and appended to the input file.

The results are output to the same file. 
The program also determines whether the given coordinates form:
- Trapezoid
- Rectangle
- Square
- Equilateral triangle
- Isosceles triangle
- Scalene triangle 
- or do not form any of these figures. (out-of-scope)

### Input example

>*1;1;2;1;1;2;2;2*\
*1;1;2;1;1;2;2;20*

### Output example
>*1;1;2;1;1;2;2;2;	1;	4;	square*\
*1;1;2;1;1;2;2;20;	0;	0; polygon out-of-scope*

---
## Example run

1. Load coordinates from the file "data.txt" or input them manually
2. Calculate the area and permiter of the polygon and define it's type.
3. Output the results next to the input in the file "data.txt".