'''
n = int(input(""))

if n > 1 and n < 1000:
    for i in range (1, n+1):
        print(f'{i} {i**2} {i**3}')

'''



'''
def soma(a, b):
    s = a + b

    return s


resp = soma(5,7)
print(resp)
'''

#aula do guanabara de tuplas

    #NOTA: as tuplas são imutáveis

'''
lanches = ('Hambúrger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
'''
#    for i in range (0, len(lanches)):
#       print(lanches[i])
#for comida in lanches:
#   print(comida)

#for pos, comida in enumerate(lanches):
#   print(f'{comida} na posição {pos}')

#print(sorted(lanches))

#a = (2, 4, 6)
#b = (1, 3, 5)
#c = a + b
#print(c)

#print(c,count(4)) ---> Calcula o número de vezes que um valor dentro da tupla c se repete 
#print(c.index(8)) ---> Calcula o número que corresponde ao índice de um valor dentro da tupla c 

#pessoa = ('Camila', 18, 'F')
#del(pessoa) ---> apaga a tupla inteira

'''
def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz(15)
'''

'''
def mediaNotas(n1, n2, n3):

    media = (n1 + n2 + n3)/3

    if media >= 7:
        situacao = 'Aprovado'
    elif media < 7 and media >= 4:
        situacao = 'Recuperação'
    else:
        situacao = 'Reprovado'

    return media, situacao

resposta, situacao = mediaNotas(8, 6.5, 7)
print(f"{resposta:.2f}, {situacao}")
'''

'''
def m(altura):

    altura = altura/100
    return altura

def calcularIMC(peso, altura):

    if altura >= 100:
        imc = peso/(m(altura)**2)
    else:
        imc = peso/(altura**2)

    if imc < 18.5:
        estado = 'abaixo do peso'
    elif imc < 25:
        estado = 'peso normal'  
    elif imc < 30:
        estado = 'sobrepeso'
    else:
        estado = 'obesidade'
    
    return imc, estado


resposta, estado = calcularIMC(70, 175)
print(f"IMC é {resposta:.2f}, o qual é classificado como {estado}")
'''


'''
def calcularIMC(peso, altura, unidade="metros"):
    if unidade == "cm":
        altura = altura / 100

    imc = peso / (altura ** 2)

    if imc < 18.5:
        estado = 'abaixo do peso'
    elif imc < 25:
        estado = 'peso normal'
    elif imc < 30:
        estado = 'sobrepeso'
    else:
        estado = 'obesidade'

    return imc, estado


resposta, estado = calcularIMC(70, 175, unidade="cm")
print(f"IMC é {resposta:.2f}, o qual é classificado como {estado}")
'''

'''
contpos = 0
contne = 0
contpar = 0
contimpar = 0

for n in range(1, 6):

    n = int(input(''))


    if n > 0:
        contpos += 1
    elif n < 0:
        contne += 1

    if n % 2 == 0:
        contpar += 1
    elif n % 2 != 0:
        contimpar += 1

print(f"{contpar} valor(es) par(es)")
print(f"{contimpar} valor(es) impar(es)")
print(f"{contpos} valor(es) positivo(s)") 
print(f"{contne} valor(es) negativo(s)") 
'''

'''
x = int (input(''))
y = int (input(''))
soma = 0

if (x > y):
    a = x
    x = y
    y = a


i = x + 1

while i < y and x != y:

    if i % 2 != 0:
        soma += i

    i += 1


print(soma)
'''


'''
n = int(input(''))

if n > 2 and n < 1000:
    for i in range (1, 11):
        print(f'{i} x {n} = {i*n}')
'''

'''
n = int(input(''))
i = 1

for i in range (i, n + 1):

    n1, n2, n3 = input().split() #poderia fazer: n1, n2, n3 = map(float, input().split()) 
    n1 = float(n1)               #para condensar tudo na mesma linha
    n2 = float(n2)
    n3 = float(n3)

    mediap = (n1*2 + n2*3 + n3*5)/10
    print(f'{mediap:.1f}')
'''

'''
n = 1
m = 2

while n > 0 and m > 0:
    
    n, m = map(int, input().split())
    
    if n > 0 and m > 0:
        if (n > m):
            a = n
            n = m
            m = a
    
        i = n
        soma = 0

        for i in range(i, m + 1):
            soma += i
            print(i, end="n")
        print(f'Sum={soma}')
       
    else:
        break
'''


'''
while True:
    
    senha = input("")

    if senha == '2002':
        break

    else:
        print('Senha Invalida')
        

print('Acesso Permitido')
'''

'''
while True:

    x, y = map(int, input().split())

    if x != 0 and y != 0:

        if x > 0 and y > 0:
            print('primeiro')

        elif x < 0 and y > 0:
            print('segundo')

        elif x < 0 and y < 0:
            print('terceiro')

        elif x > 0 and y < 0:
            print('quarto')

    else:
        break
'''

'''
i = 0
novanota = 0

while (i < 2):

    n1 = float(input(''))

    if n1 >= 0 and n1 <= 10:
        novanota += n1
        i += 1
    else:
        print('nota invalida')


    n2 = float(input(''))

    if n2 >= 0 and n2 <= 10:
        novanota += n2
        i += 1
        
    else:
        print('nota invalida')

media = (novanota)/2       
print(f'media = {media:.2f}')
'''

'''
x = int(input('')) 
y = int(input('')) 

if x > 0 and y > 0:
    if x > y:
        a = x
        x = y
        y = a

    i = x + 1

    for i in range(i, y):
        if (i % 5 == 2) or (i % 5 == 3):
            print(i)
'''

'''
n = int(input(''))

if n > 0:
    for i in range(1, 4*n + 1):
        if i % 4 == 0:
            print('PUM',)
            
        else:
            print(i, end=' ')
'''


'''
n = int(input(''))


if n > 1 and n < 13:
    i = 1
    fatorial = 1
    
    for i in range (1, n+1):
        fatorial = fatorial*i


    print(fatorial)
'''
'''
n = int(input(''))
cont = 0

if n > 0:
    for i in range(n):

        x = int(input())
        cont = 0

        if x > 1 and x <= 10000000:
            i = 2
            if x != 2 and x != 3 and x != 7:
                while(i < x):
                    if x % i == 0:
                        cont += 1
                        break
                    i += 1
                
                if cont > 0:
                    print(f'{x} nao eh primo')
                else:
                    print(f'{x} eh primo')
            else:
                print(f'{x} eh primo')
'''







    






      
    

      


