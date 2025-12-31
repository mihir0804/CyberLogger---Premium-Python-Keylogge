# CyberLogger: Premium Python Keylogger

**Student Name:** Mihir Milind Ughade
**Project Type:** Cybersecurity / Internal Monitoring Tool

---

## Project Description
CyberLogger is a Python-based application designed to demonstrate the mechanics of keystroke logging and data obfuscation. It features a modern, dark-themed GUI built with `customtkinter` that allows users to easily Start/Stop logging and toggle encryption for anonymity.

## Key Features
* **Modern GUI:** User-friendly control panel with visual status indicators.
* **Clean Logging:** Automatically handles Backspace editing and ignores modifier keys (Shift, Ctrl, Alt) for readable output.
* **Dual Output:** Saves logs to both `keylog.txt` (readable) and `keylog.py` (script format).
* **Encryption Mode:** Features a toggle to obfuscate logs using Base64 encoding to simulate data encryption.
* **Non-Blocking:** Runs the listener in a separate thread to ensure the GUI remains responsive.

---

## Installation & Setup

### Step A: Install Requirements
Open your terminal or command prompt in this directory and run:
```bash
pip install -r requirements.txt
```
If you don't have a requirements file yet, manually install the libraries:
```bash
pip install customtkinter pynput packaging
```

### Step B: Run the Application
To launch the dashboard, run the following command:
```bash
python gui_app.py
```

---

## File Structure
* **gui_app.py:** The main entry point containing the Graphical User Interface code.
* **keylogger_backend.py:** The core logic for capturing keystrokes and handling file I/O.
* **logs/:** The directory where `keylog.txt` and `keylog.py` are saved.

---

## Disclaimer
This tool is developed for educational purposes only. It is intended to demonstrate how input monitoring works for cybersecurity research and defense analysis. Unauthorized use of keyloggers on computers you do not own or have permission to monitor is illegal.
