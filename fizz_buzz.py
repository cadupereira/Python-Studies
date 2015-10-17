print ("MEU PRIMEIRO PROGRAMA EM PYTHON")
a = int(input("Entre um numero:"))
if a < 101:
    if a%3==0:
        print("COOL: Possivel dividir por 3, resposta:", a//3)
    elif a:
        print("Impossivel dividir por 3")
    if a%5==0:
        print("COOL: Possivel dividir por 5, resposta:", a//5)
    elif a:
        print ("Impossivel dividir por 5")
elif a: 
    print ("Fora do limite definido")
