import numpy as np
import pandas as pd

def calcular_media(media):
    media = np.mean(lista_de_numeros)
    return media


lista_de_numeros = [12, 45, 67, 23, 89, 34, 22, 90, 56, 78]

print("Média: ", calcular_media(lista_de_numeros))


def numeros_maiores_que_a_media():

    numeros_maiores = []

    for numero in lista_de_numeros:
        if numero > calcular_media(lista_de_numeros):
            numeros_maiores.append(numero)

    return numeros_maiores


print("Números maiores que a média: ", numeros_maiores_que_a_media())


df = pd.DataFrame(
    {'Numeros Maiores que a Média': numeros_maiores_que_a_media()}
)


print("\n\n", df)

df.to_csv("maiores_que_a_media.csv", index=False)


print("Salvo com sucesso!")
