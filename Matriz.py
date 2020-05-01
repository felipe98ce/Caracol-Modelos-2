matriz = []

dimension = int(input("# Filas columnas"))
caracol = dimension
borde1 = dimension
borde2 = 0
numalter = 0
dim1 = 1
dim2 = 2
dim3 = 3
dim4 = 4

for i in range(dimension):
    matriz.append([0]*dimension)
    
for a in range(dimension):
    for b in range(dimension):
        matriz[a][b] = int(numalter)
        numalter += 1

"print(matriz)"

for a in range(dimension):
    for b in range(dimension):
        print(matriz[a][b],end=' ')
    print()

for s in range((dimension*2)-1):
    if s/dim1 == 1:
        if borde1 == dimension:
            for t in range(dimension):
                print(matriz[borde2+1][t], end=' ')
            dim1 += 3
            caracol -= 1
            borde2 += 1
        else:
            for t in range(borde1):
                print(matriz[borde2+1][t], end=' ')
            dim1 += 3
            caracol -= 1
            borde2 += 1
            borde1 -= 1
    else:
        if s/dim2 == 1:
            for w in range(borde1 - 1):
                print(matriz[w+1][borde1], end=' ')
            dim1 += 3
        else:
            if s / dim3 == 1:
                for x in range(borde1 -1):
                    print(matriz[borde1][x], end=' ')
                dim1 += 3
                caracol -= 1
                borde1 -= 1
            else:
                if s / dim4 == 1:
                    for y in range(borde1 - 1):
                        print(matriz[y][borde2], end=' ')
                    dim1 += 3






