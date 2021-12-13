from tkinter import*
from tkinter.messagebox import*
from module1 import*

letters=read_from_file("letters.txt")
numbers=read_from_file("numbers.txt")
one=read_from_file("one.txt")
two=read_from_file("two.txt")
three=read_from_file("three.txt")
four=read_from_file("four.txt")
five=read_from_file("five.txt")
six=read_from_file("six.txt")
seven=read_from_file("seven.txt")
eight=read_from_file("eight.txt")
nine=read_from_file("nine.txt")

window=Tk()
window.title("Число имени!")
window.geometry("1500x900")

lbl=Label(window, text="Узнаем число твоего имени!\nВведи имя:", font="Arial 20", fg="blue" )
ent=Entry(window, font="Arial 30", fg="blue", bg="grey")
btn=Button(window, text="Нажми меня, как введёшь имя", font="Arial 18", fg="blue", command=lambda:name_number(letters,numbers,ent.get().lower(),lbl3))
lbl2=Label(window, text="Число твоего имени: ", font="Coral 14", fg="blue",)
lbl3=Label(window, font="Coral 10", bg="#FDD9B5",  fg="black")


lbl.pack()
ent.pack()
btn.pack()
lbl2.pack(side=LEFT)
lbl3.pack(side=RIGHT)

window.mainloop()