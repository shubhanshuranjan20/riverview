import tkinter as tk
from tkinter import filedialog, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd

class TowerPlotterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tower Plotter")

      
        self.style = ttk.Style()
        self.style.configure("Header.TLabel", foreground="white", background="#4CAF50", font=('Helvetica', 14, 'bold'))
        self.style.configure("Border.TFrame", background="#4CAF50")

        self.create_widgets()

    def create_widgets(self):
      
        self.file_frame = ttk.Frame(self.root, padding=(10, 10, 10, 10), style="Border.TFrame")
        self.file_frame.pack(pady=10)

        header_label = ttk.Label(self.file_frame, text="Select Excel File", style="Header.TLabel")
        header_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))

        self.file_path_label = ttk.Label(self.file_frame, text="File Path:")
        self.file_path_label.grid(row=1, column=0, padx=(0, 10), sticky='e')

        self.file_path_entry = ttk.Entry(self.file_frame, width=40, state='disabled')
        self.file_path_entry.grid(row=1, column=1)

        self.browse_button = ttk.Button(self.file_frame, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=1, column=2)

        self.plot_frame = ttk.Frame(self.root, padding=(10, 10, 10, 10), style="Border.TFrame")
        self.plot_frame.pack(pady=10)

        self.fig = Figure(figsize=(8, 6))
        self.ax = self.fig.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack()

        
        self.plot_button = ttk.Button(self.root, text="Update Plot", command=self.update_plot)
        self.plot_button.pack(pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
        self.file_path_entry.config(state='normal')
        self.file_path_entry.delete(0, tk.END)
        self.file_path_entry.insert(0, file_path)
        self.file_path_entry.config(state='disabled')

    def update_plot(self):
        file_path = self.file_path_entry.get()

        if not file_path:
            tk.messagebox.showerror("Error", "Please select an Excel file.")
            return

        try:
            df = pd.read_excel(file_path)
            self.plot_data(df)
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error reading Excel file:\n{e}")

    def plot_data(self, df):
        self.ax.clear()

        self.ax.plot(df.index, df['Tower 1-1'], label='Tower 1-1', color='red')
        self.ax.plot(df.index, df['Tower 1-2'], label='Tower 1-2', color='green')
        self.ax.plot(df.index, df['Tower 2-1'], label='Tower 2-1', color='blue')
        self.ax.plot(df.index, df['Tower 2-2'], label='Tower 2-2', color='orange')
        self.ax.plot(df.index, df['Tower 3-1'], label='Tower 3-1', color='purple')
        self.ax.plot(df.index, df['Tower 3-2'], label='Tower 3-2', color='brown')

        self.ax.set_xlabel('Index')
        self.ax.set_ylabel('Tower Values')
        self.ax.set_title('Tower Values vs Index')
        self.ax.legend()
        self.ax.grid(True)

        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = TowerPlotterApp(root)
    root.mainloop()
    
    



