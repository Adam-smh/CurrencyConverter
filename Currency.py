from tkinter import *
import requests

root = Tk()
root.title("Currency Converter")
root.config(bg='#EB5E28')
root.geometry("400x500")



value = IntVar()


class CC:
    def __init__(self, window):
        self.value = Label(window, font=("Sans serif", 20), text="USD")
        self.value.place(relx="0.4", rely="0.1")
        self.value.config(bg="#EB5E28")

        self.value_entry = Entry(window, textvariable=value)
        self.value_entry.place(relx="0.3", rely="0.2")

        self.con_entry = Entry(window)
        self.con_entry.place(relx="0.3", rely="0.3")

        self.con = Label(window, text="")
        self.con.place(relx="0.66", rely="0.7")
        self.con.config(bg="#EB5E28")

        self.convert = Label(root, text="Amount: ")
        self.convert.place(relx="0.3", rely="0.7")
        self.convert.config(bg="#EB5E28")

        self.btn = Button(root, command=self.conversion, text="Convert", width=20)
        self.btn.place(relx="0.3", rely="0.8")

    def conversion(self):
        req = 'https://v6.exchangerate-api.com/v6/ddccd8b4e623a3f196cb430a/latest/' + self.con_entry.get()
        data = requests.get(req).json()
        res = int(self.value_entry.get()) * data["conversion_rates"]["USD"]
        self.convert.config(text=res)


CC(root)
root.mainloop()
