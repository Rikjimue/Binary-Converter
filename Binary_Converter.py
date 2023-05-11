# Basic Binary converter with a GUI that can convert Numbers, Letter, and characters into binary.
# This is assuming that there is no access to functions or libraries that already do this, like bin().
import math
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from ctypes import windll
from Binary_Convert_Mod import *

windll.shcore.SetProcessDpiAwareness(1)


class App(object):
    def __init__(self, master, **kwargs):
        self.master = master
        root.title("Binary Converter")
        root.geometry('800x500')
        root.resizable(False, False)
        self.create_input_textbox()
        self.create_output_textbox()
        self.create_radio_buttons()
        self.create_combobox()
        self.create_label()
        self.create_button()
        self.convert()

    def create_input_textbox(self):
        self.input_textbox = tk.Text(self.master, height=3, width=55, wrap='word', font=('Arial', 10))
        vertscroll = ttk.Scrollbar(self.master)
        vertscroll.config(command=self.input_textbox.yview)
        self.input_textbox.config(yscrollcommand=vertscroll.set)
        self.input_textbox.place(x=400, y=165, anchor=CENTER)
        vertscroll.place(x=720, y=165, anchor=CENTER, height=73)

    def create_output_textbox(self):
        self.output_textbox = tk.Text(self.master, height=3, width=55, wrap='word', state='normal', font=('Arial', 10))
        vertscroll = ttk.Scrollbar(self.master)
        vertscroll.config(command=self.output_textbox.yview)
        self.output_textbox.config(yscrollcommand=vertscroll.set)
        self.output_textbox.place(x=400, y=310, anchor=CENTER)
        vertscroll.place(x=720, y=310, anchor=CENTER, height=73)

    def create_combobox(self):
        self.convert_combobox = ttk.Combobox(self.master, height=5, width=15, state='readonly',
                                             values=['Choose an option', 'Binary to Decimal', 'Decimal to Binary', 'Word to Binary', 'Binary to Word'])
        self.convert_combobox.place(x=405, y=75, anchor=CENTER)
        self.convert_combobox.current(0)
        self.bit_combobox = ttk.Combobox(self.master, height=5, width=11, state='readonly',
                                         values=['Required Bits', '4 Bit', '8 Bit', '16 Bit'])
        self.bit_combobox.place(x=600, y=75, anchor=CENTER)
        self.bit_combobox.current(0)

    def create_label(self):
        self.label = Label(self.master, text="Binary Converter", font=("Arial Bold", 20))
        self.label.place(x=405, y=0, anchor=N)

    def create_button(self):
        self.button = Button(self.master, text='Convert', command=self.convert)
        self.button.place(x=400, y=235, anchor=CENTER)

    def create_radio_buttons(self):
        self.signed_var = IntVar()
        self.signed_var.set(1)
        self.radio_unsigned = tk.Radiobutton(self.master, text='Unsigned', variable=self.signed_var, value=1)
        self.radio_signed = tk.Radiobutton(self.master, text='Signed', variable=self.signed_var, value=2)
        self.radio_complement = tk.Radiobutton(self.master, text="2's Complement", variable=self.signed_var, value=3)
        self.radio_unsigned.place(x=200, y=105, anchor=CENTER)
        self.radio_signed.place(x=100, y=105, anchor=CENTER)
        self.radio_complement.place(x=330, y=105, anchor=CENTER)

    def convert(self):
        try:
            self.output_textbox.delete('1.0', 'end-1c')
            current_index = self.convert_combobox.current()
            entry = self.input_textbox.get('1.0', 'end-1c')
            signed = self.signed_var.get()
            try:
                if current_index == 0:
                    answer = 'Choose an option!'
                elif current_index == 1:
                    if signed == 1:
                        answer = binaryToNumber(entry)
                    elif signed == 2:
                        if entry[0] == '1':
                            answer = '-' + str(binaryToNumber(entry[1:]))
                        else:
                            answer = str(binaryToNumber(entry[1:]))
                    else:
                        answer = complementToNumber(entry)
                        self.output_textbox.insert(tk.END, answer)
                        return
                elif current_index == 2:
                    if signed == 1:
                        if entry[0] == '-':
                            answer = 'Must be a positive integer.'
                        else:
                            answer = numberToBinary(entry)
                    elif signed == 2:
                        if entry[0] == '-':
                            answer = numberToBinary(entry[1:])
                            print(answer)
                            try:
                                int(answer)
                                if self.bit_combobox.current() == 1:
                                    answer = negative_state2_check_bits(answer, 4)
                                elif self.bit_combobox.current() == 2:
                                    answer = negative_state2_check_bits(answer, 8)
                                elif self.bit_combobox.current() == 3:
                                    answer = negative_state2_check_bits(answer, 16)
                                else:
                                    answer = '1' + answer
                            except ValueError:
                                pass
                            self.output_textbox.insert(tk.END, answer)
                            return
                        else:
                            answer = '0' + numberToBinary(entry)
                    else:
                        answer = complementNumberToBinary(entry)
                elif current_index == 3:
                    if signed == 1:
                        answer = wordToBinary(entry)
                    else:
                        answer = 'Characters must be unsigned.'
                elif current_index == 4:
                    if signed == 1:
                        answer = binaryToWord(entry)
                    else:
                        answer = 'Characters must be unsigned.'
                else:
                    raise Exception('Index Error')
            except ValueError:
                answer = "Invalid Input."
            try:
                int(answer)
                if self.bit_combobox.current() == 1:
                    answer = check_bits(answer, 4)
                elif self.bit_combobox.current() == 2:
                    answer = check_bits(answer, 8)
                elif self.bit_combobox.current() == 3:
                    answer = check_bits(answer, 16)
            except ValueError:
                pass
            self.output_textbox.insert(tk.END, answer)
        except:
            answer = 'Invalid input.'
            self.output_textbox.insert(tk.END, answer)

root = tk.Tk()
app = App(root)
root.mainloop()
