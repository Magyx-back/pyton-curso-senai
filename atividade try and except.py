#atividade 1

try:
    n = int(input('numero:'))
except ValueError as erro:
    print(erro)   

#atividade 2

try:
    a = int(input("Digite o primeiro número: ")) 
    b = int(input("Digite o segundo número: "))
    
    resultado = a / b

except ZeroDivisionError:
    print("nao foi possivel dividor o numero")

except ValueError:
    print("digite apenas numeros")

else:
    print(resultado)
    print("Seu número foi dividido com sucesso!")

finally:
    print("Fim do programa.")

    #atividae 3

lista = ["a", "b", "c"]

try:
    posicao = (int(input('digite uma posicao de a a c')))
    print(lista[posicao])

except IndexError:
    print('deu erro pois a posicao nao existe')

finally:
    print('fim do programa')










