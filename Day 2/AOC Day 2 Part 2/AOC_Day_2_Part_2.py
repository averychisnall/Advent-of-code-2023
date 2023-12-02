f = open("input.txt", "r")
text = f.read()

line = text.split("\n")

gamenum = 0
total = 0

possible = True

for x in line:
    rednum = ""
    bluenum = ""
    greennum = ""
    redmax = "0"
    bluemax = "0"
    greenmax = "0"

    gamenum = gamenum + 1
    group = x.split(";")
    for y in group:
        red = y.find("red")
        blue = y.find("blue")
        green = y.find("green")

        if red != -1:
            rednum = y[red-3] + y[red-2]
            rednum.strip(' ')
            if(int(rednum) > int(redmax)):
                redmax = rednum
        else:
            rednum = "0"

        if blue != -1:
            bluenum = y[blue -3] + y[blue -2]
            bluenum.strip(' ')
            if(int(bluenum) > int(bluemax)):
                bluemax = bluenum
        else:
            bluenum = "0"

        if green != -1:
            greennum = y[green-3] + y[green-2]
            greennum.strip(' ')
            if(int(greennum) > int(greenmax)):
                greenmax = greennum
        else:
            greennum = "0"
    
    power = int(redmax) * int(bluemax) * int(greenmax)

    total = total + power

print(total)