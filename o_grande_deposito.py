if (deposito := float(input())) > 0:
  print(f"Deposito realizado com sucesso!\nSaldo atual: R$ {deposito:.2f}")
elif deposito == 0:
  print("Encerrando o programa...")
else:
  print("Valor invalido! Digite um valor maior que zero.")

#  Imprimir a mensagem de sucesso, formatando o saldo atual (vide Exemplos).
#  Imprimir a mensagem de valor inválido.
#  Imprimir a mensagem de encerrar o programa.