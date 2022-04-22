import turtle as t

def rechthoek(horizontaal, verticaal, kleur):
    t.pendown()
    t.pensize(1)
    t.color(kleur)
    t.begin_fill()
    for teller in range(1, 3):
        t.forward(horizontaal)
        t.right(90)
        t.forward(verticaal)
        t.right(90)
    t.end_fill()
    t.penup()
    t.speed('slow')
    t.bgcolor('Dodger blue')


        # voeten
        t.goto(-100, -150)
        rechthoek(50, 20, 'blue')
        t.goto(-30, -150)
        rechthoek(50, 20, 'blue')

        # benen
        t.goto(-25, -50)
        rechthoek(15, 100, 'grey')
        t.goto(-90, 100)
        rechthoek(-12, 100)

        # lichaam
        t.goto(-90, 100)
        rechthoek(100, 150, 'red')

        # armen
        t.goto(-150, 70)
        rechthoek(60, 15, 'grey')
        t.goto(-150, 110)
        rechthoek(55, 110)

        t.goto(55, 70)
        rechthoek(60, 15, 110)
        t.goto(55, 110)
        rechthoek(15, 40, 'grey')

        #nek
        t.goto(-50, 120)
        rechthoek(15, 20 , 'grey')

        #hoofd
        t.goto(-85, 170)
        rechthoek(80, 50, 'red')

        # ogen
        t.goto(-60, 160)
        rechthoek(30, 10, 'white')
        t.goto(-55, 155)
        rechthoek(5, 5, 'black')
        t.goto(-40, 155)
        rechthoek(5, 5, 'black')

        # mond
        t.goto(-65, 135)
        rechthoek(40, 5, 'black')










