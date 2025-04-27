import tkinter as tk
from tkinter import messagebox


def read_population_data():
    try:
        with open("population.txt", "r") as f:
            populations = [float(line.strip()) for line in f]
        if len(populations) != 41:
            raise ValueError("File must contain exactly 41 values (1950-1990)")
        return populations
    except FileNotFoundError:
        messagebox.showerror("Error", "population.txt not found")
        return None
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return None


def calculate_stats():
    populations = read_population_data()
    if not populations:
        return None

    changes = []
    for i in range(1, len(populations)):
        changes.append(populations[i] - populations[i - 1])

    avg_change = sum(changes) / len(changes)

    max_idx = changes.index(max(changes))
    max_year = 1950 + 1 + max_idx

    min_idx = changes.index(min(changes))
    min_year = 1950 + 1 + min_idx

    return avg_change, max_year, min_year


def display_stats():
    stats = calculate_stats()
    if not stats:
        return

    avg, max_year, min_year = stats

    avg_label.config(text=f"Average Annual Change: {avg:,.2f}")
    max_label.config(text=f"Year with Greatest Increase: {max_year}")
    min_label.config(text=f"Year with Smallest Increase: {min_year}")


# GUI Setup
root = tk.Tk()
root.title("Population Stats Display System")

# Header Frame
header_frame = tk.Frame(root)
header_frame.pack(pady=10)

# Title
title_label = tk.Label(
    header_frame,
    text="Population Stats Program",
)
title_label.pack(side="top", pady=5)
# Labels
avg_label = tk.Label(root, text="Average Annual Change: ")
max_label = tk.Label(root, text="Year with Greatest Increase: ")
min_label = tk.Label(root, text="Year with Smallest Increase: ")

# Buttons
button_frame = tk.Frame(header_frame)
button_frame.pack(pady=5)
display_btn = tk.Button(button_frame, text="Display Stats", command=display_stats)
quit_btn = tk.Button(button_frame, text="Quit", command=root.quit)
display_btn.pack(side="left", padx=5)
quit_btn.pack(side="left", padx=5)

# Layout
avg_label.pack(pady=5)
max_label.pack(pady=5)
min_label.pack(pady=5)
display_btn.pack(pady=10)
quit_btn.pack(pady=10)

root.mainloop()
