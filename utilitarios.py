# utilitarios.py

# Lista para armazenar categorias
categorias = []

# Lista para armazenar transações
transacoes = []

def cadastrar_categoria(nome):
    """
    Cadastra uma nova categoria e retorna seu identificador.
    """
    categoria = {"nome": nome}
    categorias.append(categoria)
    return categoria

def cadastrar_transacao(descricao, valor, categoria):
    """
    Cadastra uma nova transação com descrição, valor e categoria.
    """
    transacao = {
        "descricao": descricao,
        "valor": valor,
        "categoria": categoria
    }
    transacoes.append(transacao)

def saldo_total():
    """
    Calcula o saldo total somando todas as transações.
    """
    saldo = 0
    for transacao in transacoes:
        saldo += transacao["valor"]
    return saldo