import os
from classes import *
from functions.file_management import data_manual_import, data_file_exists
from functions.polygon_definition import polygon_define_main
from functions.perimeter_area_calculation import polygon_calculate_main
from functions.output_messages import *

# Declaration of the file path
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "data.txt")

# Does the file exist?
exists = data_file_exists(file_path)

# When it doesn't...
if exists == 0:
    output_message("warning", "The file 'data.txt' does not exist")
    data_manual_import(file_path)

# When it does...
elif exists == 1:
    output_message("ok", "The file 'data.txt' is valid")
    pass

# Rounding parameter
epsilon = 0.01

# Define the polygon
polygon_define_main(file_path, epsilon)

# Calculate the area and perimeter
polygon_calculate_main(file_path, epsilon)

# End of program
output_message("exit", "End of program")
exit()