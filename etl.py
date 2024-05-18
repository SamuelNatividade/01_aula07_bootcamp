import csv 

path_arquivo = "vendas.csv"

def ler_csv(nome_do_arquivo_csv: str) -> list[dict]:
    """
    Funcao que le um arquivo csv e retonar uma lista de dicionarios
    """
    lista = []
    with open(nome_do_arquivo_csv, mode = "r", encoding = "utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista



def filtrar_produtos_entregues(lista: list[dict]) -> list[dict]:
    """
    Funcao que filtra produtos entregues
    """
    lista_com_produtos_filtrados = []
    for produto in lista:
        if produto.get("entregue") == "True":
            lista_com_produtos_filtrados.append(produto)
    return lista_com_produtos_filtrados

lista_de_produtos = ler_csv(path_arquivo)
produtos_entregues = filtrar_produtos_entregues(lista_de_produtos)

def somar_valores_dos_produtos_entregues(lista: list[dict]) -> float:
    """
    Funcao que calcula o valor total da lista
    """
    valor_total = 0
    for produto in lista:
        valor_total += int(produto.get("price"))
    return valor_total

lista_de_produtos = ler_csv(path_arquivo)
produtos_entregues = filtrar_produtos_entregues(lista_de_produtos)
valor_total = somar_valores_dos_produtos_entregues(produtos_entregues)