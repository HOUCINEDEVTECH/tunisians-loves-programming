# Programme Python pour dessiner
# les cercles tangents
# Import du module turtle
import turtle
#Initialisation de l’instance turtle
tur = turtle.Turtle()
# rayon du plus petit cercle
rayon =7
# nombre des cercles
nb = 3
# boucle pour dessiner les cercles tangents
for i in range(1, nb + 1, 1):
   tur.circle(rayon*i)

   # Utilisation d’une boucle pour dessiner un carré avec turtle
   # On importe le module turtle
import turtle

# Initialisation du dessinateur
tur = turtle.Turtle()
# Début de la boucle
for i in range(4):  # la boucle va tourner 4 fois
   tur.forward(20)  # Avance le dessinateur de 100 pas en avant
tur.left(90)  # Rotation du dessinateur de 90 degrés