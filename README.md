# Requirements File Updater

This Python script is designed to update package versions in a `requirements.txt` file based on the currently installed packages in your Python environment.

## Purpose
The script helps maintain consistent package versions by:
1. Reading the current installed package versions (from `requirements1.txt`)
2. Updating the versions in your project's `requirements.txt` file
3. Preserving any package extras (e.g., `package[extra]`) and package name casing

## Prerequisites
- Python 3.x
- Two files in the same directory as the script:
  - `requirements.txt`: Your project's original requirements file
  - `requirements1.txt`: A file containing the output of `pip freeze`

## How to Use

1. First, generate a freeze file of your current environment:
```bash
pip freeze > requirements1.txt
```

2. Run the script:
```bash
python updater.py
```

## Features
- Handles multiple file encodings (utf-8, utf-16, ascii)
- Preserves package extras (e.g., `package[extra]`)
- Maintains original package name casing
- Provides verbose output of updates and warnings
- Skips commented lines (starting with #)

## Example Output
```
Found package: numpy with version: 1.21.0
Found package: pandas with version: 1.3.0
Updated numpy to version 1.21.0
Updated pandas to version 1.3.0
Warning: Version not found for some-package

Updated requirements.txt successfully!
```

## Error Handling
- Provides clear error messages for file reading issues
- Attempts multiple encodings when reading files
- Preserves original requirements if packages are not found in the freeze file

## Note
Make sure to backup your original `requirements.txt` file before running the script, as it will overwrite the existing file with the updated versions.
