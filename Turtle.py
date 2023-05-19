try:

    import turtle
    turtle.mode("logo")
    turtle.shape("turtle")
    turtle.pensize("5")
    turtle.pencolor("black")
    turtle.speed(1000)

    def pattern(m):
        turtle.forward(m)
        turtle.right(90)
        turtle.forward(m)
        turtle.right(90)
        turtle.forward(m)
        turtle.right(90)
        turtle.forward(m)
        turtle.penup()
        turtle.right(90)
        turtle.pendown()

    def up(n, x=0, y=0):
        '''Pattern goes up'''
        k = y

        for j in range(1, n+1):
            turtle.penup()
            turtle.setposition(x, k)
            turtle.pendown()
            for i in range(1, 5):

                m = i*10
                pattern(m)
            k += 40
        turtle.penup()

    def left(n, x=0, y=0):
        '''Actually goes right'''
        k = x

        for j in range(1, n+1):
            turtle.penup()
            turtle.setposition(k, y)
            turtle.pendown()
            for i in range(1, 5):

                m = i*10

                pattern(m)

            k += 40
        turtle.penup()
    last_position = 0
    word = input('Enter sentence:\n').upper()
    for i in word:
        match i:
            case 'A':
                up(4, last_position)
                left(3, last_position, 160)
                left(3, last_position, 80)
                up(5, last_position+120)
                last_position = turtle.xcor()+80
            case 'B':
                up(4, last_position)
                left(3, last_position)
                left(2, last_position, 80)
                left(3, last_position, 160)
                up(2, last_position+80)
                up(2, last_position+80, 120)
                last_position = turtle.xcor()+80
            case'C':
                left(3, last_position)
                up(4, last_position)
                left(3, last_position, 120)
                last_position = turtle.xcor()+80
            case 'D':
                up(4, last_position)
                left(3, last_position)
                left(3, last_position, 120)
                up(2, last_position+120, 40)
                last_position = turtle.xcor()+80

    turtle.hideturtle()
    turtle.exitonclick()
except:
    print('Eish')