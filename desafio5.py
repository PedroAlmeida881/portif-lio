print('Data de vida')
print('-'*20)
print('Digite seu nome:')
nome=input()
def calcular(idade):
    return (idade * 365)
print('Digite sua idade:')
idade= int(input ())
dias = calcular(idade)
print('Olá',nome+", você já viveu ", dias, "dias.") 
