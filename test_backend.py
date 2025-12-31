from keylogger_backend import Keylogger
import time
import os

print("Starting backend test...")
k = Keylogger(log_dir="test_logs")
k.start()
time.sleep(1)
# Simulate manual key press injection for testing since we can't physically press keys
k.process_key_press(type('obj', (object,), {'char': 'T', 'space': False, 'enter': False})) 
k.process_key_press(type('obj', (object,), {'char': 'e', 'space': False, 'enter': False})) 
k.process_key_press(type('obj', (object,), {'char': 's', 'space': False, 'enter': False})) 
k.process_key_press(type('obj', (object,), {'char': 't', 'space': False, 'enter': False})) 
k.stop()

if os.path.exists("test_logs/keylog.txt") and os.path.exists("test_logs/keylog.py"):
    print("SUCCESS: Log files created.")
    with open("test_logs/keylog.txt", "r") as f:
        print(f"Content: {f.read()}")
else:
    print("FAILURE: Log files not found.")
