# Programme Python pour dessiner
# les cercles tangents
# Import du module turtle
import turtle
#Initialisation de l’instance turtle
tur = turtle.Turtle()
# rayon du plus petit cercle
rayon = 10
# nombre des cercles
nb = 10
# boucle pour dessiner les cercles tangents
for i in range(1, nb + 1, 1):
   tur.circle(rayon*i)