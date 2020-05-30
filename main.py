"""
Main
Calculator python
Tkinterpy
by RMP
29/05/2020
"""
from calc_factories import make_root, make_label, make_display, make_buttons
from calc_class import Calculator


def main():
    root = make_root('Calculator')
    label = make_label(root)
    display = make_display(root)
    buttons = make_buttons(root)
    calculator = Calculator(root, label, display, buttons)
    calculator.start()


if __name__ == '__main__':
    main()
