import turtle
import random
import easygui as easy


def move(tte=turtle, x=None, y=None):
    if tte is None:
        tte = turtle.Turtle()
    tte.up()
    if x is None:
        x = tte.pos()[0]
    if y is None:
        y = tte.pos()[1]
    tte.setposition(x, y)
    tte.down()

# Initialisation du jeu
ts = turtle.getscreen()
ts.clear()
ts.bgpic("champcourse2.gif")

ts.title("Bienvenue Ã  la course des tortues !")
ts.setup (width=1400, height=800, startx=0, starty=0)






# DÃ©clarez les 5 tortues et positionnez-les sur leurs hexagones respectifs
turtleFast = []
turtleColor = ["Orange", "Deep Sky Blue", "Red", "Purple", "Dark Slate Gray"]
for x in range(0, 5):
    tt = turtle.Turtle()
    tt.shape('turtle')
    tt.color(turtleColor[x])
    turtleFast.append(tt)
    move(tte=turtleFast[x], x=-650, y=-455 + (155*(x+1)))


# Demander de saisir dans la console les prÃ©dictions des joeurus 1 et 2 dans le format 1,2,3
predictionPlayer1 = input("Donner l'odre des prédictions Player 1, ex: 2,3,1,4 : ").split(",")
predictionPlayer2 = input("Donner l'odre des prédictions Player 2, ex: 2,3,1,4 : ").split(",")


# A l'aide d'une boucle while, faire courir les tortues en tirant un nombre entre 0 et 5 qui reprÃ©sente le nombre de pixels du dÃ©placement vers la droite
distance = [0, 0, 0, 0, 0]
orderWin = []
while len(orderWin) < 4:
    for x, player in enumerate(turtleFast):
        if(distance[x] < 1380):
            speed = random.randint(0, 5)
            player.forward(speed)
            distance[x] += speed
        elif (1380 < distance[x] < 1390):
            orderWin.append(str(x))
            player.forward(11)





# Comparer les rÃ©sultats de la course avec les pronostics des joueurs
# et afficher le rÃ©sultat de la course
# et le joueur gagnant avec la tortue arbitre et l'instruction turtle.Write Ã  la position 0,0
# A IMPLEMENTER

PlayerWin = 0
for x, tt in enumerate(orderWin):
    if predictionPlayer1[x] == tt:
        PlayerWin = 1
        break
    if predictionPlayer2[x] == tt:
        PlayerWin = 2
        break
else:
    print("prout")


move(turtleFast[int(orderWin[x])], 0, 50)

turtle_arbitre = turtle.Turtle()
turtle_arbitre.goto(0,0)
turtle_arbitre.color("Black")
turtle_arbitre.write("Le joueur " + str(PlayerWin) + " à  gagné", move=True, align="left", font=("Arial", 16, "normal"))



turtle.mainloop()