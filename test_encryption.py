from keylogger_backend import Keylogger
import time
import os

print("Starting encryption test...")
k = Keylogger(log_dir="test_enc_logs")
k.set_encryption(True) # ENABLE ENCRYPTION
k.start()
time.sleep(1)
# Simulate key press
k.process_key_press(type('obj', (object,), {'char': 'S', 'space': False, 'enter': False})) 
k.process_key_press(type('obj', (object,), {'char': 'e', 'space': False, 'enter': False})) 
k.process_key_press(type('obj', (object,), {'char': 'c', 'space': False, 'enter': False})) 
k.process_key_press(type('obj', (object,), {'char': 'r', 'space': False, 'enter': False})) 
k.process_key_press(type('obj', (object,), {'char': 'e', 'space': False, 'enter': False})) 
k.process_key_press(type('obj', (object,), {'char': 't', 'space': False, 'enter': False})) 
k.stop()

if os.path.exists("test_enc_logs/keylog.txt"):
    with open("test_enc_logs/keylog.txt", "r") as f:
        content = f.read()
        print(f"Content: {content}")
        if "[ENCRYPTED]" in content:
            print("SUCCESS: Log content is encrypted.")
        else:
            print("FAILURE: Log content is not encrypted.")
else:
    print("FAILURE: Log file not found.")
