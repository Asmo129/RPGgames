from tkinter import *

window = Tk()

window.title('An RPG unnecessarily ugly')
window.minsize(360, 240)
window.config(background='#232326')

screen=Label (window, text= 'print_show')
screen.pack

window.mainloop()