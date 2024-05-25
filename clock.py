import tkinter as tk
from tkinter import messagebox
import time

class CountdownTimerApp:
    def __init__(self, master):
        self.master = master
        master.title("Countdown Timer")
        master.configure(bg='black')
        master.overrideredirect(True)

        self.canvas = tk.Canvas(master, width=300, height=300, bg='black', highlightthickness=0)
        self.canvas.pack(expand=True)

        self.countdown_active = False
        self.ship_radius = 100
        self.ship = self.canvas.create_oval(150-self.ship_radius, 150-self.ship_radius, 150+self.ship_radius, 150+self.ship_radius, outline='yellow', width=10)
        self.time_text = self.canvas.create_text(150, 150, text="00:00:00", fill="white", font=("Arial", 24))

        self.label = tk.Label(master, text="Enter time:", fg='white', bg='black')
        self.label.pack()

        self.hours_entry = tk.Entry(master, width=5)
        self.hours_entry.insert(tk.END, "0")
        self.hours_entry.pack(side=tk.LEFT)

        self.minutes_entry = tk.Entry(master, width=5)
        self.minutes_entry.insert(tk.END, "0")
        self.minutes_entry.pack(side=tk.LEFT)

        self.seconds_entry = tk.Entry(master, width=5)
        self.seconds_entry.insert(tk.END, "0")
        self.seconds_entry.pack(side=tk.LEFT)

        self.start_button = tk.Button(master, text="Start", command=self.start_countdown, bg='yellow')
        self.start_button.pack(side=tk.LEFT)

        self.reset_button = tk.Button(master, text="Reset", command=self.reset_timer, bg='yellow')
        self.reset_button.pack(side=tk.RIGHT)

    def start_countdown(self):
        if self.countdown_active:
            messagebox.showinfo("Countdown Timer", "Timer is already active. Please reset to start again.")
            return

        try:
            hours = int(self.hours_entry.get())
            minutes = int(self.minutes_entry.get())
            seconds = int(self.seconds_entry.get())
            total_seconds = hours * 3600 + minutes * 60 + seconds
            if total_seconds <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter valid time values.")
            return

        self.countdown_active = True
        self.update_countdown(total_seconds)

    def update_countdown(self, remaining):
        if remaining < 0:
            remaining = 0

        hours = remaining // 3600
        minutes = (remaining % 3600) // 60
        seconds = remaining % 60
        time_string = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
        self.canvas.itemconfig(self.time_text, text=time_string)

        if remaining == 0:
            self.countdown_active = False
            messagebox.showinfo("Countdown Timer", "Time's up!")
        else:
            self.master.after(1000, self.update_countdown, remaining - 1)

    def reset_timer(self):
        self.canvas.coords(self.ship, 150-self.ship_radius, 150-self.ship_radius, 150+self.ship_radius, 150+self.ship_radius)
        self.canvas.itemconfig(self.time_text, text="00:00:00")
        self.countdown_active = False

def main():
    root = tk.Tk()
    app = CountdownTimerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
