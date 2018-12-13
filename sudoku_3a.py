import random

line = [[0, 0, 0, 0, 0, 0, 0, 0, 0] for x in range(9)]
column = [[0, 0, 0, 0, 0, 0, 0, 0, 0] for x in range(9)]
block = [[0, 0, 0, 0, 0, 0, 0, 0, 0] for x in range(9)]
series = [[[1, 2, 3, 4, 5, 6, 7, 8, 9] for x in range(9)] for y in range(9)]

i = 0
j = 0
while j < 9:
    if len(series[i][j]) > 0:
        luck = random.choice(series[i][j])
        k = int((j // 3) * 3 + i // 3)
        n = int((j % 3) * 3 + i % 3)
        # sprawdz_kolizji()
        if line[i].count(luck) == 0 and column[j].count(luck) == 0 and block[k].count(luck) == 0:
            # zmiana_miejsc()
            line[i][j] = luck
            column[j][i] = luck
            block[k][n] = luck
            series[i][j].remove(luck)
            # zwiekszenie_ij()
            if i < 8:
                i = i + 1
            else:
                i = 0
                j = j + 1
        else:
            # usuniecie()
            series[i][j].remove(luck)
    else:
        series[i][j] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # zmniejszenie_ij()
        if i > 0:
            i = i - 1
        else:
            if j > 0:
                i = 8
                j = j - 1
            else:
                j = 10
        # ponowne_0()
        k = int((j // 3) * 3 + i // 3)
        n = int((j % 3) * 3 + i % 3)
        line[i][j] = 0
        column[j][i] = 0
        block[k][n] = 0

for item in range(0, 9):
    print(line[item])
