import os
import re
from classes import point
from .output_messages import *
from functions import output_messages


# Does the file exist? If not, create one. If it does, check its contents.
def data_file_exists(file_path):
    if not os.path.exists(file_path):
        return 0

    else:
        output_message("ok", "The file 'data.txt' exists")

        # Open the file and read its contents
        with open(file_path, "r") as file:
            output_message("status", "Validating file's contents")

            content = file.read().strip()

        # Check if the file contains only numbers (and possibly semicolons)
        if re.fullmatch(r"(\d+(\.\d+)?(;(\d+(\.\d+)?))*)?", content):
            return 1

        else:
            output_message("error", "The file 'data.txt' contains inappropriate characters")


# Importing data from a file
def data_file_import(file_path):
    labels = ["A", "B", "C", "D"]
    labels_3 = ["A", "B", "C", "D"]

    with open(file_path, "r") as file:
        output_message("status", "Splitting the data to import")
        data = file.read().strip().split(";")

    # Filter data to contain only numbers
    filtered_data = []
    output_message("status", "Filtering data")

    # Float conversion, skipping non-numeric values
    for value in data:
        try:
            filtered_data.append(float(value))

        except ValueError:
            continue

    # Check if the file contains coordinates of three or four points
    output_message("status", "Validating imported data")

    if len(filtered_data) == 8:
        output_message("ok", "File contains coordinates of four points")
        return {labels[i]: point(filtered_data[i * 2], filtered_data[i * 2 + 1]) for i in range(4)}, len(filtered_data)

    elif len(filtered_data) == 6:
        output_message("ok", "File contains coordinates of three points")
        return {labels_3[i]: point(filtered_data[i * 2], filtered_data[i * 2 + 1]) for i in range(3)}, len(filtered_data)

    else:
        output_message("error", "File must contain coordinates of three or four points")



# Validate user input for manual data entry
def data_manual_get_valid_input(user_input_prompt):
    while True:
        output_message("status", "Checking user input")

        user_input = input(user_input_prompt).strip()

        # Input is valid if it contains 6 or 8 numbers separated by semicolons
        if re.fullmatch(r"(\d+;){5}\d+" , user_input) or re.fullmatch(r"(\d+;){7}\d+", user_input):
            output_message("ok", "Input data is valid")
            return user_input

        else:
            output_message("warning", "Please provide six or eight numbers separated by semicolons (e.g. 1;1;2;2;3;3;4;4)")


# Manual data entry
def data_manual_import(file_path):
    user_choice = input(output_messages("input", "Would you like to manually input data? (Y/N)")).upper()

    if user_choice == 'Y':
        data_manual = data_manual_get_valid_input(output_messages("input", "Please provide coordinates: "))

        with open(file_path, "w") as file:
            output_message("status", "Importing manual input data")
            file.write(data_manual)

    else:
        output_message("exit", "The data has not been provided")


# Data export to a file
def data_file_export(file_path, *values):
    with open(file_path, "r") as file:
        output_message("status", "Accessing the file")
        lines = file.readlines()

    if lines:
        lines[-1] = lines[-1].strip() + ";" + ";".join(map(str, values)) + "\n"

    else:
        lines.append(";".join(map(str, values)) + "\n")

    with open(file_path, "w") as file:
        output_message("status", "Writing data to file")
        file.writelines(lines)