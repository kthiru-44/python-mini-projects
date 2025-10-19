Password Manager (Tkinter GUI)

This is a simple password manager application built using Python and the Tkinter library. It allows users to securely store website credentials and generate strong random passwords.

## Features

- Graphical user interface (GUI) using Tkinter
- Password generator with random letters, numbers, and symbols
- Saves website, email/username, and password entries to a local text file
- Input validation to ensure fields are not left empty
- Clipboard copy of the generated password for convenience

## How It Works

1. Enter the website name, email/username, and either a manual or auto-generated password.
2. Click "Add" to save the data to `data.txt`.
3. Optionally, click "Generate Password" to create a secure random password automatically.
4. Passwords are saved in this format:
website | email/username | password


## Requirements

- Python 3.x
- No external libraries (uses `tkinter`, `random`, `string`, and `pyperclip` if clipboard support is added
