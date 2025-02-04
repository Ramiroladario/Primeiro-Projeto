from utilitarios import (
    cadastrar_categoria,
    cadastrar_transacao,
    saldo_total,
)

# Categorias
categoria_receitas = cadastrar_categoria("Receitas")
categoria_contas = cadastrar_categoria("Contas Fixas")
categoria_viagens = cadastrar_categoria("Viagens")
categoria_lazer = cadastrar_categoria("Lazer")

# Transações
cadastrar_transacao(
    descricao="Salário JAN/2025",
    valor=2000.00,
    categoria=categoria_receitas
)

cadastrar_transacao(
    descricao="Salário FEV/2025",
    valor=2000.00,
    categoria=categoria_receitas
)

cadastrar_transacao(
    descricao="Bônus FEV/2025",
    valor=500.00,
    categoria=categoria_receitas
)

cadastrar_transacao(
    descricao="Conta de Luz FEV/2025",
    valor=-200.00,
    categoria=categoria_contas
)

cadastrar_transacao(
    descricao="Mercado JAN/2025",
    valor=-783.00,
    categoria=categoria_contas
)

cadastrar_transacao(
    descricao="Conta de Luz JAN/2025",
    valor=-83.00,
    categoria=categoria_contas
)

cadastrar_transacao(
    descricao="Conta de Luz FEV/2025",
    valor=-100.00,
    categoria=categoria_contas
)

cadastrar_transacao(
    descricao="Ingresso J&M JAN/2025",
    valor=-280.00,
    categoria=categoria_lazer
)

cadastrar_transacao(
    descricao="Gasolina para viagem FEV/2025",
    valor=-300.00,
    categoria=categoria_viagens
)

# Calcula o saldo total
total = saldo_total()

# Exibe o saldo total
print("Saldo Total: ", total)