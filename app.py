import os
import tkinter as tk
from tkinter import filedialog, messagebox
from modules.ring import Ring
from modules.checker import check_all_properties
from modules.utils import load_ring_from_input
from modules.export import export_results_txt, export_results_csv, export_batch_results_csv

class RingCheckerApp:
    def __init__(self, root):
        self.root = root

        self.root.title("Ring Property Checker")

        self.mode_var = tk.StringVar(value="z")
        self.path_var = tk.StringVar()
        self.n_var = tk.StringVar()

        self.build_interface()
    
    def build_interface(self):
        mode_frame = tk.Frame(self.root)
        mode_frame.pack(pady=10)
        tk.Radiobutton(mode_frame, text="ℤ_n", variable=self.mode_var, value="z", command=self.toggle_mode).pack(side="left")
        tk.Radiobutton(mode_frame, text="JSON", variable=self.mode_var, value="json", command=self.toggle_mode).pack(side="left")

        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=10)
        self.n_entry = tk.Entry(self.input_frame, textvariable=self.n_var, width=10)
        self.path_entry = tk.Entry(self.input_frame, textvariable=self.path_var, width=40)
        self.browse_button = tk.Button(self.input_frame, text="Browse", command=self.browse_file)

        self.toggle_mode()

        tk.Button(self.root, text="Check Properties", command=self.run_check).pack(pady=10)

        self.results_frame = tk.Frame(self.root)
        self.export_frame = tk.Frame(self.root)
        self.export_frame.pack(pady=10)
        
        tk.Button(self.export_frame, text="Batch Check Folder", command=self.batch_check).pack(side="left", padx=5)
        tk.Button(self.export_frame, text="Export to TXT", command=self.export_txt).pack(side="left", padx=5)
        tk.Button(self.export_frame, text="Export to CSV", command=self.export_csv).pack(side="left", padx=5)
        self.current_results = None
        self.results_frame.pack()

        

    def toggle_mode(self):
        for widget in self.input_frame.winfo_children():
            widget.pack_forget()
        
        if self.mode_var.get() == "z":
            tk.Label(self.input_frame, text="Enter n:").pack(side="left")
            self.n_entry.pack(side="left")
        else:
            tk.Label(self.input_frame, text="Enter JSON file path:").pack(side="left")
            self.path_entry.pack(side="left")
            self.browse_button.pack(side="left")
    
    def browse_file(self):
        path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if path:
            self.path_var.set(path)

    def run_check(self):
        try:
            if self.mode_var.get() == "z":
                n = int(self.n_var.get())
                ring = Ring(modulo=n)
            else:
                path = self.path_var.get()
                if not path:
                    raise ValueError("No file selected")
                ring = load_ring_from_input(path)

            results = check_all_properties(ring)
            self.current_results = results
            self.display_results(results)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to check ring: {e}")

    def batch_check(self):
        folder = filedialog.askdirectory()
        if not folder:
            return

        files = [f for f in os.listdir(folder) if f.endswith(".json")]
        if not files:
            messagebox.showwarning("No JSON Files", "No .json files found in selected folder.")
            return

        batch_results = {}
        errors = []

        for filename in files:
            path = os.path.join(folder, filename)
            try:
                ring = load_ring_from_input(path)
                result = check_all_properties(ring)
                batch_results[filename] = result
            except Exception as e:
                errors.append((filename, str(e)))

        if batch_results:
            save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
            if save_path:
                export_batch_results_csv(batch_results, save_path)
                messagebox.showinfo("Exported", f"Batch results saved to {save_path}")

        if errors:
            err_msg = "\n".join(f"{f}: {msg}" for f, msg in errors)
            messagebox.showwarning("Some Files Failed", f"Errors:\n{err_msg}")

    def display_results(self, results):
        for widget in self.results_frame.winfo_children():
            widget.destroy()

        for prop, result in results.items():
            color = "green" if result["result"] else "red"
            status = "✔️" if result["result"] else "❌"
            label = f"{prop}: {status}"
            tk.Label(self.results_frame, text=label, fg=color, font=("Arial", 12, "bold")).pack(anchor="w")

            if not result["result"] and result["counterexample"] is not None:
                counter = f"    Counterexample: {result['counterexample']}"
                tk.Label(self.results_frame, text=counter, fg="gray", font=("Courier", 10)).pack(anchor="w")

    def export_txt(self):
        if not self.current_results:
            messagebox.showwarning("No Data", "Please check a ring first.")
            return
        path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if path:
            export_results_txt(self.current_results, path)
            messagebox.showinfo("Exported", f"Results saved to {path}")

    def export_csv(self):
        if not self.current_results:
            messagebox.showwarning("No Data", "Please check a ring first.")
            return
        path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if path:
            export_results_csv(self.current_results, path)
            messagebox.showinfo("Exported", f"Results saved to {path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RingCheckerApp(root)
    root.mainloop()
