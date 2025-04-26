import tkinter as tk
import time

# Constants
BITS_PER_DIGIT = 3
DIGITS = 6
LABEL_FONT = ('Helvetica', 20)
LABEL_WIDTH = 2

# Color schemes
LIGHT_MODE = {'bg': '#EEE', 'fg': '#222'}
DARK_MODE = {'bg': '#222', 'fg': '#EEE'}

# Initial mode
current_mode = DARK_MODE

def time_to_binary(current_time):
    """
    Convert the current time to binary representation.
    :param current_time: str
    :return: str
    """
    return ''.join(format(int(current_time[i:i+2]), '06b') for i in range(0, len(current_time), 2))

def update_clock():
    """
    Update the clock display with the current time in binary.
    """
    current_time = time.strftime('%H%M%S')
    binary_time = time_to_binary(current_time)
    for c, bit in enumerate(binary_time):
        labels[c].config(text=bit)
    hour_label.config(text=current_time[:2])
    minute_label.config(text=current_time[2:4])
    second_label.config(text=current_time[4:6])
    root.after(100, update_clock)

def toggle_mode():
    """
    Toggle between light and dark mode.
    """
    global current_mode
    current_mode = DARK_MODE if current_mode == LIGHT_MODE else LIGHT_MODE
    root.config(bg=current_mode['bg'])
    for label in labels:
        label.config(bg=current_mode['bg'], fg=current_mode['fg'])
    hour_label.config(bg=current_mode['bg'], fg=current_mode['fg'])
    minute_label.config(bg=current_mode['bg'], fg=current_mode['fg'])
    second_label.config(bg=current_mode['bg'], fg=current_mode['fg'])
    toggle_button.config(bg=current_mode['bg'], fg=current_mode['fg'])

root = tk.Tk()
root.title("Binary Clock")
root.config(bg=current_mode['bg'])
root.resizable(False, False)

# Create and place binary labels
labels = [tk.Label(root, font=LABEL_FONT, width=LABEL_WIDTH, bg=current_mode['bg'], fg=current_mode['fg']) for _ in range(BITS_PER_DIGIT * DIGITS)]
for i in range(DIGITS):
    for j in range(BITS_PER_DIGIT):
        labels[i * BITS_PER_DIGIT + j].grid(row=i // 2, column=j + (i % 2) * BITS_PER_DIGIT)

# Create and place decimal labels
hour_label = tk.Label(root, font=LABEL_FONT, width=5, bg=current_mode['bg'], fg=current_mode['fg'])
hour_label.grid(row=0, column=8, padx=(10, 0))

minute_label = tk.Label(root, font=LABEL_FONT, width=5, bg=current_mode['bg'], fg=current_mode['fg'])
minute_label.grid(row=1, column=8, padx=(10, 0))

second_label = tk.Label(root, font=LABEL_FONT, width=5, bg=current_mode['bg'], fg=current_mode['fg'])
second_label.grid(row=2, column=8, padx=(10, 0))

# Create toggle button
toggle_button = tk.Button(root, text="Toggle Dark Mode", command=toggle_mode, bg=current_mode['bg'], fg=current_mode['fg'])
toggle_button.grid(row=3, columnspan=24)

update_clock()
root.mainloop()