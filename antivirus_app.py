import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from ttkthemes import ThemedStyle
from antivirus_animation import AntivirusAnimation
from antivirus_cli import run_cli
from antivirus_gui import AntivirusGUI
import os

class AntivirusApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My Antivirus App")
        self.geometry("600x400")

        self.style = ThemedStyle(self)
        self.style.set_theme("breeze")  # Choose a theme that you like

        # Create a title label
        title_label = ttk.Label(self, text="My Antivirus App", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=20)

        # Create a frame for better organization
        main_frame = ttk.Frame(self)
        main_frame.pack(expand=True, fill="both")

        # Create buttons with better styling
        buttons = [
            {"text": "Scan Files", "command": self.scan_files},
            {"text": "Device Security", "command": self.device_security},
            {"text": "Network Security", "command": self.network_security},
            {"text": "Browser Control", "command": self.browser_control}
        ]

        for i, button in enumerate(buttons):
            ttk.Button(main_frame, text=button["text"], command=button["command"], style="Accent.TButton").grid(
                row=i, column=0, pady=10, padx=20, sticky="ew"
            )

        # Create a progress bar
        self.progress_bar = ttk.Progressbar(main_frame, mode="determinate", length=500)
        self.progress_bar.grid(row=len(buttons), column=0, pady=20, padx=20, sticky="ew")

        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(len(buttons), weight=1)

    def scan_files(self):
        directory = filedialog.askdirectory(title="Select Directory to Scan")
        if directory:
            self.progress_bar["value"] = 0
            self.update()
            animation = AntivirusAnimation(self, "Scanning Files", self.simulate_scan(directory))

    def device_security(self):
        animation = AntivirusAnimation(self, "Checking Device Security", self.device_security_result)

    def network_security(self):
        animation = AntivirusAnimation(self, "Checking Network Security", self.network_security_result)

    def browser_control(self):
        animation = AntivirusAnimation(self, "Controlling Browser Security", self.browser_control_result)

    def simulate_scan(self, directory):
        file_count = sum(len(files) for _, _, files in os.walk(directory))

        if file_count == 0:
            yield {"Result": "No files to scan."}
            return

        progress_per_file = 100 / file_count

        for i, (root, _, files) in enumerate(os.walk(directory), 1):
            for j, file in enumerate(files, 1):
                file_path = os.path.join(root, file)
                result = self.scan_file(file_path)
                yield {"Result": f"Scan Progress: {i}/{file_count} | Scanning: {file} ({j}/{len(files)})\n{result}"}

                self.progress_bar["value"] = min(100, self.progress_bar["value"] + progress_per_file)
                self.update()

        self.show_result("Scanning completed.")

    def scan_file(self, file_path):
        # Simulate scanning for a malicious file
        malicious_file = "malicious_file.exe"
        if os.path.basename(file_path) == malicious_file:
            return f"Malicious File Found: {file_path}"
        else:
            return f"File is Clean: {file_path}"

    def show_result(self, result):
        messagebox.showinfo("Task Completed", result)

    def device_security_result(self):
        return iter([{"Result": "Device security check completed."}])

    def network_security_result(self):
        return self.show_result("Network security check completed.")

    def browser_control_result(self):
        return self.show_result("Browser control completed.")

if __name__ == "__main__":
    app = AntivirusApp()
    app.mainloop()
