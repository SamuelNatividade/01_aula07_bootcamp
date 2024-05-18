import random
idades = []
for _ in range(50):
    idade = random.randint(1,100)
    idades.append(idade)

## 1. Calcular a media de valores em uma lista
def calcular_media_de_uma_lista(lista_com_valores: list) -> float:
    """"
    Essa funcao calcula a media de uma lista, contendo somente valores numericos
    """
    soma_lista: float  = sum(lista_com_valores)
    tamanho_da_lista: int  = len(lista_com_valores)
    media_da_lista: float  = round(soma_lista/tamanho_da_lista,2)
    return media_da_lista

print(calcular_media_de_uma_lista(lista_com_valores = idades))


# 2. Filtrar dados acima de um limite.
def filtrar_dados_acima_um_valor(lista_para_ser_filtrada: list , valor_filtro: float) -> list:
    lista_com_filtro_aplicado: list  = []
    for valor in lista_para_ser_filtrada:
        if valor > valor_filtro:
            lista_com_filtro_aplicado.append(valor)
        else:
            pass
    return lista_com_filtro_aplicado

lista_teste = range(1,10)
print(filtrar_dados_acima_um_valor(lista_para_ser_filtrada = idades, valor_filtro = 50))


## 3. Contar valores unicos de uma lista count(distinct))
def contar_valores_unicos_lista(lista:list) -> int:
    return len(set(lista))

print(contar_valores_unicos_lista(idades))