import tkinter as tk
import time

def time_to_binary(current_time):
    binary_time = ''.join(format(int(digit), '04b') for digit in current_time)
    return binary_time

def update_clock():
    current_time = time.strftime('%H%M%S')
    binary_time = time_to_binary(current_time)
    for c, bit in enumerate(binary_time):
        labels[c].config(text=bit)
    hour_label.config(text=current_time[:2])
    minute_label.config(text=current_time[2:4])
    second_label.config(text=current_time[4:6])
    root.after(1000, update_clock)

root = tk.Tk()
root.title("Binary Clock")

labels = [tk.Label(root, font=('Helvetica', 20), width=2) for _ in range(24)]
for i, label in enumerate(labels[:8]):
    label.grid(row=0, column=i)
for i, label in enumerate(labels[8:16]):
    label.grid(row=1, column=i)
for i, label in enumerate(labels[16:]):
    label.grid(row=2, column=i)

hour_label = tk.Label(root, font=('Helvetica', 20), width=5)
hour_label.grid(row=0, column=8, padx=(10, 0))

minute_label = tk.Label(root, font=('Helvetica', 20), width=5)
minute_label.grid(row=1, column=8, padx=(10, 0))

second_label = tk.Label(root, font=('Helvetica', 20), width=5)
second_label.grid(row=2, column=8, padx=(10, 0))

update_clock()
root.mainloop()
