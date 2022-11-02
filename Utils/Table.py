import tkinter as tk
from tkinter import ttk
from tkinter.constants import END



class Table:
    def __init__(self, vue, lines_array, modifiable_rows=True):
        self.vue = vue
        self.total_rows = len(lines_array)
        self.total_columns = len(lines_array[0])
        self.lines_array = lines_array
        self.modifiable_rows = modifiable_rows
        self.create()

    def create(self):
            for i in range(self.total_rows):
                for j in range(self.total_columns):
                    if self.modifiable_rows:
                        self.e = tk.Entry(self.vue, width=20, font=('Arial', 16, 'bold'))
                        self.e.grid(row=i, column=j)
                        self.e.insert(END, self.lines_array[i][j])
                    else:
                        block = ttk.Label(self.vue, text=self.lines_array[i][j])
                        block.grid(column=j, row=i, padx=50, sticky=tk.N)

