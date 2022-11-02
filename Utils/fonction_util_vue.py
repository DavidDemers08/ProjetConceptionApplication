import tkinter as tk
from tkinter import ttk

class VueGen():



    def generate_button( parent,name, text,geometry, pos, dim, command):
        btn_name = 'button_' + name
        btn_text = text
        btn_width = geometry[0]
        btn_height =geometry[1]
        btn_row = pos[0]
        btn_col = pos[1]
        btn_cspan = dim[0]
        btn_rspan = dim[1]
        btn_command = command

        btn_name = ttk.Button(parent,  text=btn_text, width=btn_width)
        btn_name.grid(row=btn_row, column=btn_col, columnspan=btn_cspan, rowspan=btn_rspan, pady=(20, 0), sticky=tk.E)

    def generate_label(parent,name, text, width,borderwidth,relief, anchor,pos, dim ):
        lbl_name = name+'_label'
        lbl_text = text
        lbl_width = width
        lbl_bwitdh=borderwidth
        lbl_relief = relief
        lbl_anchor = anchor
        lbl_row = pos[0]
        lbl_col = pos[1]
        lbl_rspan = dim[0]
        lbl_cspan = dim[1]


        lbl_name = ttk.Label(parent, text=lbl_text, width=lbl_width, borderwidth=lbl_bwitdh, relief=lbl_relief)
        lbl_name.config(anchor=lbl_anchor)
        lbl_name.grid(row=lbl_row, column=lbl_col, pady=(20, 0))

