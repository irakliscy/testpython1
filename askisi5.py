import random     
suma1, suma2, suma3= 0, 0, 0
#A
n1 = int(input('Dose to n1\n'))
n2 = int(input('Dose to n2\n'))
plithostheseon = n1*n2
#μπορούμε να φτιάξουμε τον αντίστοιχο πίνακα(-λίστα) ετσι: pinakas = [[]*n1]*n2

for _ in range(100):
    orizontio_pl, katheto_pl, diag_pl = 0, 0, 0
    pinakas = []

    for i in range(n1*n2):
        if i<=(n1*n2/2):
            pinakas.append('S')
        else:
            pinakas.append('O')
       
    random.shuffle(pinakas)       
    
    
    lista = []
    for i in range(0, plithostheseon, n1): # και μετατρέπουμε τον pinakas(1d) σε lista(2d)
        k = pinakas[i:i+n1]
        lista.append(list(k))
      
    for i in range(n2):
        for j in range(n1):
            if lista[i][j]=='S':
                try:
                    if lista[i][j+1]=='O' and lista[i][j+2]=='S':
                        orizontio_pl += 1
                except:
                    continue
                try:
                    if lista[i+1][j]=='O' and lista[i+2][j]=='S':
                        katheto_pl += 1
                except:
                    continue 
                try:
                    if lista[i+1][j+1]=='O' and lista[i+2][j+2]=='S':
                        diag_pl += 1
                except:
                    continue   
    suma1 += orizontio_pl
    suma2 += katheto_pl
    suma3 += diag_pl
    
    
print('Ο μέσος όρος οριζόντια ', suma1/100)
print('Ο μέσος όροσ κάθετα ', suma2/100)
print('Ο μέσος όρος διαγώνια(κύρια)', suma3/100)