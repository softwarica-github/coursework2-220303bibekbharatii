import tkinter as tk
from tkinter import filedialog, messagebox

class AntivirusGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Advanced Antivirus GUI")
        self.geometry("400x200")

        # Create buttons
        scan_button = tk.Button(self, text="Scan Files", command=self.scan_files)
        device_security_button = tk.Button(self, text="Device Security", command=self.device_security)
        network_security_button = tk.Button(self, text="Network Security", command=self.network_security)
        browser_control_button = tk.Button(self, text="Browser Control", command=self.browser_control)

        # Place buttons on the grid
        scan_button.grid(row=0, column=0, padx=10, pady=10)
        device_security_button.grid(row=0, column=1, padx=10, pady=10)
        network_security_button.grid(row=1, column=0, padx=10, pady=10)
        browser_control_button.grid(row=1, column=1, padx=10, pady=10)

    def scan_files(self):
        directory = filedialog.askdirectory(title="Select Directory to Scan")
        if directory:
            messagebox.showinfo("Scanning Files", f"Scanning files in directory:\n{directory}")

    def device_security(self):
        messagebox.showinfo("Device Security", "Checking device security...")

    def network_security(self):
        messagebox.showinfo("Network Security", "Checking network security...")

    def browser_control(self):
        messagebox.showinfo("Browser Control", "Controlling browser security...")

if __name__ == "__main__":
    app = AntivirusGUI()
    app.mainloop()
