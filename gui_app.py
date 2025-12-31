import customtkinter
import os
import subprocess
from keylogger_backend import Keylogger

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Premium Keylogger - CyberProject")
        self.geometry(f"{700}x500") # Increased size for tabs

        # FIX: Handle window closing event to stop background threads
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # configure grid layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # backend
        self.keylogger = Keylogger(log_dir="logs")

        # Create Sidebar
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="CyberLogger", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        self.status_label = customtkinter.CTkLabel(self.sidebar_frame, text="Status: Stopped", text_color="red", font=customtkinter.CTkFont(size=14))
        self.status_label.grid(row=1, column=0, padx=20, pady=10)

        # Create Tabview
        self.tabview = customtkinter.CTkTabview(self, width=500)
        self.tabview.grid(row=0, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.tabview.add("Controls")
        self.tabview.add("Future Scope")
        self.tabview.tab("Controls").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Future Scope").grid_columnconfigure(0, weight=1)

        # --- Controls Tab ---
        self.title_label = customtkinter.CTkLabel(self.tabview.tab("Controls"), text="Control Panel", font=customtkinter.CTkFont(size=24, weight="bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=20)

        self.buttons_frame = customtkinter.CTkFrame(self.tabview.tab("Controls"), fg_color="transparent")
        self.buttons_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        self.buttons_frame.grid_columnconfigure((0,1), weight=1)

        self.start_button = customtkinter.CTkButton(self.buttons_frame, text="START KEYLOGGER", fg_color="green", hover_color="darkgreen", command=self.start_logging, height=50)
        self.start_button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.stop_button = customtkinter.CTkButton(self.buttons_frame, text="STOP KEYLOGGER", fg_color="red", hover_color="darkred", command=self.stop_logging, state="disabled", height=50)
        self.stop_button.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.open_logs_button = customtkinter.CTkButton(self.tabview.tab("Controls"), text="Open Logs Directory", command=self.open_logs)
        self.open_logs_button.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        # Encryption Toggle
        self.encryption_switch = customtkinter.CTkSwitch(self.tabview.tab("Controls"), text="Enable Log Encryption (Anonymity)", command=self.toggle_encryption)
        self.encryption_switch.grid(row=3, column=0, padx=20, pady=(10, 20))

        # --- Future Scope Tab ---
        self.scope_label = customtkinter.CTkLabel(self.tabview.tab("Future Scope"), text="Future Roadmap", font=customtkinter.CTkFont(size=24, weight="bold"))
        self.scope_label.grid(row=0, column=0, padx=20, pady=20)
        
        features = [
            "Logging Mechanisms (Implemented)",
            "Data Storage (Implemented)", 
            "Encryption and Anonymity (Implemented)",
            "User Interface (Implemented)",
            "Protection Mechanisms (Planned)",
            "Legitimate Use Case (Planned)", 
            "Security Enhancements (Planned)",
            "Legal Research (Ongoing)",
            "Testing and Validation (Ongoing)"
        ]

        self.scrollable_frame = customtkinter.CTkScrollableFrame(self.tabview.tab("Future Scope"), label_text="Project Roadmap")
        self.scrollable_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        for i, feature in enumerate(features):
            label = customtkinter.CTkLabel(self.scrollable_frame, text=f"◉ {feature}", anchor="w", justify="left")
            label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
            if "(Implemented)" in feature:
                label.configure(text_color="lightgreen")

    def toggle_encryption(self):
        is_on = self.encryption_switch.get()
        self.keylogger.set_encryption(bool(is_on))
        print(f"Encryption set to: {bool(is_on)}")

    def start_logging(self):
        self.keylogger.start()
        self.status_label.configure(text="Status: Running", text_color="green")
        self.start_button.configure(state="disabled", fg_color="gray")
        self.stop_button.configure(state="normal", fg_color="red")
        self.encryption_switch.configure(state="disabled") # Lock settings while running
        print("Keylogger Started")

    def stop_logging(self):
        self.keylogger.stop()
        self.status_label.configure(text="Status: Stopped", text_color="red")
        self.start_button.configure(state="normal", fg_color="green")
        self.stop_button.configure(state="disabled", fg_color="gray")
        self.encryption_switch.configure(state="normal")
        print("Keylogger Stopped")

    def open_logs(self):
        log_dir = os.path.abspath(self.keylogger.log_dir)
        try:
            if os.name == 'nt':  # Windows
                os.startfile(log_dir)
            elif os.name == 'posix':  # macOS/Linux
                subprocess.call(('open', log_dir))
        except FileNotFoundError:
            print(f"Log directory not found: {log_dir}")

    # FIX: Clean exit method
    def on_closing(self):
        print("Closing application...")
        if self.keylogger.is_running:
            self.keylogger.stop()
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
