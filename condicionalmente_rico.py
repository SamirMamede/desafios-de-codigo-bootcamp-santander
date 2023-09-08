# Entrada de dados
saldo_total = int(input())
valor_saque = int(input())

# Criar as condições necessárias para impressão da saída, vide tabela de exemplos.
if (novo_saldo := saldo_total - valor_saque) <= saldo_total and novo_saldo > 0:
  print(f"Saque realizado com sucesso. Novo saldo: {novo_saldo}")
else:
  print(f"Saldo insuficiente. Saque nao realizado!")