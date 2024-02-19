import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from ttkthemes import ThemedStyle
from antivirus_animation import AntivirusAnimation
import os

class AntivirusApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Antivirus App")
        self.geometry("400x300")

        self.style = ThemedStyle(self)
        self.style.set_theme("plastik")

        # Create buttons
        scan_button = ttk.Button(self, text="Scan Files", command=self.scan_files)
        device_security_button = ttk.Button(self, text="Device Security", command=self.device_security)
        network_security_button = ttk.Button(self, text="Network Security", command=self.network_security)
        browser_control_button = ttk.Button(self, text="Browser Control", command=self.browser_control)

        # Create progress bar
        self.progress_bar = ttk.Progressbar(self, mode="determinate")

        # Place buttons and progress bar on the grid
        scan_button.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        device_security_button.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        network_security_button.grid(row=2, column=0, padx=20, pady=20, sticky="ew")
        browser_control_button.grid(row=3, column=0, padx=20, pady=20, sticky="ew")
        self.progress_bar.grid(row=4, column=0, padx=20, pady=20, sticky="ew")

        # Make buttons expand vertically
        self.grid_columnconfigure(0, weight=1)
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)

    def scan_files(self):
        directory = filedialog.askdirectory(title="Select Directory to Scan")
        if directory:
            animation = AntivirusAnimation(self, "Scanning Files", self.simulate_scan(directory))

    def device_security(self):
        animation = AntivirusAnimation(self, "Checking Device Security", iter([{"Result": "Device security check completed."}]))

    def network_security(self):
        animation = AntivirusAnimation(self, "Checking Network Security", lambda: self.show_result("Network security check completed."))

    def browser_control(self):
        animation = AntivirusAnimation(self, "Controlling Browser Security", lambda: self.show_result("Browser control completed."))

    def simulate_scan(self, directory):
        file_count = sum(len(files) for _, _, files in os.walk(directory))
        progress_per_file = 100 / file_count

        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                malicious_file = "malicious_file.exe"
                if os.path.basename(file_path) == malicious_file:
                    yield {"Result": "Malicious File Found"}
                else:
                    yield {"Result": "File is Clean"}
                self.progress_bar["value"] = min(100, self.progress_bar["value"] + progress_per_file)
                self.update()

        self.show_result("Scanning completed.")

    def show_result(self, result):
        messagebox.showinfo("Task Completed", result)

if __name__ == "__main__":
    app = AntivirusApp()
    app.mainloop()
