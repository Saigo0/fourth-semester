d = "<..><.<..>><><<>>"
countMenor = 0
countMaior = 0

for i in range(len(d)):
    if d[i] == "<":
        countMenor += 1
    elif d[i] == ">":
        countMaior += 1

if countMenor < countMaior:
    print(countMenor)
else:
    print(countMaior)
