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

    gamenum = gamenum + 1
    group = x.split(";")
    for y in group:
        red = y.find("red")
        blue = y.find("blue")
        green = y.find("green")

        if red != -1:
            rednum = y[red-3] + y[red-2]
            rednum.strip(' ')
        if blue != -1:
            bluenum = y[blue -3] + y[blue -2]
            bluenum.strip(' ')
        if green != -1:
            greennum = y[green-3] + y[green-2]
            greennum.strip(' ')

        if (rednum != "" and int(rednum) > 12) or (greennum != "" and int(greennum) > 13) or (bluenum != "" and int(bluenum) > 14):
            possible = False
            break
        else:
            possible = True

    if possible != False and gamenum < 101:
        total = total + gamenum

print(total)