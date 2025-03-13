import pandas as pd
import os
from tkinter import Tk, filedialog

# Open a directory selection dialog
Tk().withdraw()  # Hide the root Tk window
directory = filedialog.askdirectory(title="Select a directory containing .tsv files")

if directory:
    # Iterate over all .tsv files in the selected directory
    for file_name in os.listdir(directory):
        if file_name.endswith(".tsv"):
            file_path = os.path.join(directory, file_name)

            # Read the TSV file (tab-separated, UTF-8 encoding)
            df = pd.read_csv(file_path, sep='\t', dtype=str, encoding="utf-8")

            # Define the output .xlsx file path
            xlsx_file_path = os.path.join(directory, os.path.splitext(file_name)[0] + ".xlsx")

            # Save as an Excel file using openpyxl
            df.to_excel(xlsx_file_path, index=False, engine="openpyxl")

            print(f"Converted: {file_name} → {os.path.basename(xlsx_file_path)}")

    print("Conversion completed.")
else:
    print("No directory selected.")
