
valor_1 = 10
valor_2 = 26

def soma(valor_1_para_somar: float , valor_2_para_somar: float) -> float:
    """"
    Uma funcao simples de soma de valores do tipo float que retorna float
    """
    resultado_da_soma = valor_1_para_somar + valor_2_para_somar
    return resultado_da_soma

print(soma(valor_1_para_somar= valor_1, valor_2_para_somar = valor_2))



## se o parametro valor_2_para_somar nao for inserido, automaticamente sera colocado 10
def soma_(valor_1_para_somar: float , valor_2_para_somar: float = 10) -> float:
    """"
    Uma funcao simples de soma de valores do tipo float que retorna float
    """
    resultado_da_soma = valor_1_para_somar + valor_2_para_somar
    return resultado_da_soma

print(soma(valor_1_para_somar= valor_1, valor_2_para_somar = valor_2))

