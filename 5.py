import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd
from matplotlib.ticker import FuncFormatter

class TowerPlotterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tower Plotter")

        self.create_widgets()

    def create_widgets(self):
        self.file_frame = ttk.Frame(self.root, padding=(10, 10, 10, 10), style="Border.TFrame")
        self.file_frame.pack(pady=10)

        header_label = ttk.Label(self.file_frame, text="Select Excel File", style="Header.TLabel")
        header_label.grid(row=0, column=0, columnspan=4, pady=(0, 10))

        self.file_path_label = ttk.Label(self.file_frame, text="File Path:")
        self.file_path_label.grid(row=1, column=0, padx=(0, 10), sticky='e')

        self.file_path_entry = ttk.Entry(self.file_frame, width=40, state='disabled')
        self.file_path_entry.grid(row=1, column=1)

        self.browse_button = ttk.Button(self.file_frame, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=1, column=2, padx=(5, 5))  # Added padx for a gap

        self.update_button = ttk.Button(self.file_frame, text="Update", command=self.update_plot)
        self.update_button.grid(row=1, column=3)

        self.tower_selection_frame = ttk.Frame(self.root, padding=(10, 10, 10, 10), style="Border.TFrame")
        self.tower_selection_frame.pack(pady=10)

        self.tower_checkboxes = {}
        self.create_checkbox_for_tower("Tower 1-1")
        self.create_checkbox_for_tower("Tower 1-2")
        self.create_checkbox_for_tower("Tower 2-1")
        self.create_checkbox_for_tower("Tower 2-2")
        self.create_checkbox_for_tower("Tower 3-1")
        self.create_checkbox_for_tower("Tower 3-2")

        self.plot_frame = ttk.Frame(self.root, padding=(10, 10, 10, 10), style="Border.TFrame")
        self.plot_frame.pack(pady=10, expand=True, fill=tk.BOTH)

        self.fig = Figure(figsize=(8, 6))
        self.ax = self.fig.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(expand=True, fill=tk.BOTH)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
        self.file_path_entry.config(state='normal')
        self.file_path_entry.delete(0, tk.END)
        self.file_path_entry.insert(0, file_path)
        self.file_path_entry.config(state='disabled')

    def update_plot(self):
        file_path = self.file_path_entry.get()

        if not file_path:
            messagebox.showerror("Error", "Please select an Excel file.")
            return

        try:
            df = pd.read_excel(file_path)
            self.plot_data(df)
        except Exception as e:
            messagebox.showerror("Error", f"Error reading Excel file:\n{e}")

    def plot_data(self, df):
        self.ax.clear()

        selected_towers = self.get_selected_towers()
        if not selected_towers:
            messagebox.showerror("Error", "Please select at least one tower.")
            return

        for tower in selected_towers:
            df[tower] = df[tower] / 1000
            self.ax.plot(df.index, df[tower], label=tower)

        self.ax.set_xlabel('Hours')
        self.ax.set_ylabel('Energy Consumption (KW)')
        self.ax.set_title('Energy Consumption Per Hour')
        self.ax.legend()
        self.ax.grid(True)

        self.ax.get_yaxis().set_major_formatter(FuncFormatter(lambda x, p: format(x, '.1f').rstrip('0').rstrip('.')))

        self.canvas.draw()

    def create_checkbox_for_tower(self, tower_name):
        var = tk.BooleanVar()
        checkbox = ttk.Checkbutton(self.tower_selection_frame, text=tower_name, variable=var)
        checkbox.grid(sticky='w')
        self.tower_checkboxes[tower_name] = var

    def get_selected_towers(self):
        return [tower for tower, var in self.tower_checkboxes.items() if var.get()]

if __name__ == "__main__":
    root = tk.Tk()
    app = TowerPlotterApp(root)
    root.mainloop()
