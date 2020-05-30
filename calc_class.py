"""
Calculator Class
Objetivo: Manipular as características da Calculadora
"""
import re
import math
import tkinter as tk
from typing import List
from pprint import pprint


class Calculator:
    """Calculator"""

    def __init__(self, root, label, display, buttons):
        self.root: tk.Tk = root
        self.label: tk.Label = label
        self.display: tk.Entry = display
        self.buttons: List[List[tk.Button]] = buttons

    def start(self):
        self._config_display()
        self._config_button()
        self.display.focus()
        self.root.mainloop()

    def clear(self, event=None):
        self.display.delete(0, 'end')
        self.label.config(text='Sem Valores')

    def add_text_to_display(self, event=None):
        self.display.insert('end', event.widget['text'])

    def _fix_text(self, text):
        display = self.display
        # element don't want to None
        new_text = re.sub(r'[^\d\.\/\+\-\*\^\(\)e]', r'', text, 0)
        # repeated to signal
        new_text = re.sub(r'([\+\-\/\*\^\.])\1+', r'\1', new_text, 0)
        # signals (), *() to none
        new_text = re.sub(r'\*?\(\)', r'', new_text, 0)
        return new_text

    def _get_equations(self, text):
        return re.split(r'\^', text)

    def exec_calc(self, event=None):
        fixed_text = self._fix_text(self.display.get())
        equations = self._get_equations(fixed_text)
        try:
            # if one clause
            if len(equations) == 1:
                result = eval(self._fix_text(equations[0]))
            else:
                result = eval(self._fix_text(equations[0]))
                for equation in equations[1:]:
                    result = math.pow(result, eval(self._fix_text(equation)))

            self.display.delete(0, 'end')
            self.display.insert('end', result)
            self.label.config(text=f'{fixed_text} = {result}')

        except OverflowError:
            self.label.config(text="Limit Overflow")
        except Exception as e:
            self.label.config(text=f"Calc Error! in ({fixed_text})")

    def _config_display(self):
        self.display.bind('<Return>', self.exec_calc)
        self.display.bind('<KP_Enter>', self.exec_calc)

    def _config_button(self):
        buttons = self.buttons
        for row_values in buttons:
            for button in row_values:
                button_text = button['text']
                # buttons event
                if button_text == 'C':
                    button.bind('<Button-1>', self.clear)
                    button.config(fg='#000000', bg='#FF6347')
                if button_text in '0123456789/*+-.^()':
                    button.bind('<Button-1>', self.add_text_to_display)
                    if button_text in '/*+-^()':
                        button.config(fg='#000000', bg='#6495ED')
                if button_text == '=':
                    button.bind('<Button-1>', self.exec_calc)
                    button.config(fg='#000000', bg='#90EE90')
