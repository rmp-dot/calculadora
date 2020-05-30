"""
Factories
Construtor de Funções
by RMP
in 29/05/2020

"""
import tkinter as tk
from typing import List


def make_root(title) -> tk.Tk:
    root = tk.Tk()
    root.title(title)
    root.config(padx=10, pady=10, background='#fff')
    root.resizable(False, False)
    return root


def make_label(root) -> tk.Label:
    label = tk.Label(
        root,
        text="Sem Valores",
        anchor="e",
        justify="right",
        background="#FFFFFF",
        foreground="#000000",
    )
    label.grid(row=0, column=0, columnspan=5, sticky="news")
    return label


def make_display(root) -> tk.Entry:
    display = tk.Entry(root)
    display.grid(row=1, column=0, columnspan=5, sticky="news", pady=(0, 10))
    display.config(
        font=("Helvetica", 25, "bold"),
        justify="right",
        bd=1,
        bg='#00BFFF',
        fg='#00008B',
        selectforeground='#000000',
        selectbackground='#FFFFFF',
        relief="flat",
        highlightthickness=1,
    )
    display.bind('<Control-a>', _display_control_a)
    return display


def _display_control_a(event):
    event.widget.select_range(0, 'end')
    event.widget.icursor('end')
    return "break"


def make_buttons(root) -> List[List[tk.Button]]:
    button_texts: List[List[str]] = [
        ["7", "8", "9", "C", "+"],
        ["4", "5", "6", "^", "-"],
        ["1", "2", "3", "/", "*"],
        ["0", ".", "=", "(", ")"],
    ]
    buttons: List[List[tk.Button]] = []

    for row_index, row_value in enumerate(button_texts, start=2):
        button_row = []
        for col_index, col_value in enumerate(row_value):
            btn = tk.Button(root, text=col_value)
            btn.grid(
                row=row_index,
                column=col_index,
                sticky='news',
                padx=5,
                pady=5,
            )
            btn.config(
                font=('Helvetica', 20, 'normal'),
                pady=10,
                width=1,
                bd=0,
                cursor="hand2",
                highlightthickness=0,
                foreground='#6A5ACD',
                background='#B0E0E6',
                highlightbackground='#FFFFFF',
                activebackground='#00BFFF',
                activeforeground='#000000',
            )
            button_row.append(btn)
        buttons.append(button_row)
    return buttons





