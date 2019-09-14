# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 13:05:29 2019

@author: Owner
"""

from functools import partial
import tkinter as tk


class applikasiKalkulator(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Bend Kalkulator")
        self.membuatTombol()
        self.penentu = False

    def membuatTombol(self):
        self.layar = tk.Entry(self, width=25)
        self.layar.grid(row=0, column=0, columnspan=5)

        btn_list = [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
            '0', '+', '-',
            'C', '/', '*',
            '='
        ]
        baris = 1
        kolom = 0
        for penampung in btn_list:
            perintah = partial(self.hitung, penampung)
            if penampung == '=':
                tk.Button(self, text='=', width=22, command=perintah).grid(row=baris, column=kolom, columnspan=5)
            else :
                tk.Button(self, text=penampung, width=5, command=perintah).grid(row=baris, column=kolom)
            kolom += 1
            if kolom > 2:
                kolom = 0
                baris += 1

    def hitung(self, key):
        if key == '=':
            self.penentu = True
            try:
                result = eval(self.layar.get())
                self.layar.delete(0, tk.END)
                self.layar.insert(tk.END, str(result))
            except:
                self.layar.insert(tk.END, "")
        elif key == 'C':
            self.layar.delete(0, tk.END)
        else:
            if self.penentu :
                self.layar.delete(0, tk.END)
                self.penentu = False
            self.layar.insert(tk.END, key)

panggil = applikasiKalkulator()
panggil.mainloop()