#nota1 = int(input("primeira nota"))
#nota2 = int(input("segunda nota "))
#media_final = (int(nota1+nota2/2))
#if media_final >= 70:
 #   print("aprovado!")
#else :
 #   print("reprovado.")

velocidade = int(input("qual a sua velocidade em km/h?"))

if  velocidade > 80:
    print("você foi multado!")
    multa = (velocidade - 80) * 5
    print(f"O valor da sua multa é R$ {multa:.2f}.")

