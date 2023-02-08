# appel de bebliotheque tkinter
from tkinter import *
# forme de frame
top = Tk()
# caratcteristique de frame
top.title(" calaculator")
top.minsize("300",300)

# Les Entres
number1Label = Label( text="ENTRE N")
number1Label.pack()
number1Entry = Entry()
number1Entry.pack()


# operation de calcul
def DOUBELNUM() :

    num1 =  float(number1Entry.get())
    res = num1*2
    resultLabel = Label(text =" the result is "  + str(res))
    resultLabel.pack()
# Affichage de resultat
but = Button ( text =" VALIDER L OPERATION " , command= DOUBELNUM )

but.pack()



# affichage sur l'écran
top.mainloop()
