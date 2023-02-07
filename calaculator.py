# appel de bebliotheque tkinter
from tkinter import *
# forme de frame
top = Tk()
# caratcteristique de frame
top.title(" calaculator")
top.minsize("300",300)

# Les Entres
number1Label = Label( text="first number")
number1Label.pack()
number1Entry = Entry()
number1Entry.pack()

number2Label = Label( text = " seconde numnber")
number2Label.pack()
number2Entry = Entry()
number2Entry.pack()
# operation de calcul
def AddNum() :

    num1 = number1Entry.get()
    num2 = number2Entry.get()
    res= num1+num2
    resultLabel = Label(text =" the result is "  + str(res))
    resultLabel.pack()
# Affichage de resultat
but = Button ( text =" Add" , command= AddNum)

but.pack()



# affichage sur l'écran
top.mainloop()
