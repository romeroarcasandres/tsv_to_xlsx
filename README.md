# TSV to XLSX Converter

The **tsv_to_xlsx.py** automates the conversion of all `.tsv` files in a selected directory into `.xlsx` format.

---

## Overview

This tool allows users to:
- **Batch Process Files:** Select a directory and convert all `.tsv` files to `.xlsx`.
- **Preserve Data Structure:** Ensures data integrity while converting files.
- **Save Output Automatically:** The converted `.xlsx` files are saved in the same directory.

---

## Requirements

- **Python 3**
- **Libraries:**
  - `pandas`
  - `tkinter` (standard with Python)
  - `openpyxl` (Install via `pip install openpyxl`)

---

## Usage

1. Run the `tsv_to_xlsx.py` script.
2. A file dialog will prompt you to choose the folder containing the `.tsv` files.
3. The script scans all `.tsv` files in the selected directory, converts each of them into an `.xlsx` format, and saves them in the same directory with the `.xlsx` extension.

---

## Important Notes

- **No Direct Batch Conversion in Excel:**  
  This script helps users avoid manually opening and saving `.tsv` files as `.xlsx`, especially when working with multiple files.

- **File Integrity:**  
  The script ensures that the data structure remains intact during conversion.

- **Large Files:**  
  Very large `.tsv` files may require more processing time.

- **Backup Recommendation:**  
  Always keep a backup of your original TSV files before running the script.

---

## License

This project is available under the CC BY-NC 4.0 license. For complete details, please refer to the LICENSE file included with this project.
