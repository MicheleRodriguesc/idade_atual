def main():
  """
  Função principal do programa.
  """
  nome_completo = input("Digite seu nome completo: ")
  ano_nascimento = None

  # Validação do ano de nascimento
  while not ano_nascimento or not isinstance(ano_nascimento, int) or ano_nascimento < 1922 or ano_nascimento > 2021:
    try:
      ano_nascimento = int(input("Digite o ano de seu nascimento (entre 1922 e 2021): "))
    except ValueError:
      print("Erro: Ano inválido. Digite um número entre 1922 e 2021.")

  idade_atual = 2024 - ano_nascimento

  # Mensagem de saída
  print(f"{nome_completo}, você completou {idade_atual} anos em 2024.")


if __name__ == "__main__":
  main()
  