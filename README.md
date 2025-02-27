# Password Generator Script

## Overview

This script generates a random password based on user input and saves it to a text file. Additionally, it copies the generated password to the clipboard for easy use.

## Features

- Users can specify the type of password:
  - `a` (All characters: numbers, letters, and symbols)
  - `n` (Numbers only)
  - `l` (Letters only)
- The generated password is stored in a text file.
- The password is copied to the clipboard automatically.

## Requirements

This script requires the following Python libraries:

- `random`: Used to randomly generate characters for the password.
- `string`: Provides predefined character sets (digits, letters, punctuation).
- `pyperclip`: Copies the generated password to the clipboard.

## Installation

Before running the script, install the required dependencies using:

```sh
pip install -r requirements.txt
```

## Usage

1. Run the script in a Python environment.
2. Enter a password title when prompted.
3. Choose the type of password:
   - `a` for all characters
   - `n` for numbers only
   - `l` for letters only
4. The generated password will be displayed and stored in `Password.txt`.
5. The password is also copied to the clipboard.

## File Storage

The passwords are saved in `Password.txt` located at:

```
C:\Users\file_path\Password.txt
```

Ensure that the path is modified according to your actual directory.

## Error Handling

- If the specified file path is incorrect or inaccessible, an error message will be displayed.

## Example Run

```
Password title? MyBank
Type? [a = all, n = numbers, l = letters] a
Generated Password: G7#k8$Hf1@Qz
Test file created successfully at C:\Users\file_path\Password.txt
```

## requirements.txt

```
pyperclip
```

Ensure `pyperclip` is installed before running the script.
