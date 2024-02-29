import tkinter as tk
from tkinter import ttk
import time
import threading
import random

class AntivirusAnimation(tk.Toplevel):
    def __init__(self, parent, task, task_generator):
        super().__init__(parent)
        self.parent = parent
        self.title(task)
        self.geometry("600x150")

        self.canvas = tk.Canvas(self, width=600, height=150, bg="white")
        self.canvas.pack(expand=True, fill="both")

        # Ensure task_generator is an iterable
        self.task_generator = iter(task_generator)
        self.after(100, self.update_animation)

        self.create_background()

    def update_animation(self):
        try:
            progress_data = next(self.task_generator)
            result_text = progress_data.get('Result', '')
            self.draw_animation(result_text)
            self.after(100, self.update_animation)
        except StopIteration:
            self.destroy()
            self.parent.update()  # Update the main window

    def draw_animation(self, text):
        self.canvas.delete("all")

        # Draw background
        self.create_background()

        # Draw loading bar
        self.draw_loading_bar()

        # Draw bouncing ball
        self.draw_bouncing_ball()

        # Draw progress text
        self.draw_progress_text(text)

    def draw_loading_bar(self):
        bar_width = 400
        bar_height = 20
        progress_value = (time.time() % 2) / 2  # Simulate loading animation

        gradient_color = self.interpolate_color("#3498db", "#e74c3c", progress_value)
        self.canvas.create_rectangle(
            100, 70, 100 + bar_width * progress_value, 70 + bar_height,
            fill=gradient_color, outline="white", width=2
        )

    def draw_bouncing_ball(self):
        ball_size = 30
        ball_position = (time.time() % 2) * 400  # Simulate bouncing animation
        self.canvas.create_oval(
            100 + ball_position, 40, 100 + ball_position + ball_size, 40 + ball_size,
            fill="#2ecc71", outline="white", width=2
        )

    def draw_progress_text(self, text):
        self.canvas.create_text(300, 25, text=text, font=("Arial", 14), fill="#2c3e50")

    def interpolate_color(self, start_color, end_color, progress):
        start_color = [int(start_color[i:i+2], 16) for i in (1, 3, 5)]
        end_color = [int(end_color[i:i+2], 16) for i in (1, 3, 5)]
        r = int(start_color[0] + (end_color[0] - start_color[0]) * progress)
        g = int(start_color[1] + (end_color[1] - start_color[1]) * progress)
        b = int(start_color[2] + (end_color[2] - start_color[2]) * progress)
        return f'#{r:02x}{g:02x}{b:02x}'

    def create_background(self):
        self.canvas.create_rectangle(0, 0, 600, 150, fill="#ecf0f1")


if __name__ == "__main__":
    # Example usage with a list of task results
    task_results = [
        {"Result": "Scanning system files..."},
        {"Result": "Detecting threats..."},
        {"Result": "Scan complete. No threats found."},
    ]

    root = tk.Tk()
    animation = AntivirusAnimation(root, "Antivirus Scan", iter(task_results))
    root.mainloop()
