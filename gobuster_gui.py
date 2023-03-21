import tkinter as tk
from tkinter import filedialog
import subprocess

class App:
    def __init__(self, master):
        self.master = master
        master.title("Gobuster Scanner")

        self.target_frame = tk.Frame(master)
        self.target_label = tk.Label(self.target_frame, text="Target URL:")
        self.target_entry = tk.Entry(self.target_frame, width=50)
        self.target_label.pack(side="left")
        self.target_entry.pack(side="right")
        self.target_frame.pack()

        self.extensions_frame = tk.Frame(master)
        self.extensions_label = tk.Label(self.extensions_frame, text="Select file extensions to scan (comma-separated):")
        self.extensions_entry = tk.Entry(self.extensions_frame)
        self.extensions_label.pack(side="left")
        self.extensions_entry.pack(side="right")
        self.extensions_frame.pack()

        self.wordlist_frame = tk.Frame(master)
        self.wordlist_label = tk.Label(self.wordlist_frame, text="Select wordlist file:")
        self.wordlist_button = tk.Button(self.wordlist_frame, text="Browse", command=self.select_wordlist)
        self.wordlist_label.pack(side="left")
        self.wordlist_button.pack(side="right")
        self.wordlist_frame.pack()

        self.results_frame = tk.Frame(master)
        self.scrollbar = tk.Scrollbar(self.results_frame)
        self.scrollbar.pack(side="right", fill="y")
        self.results_text = tk.Text(self.results_frame, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.results_text.yview)
        self.results_text.pack(side="left", fill="both", expand=True)
        self.results_frame.pack()

        self.scan_button = tk.Button(master, text="Scan", command=self.scan)
        self.scan_button.pack()

    def select_wordlist(self):
        self.wordlist_path = filedialog.askopenfilename()

    def scan(self):
        url = self.target_entry.get()
        extensions = self.extensions_entry.get()
        wordlist = self.wordlist_path
        command = f"gobuster -u {url} -w {wordlist} -x {extensions} -t 20"
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        self.results_text.insert(tk.END, output)

root = tk.Tk()
app = App(root)
root.mainloop()
