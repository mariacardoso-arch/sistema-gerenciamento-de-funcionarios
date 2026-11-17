import json
from pathlib import Path

ARQUIVO_DADOS = Path(__file__).resolve().parent.parent / "data" / "funcionarios.json"


def atualizar_funcionario():
    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
        funcionarios = json.load(arquivo)

    if len(funcionarios) == 0:
        print("\nNenhum funcionário cadastrado.")
        return

    print("\n--- ATUALIZAÇÃO DE FUNCIONÁRIO ---")

    try:
        id_funcionario = int(input("Digite o ID do funcionário: "))
    except ValueError:
        print("\nDigite um ID válido!")
        return

    funcionario_encontrado = None

    for funcionario in funcionarios:
        if funcionario["id"] == id_funcionario:
            funcionario_encontrado = funcionario
            break

    if funcionario_encontrado is None:
        print("\nFuncionário não encontrado!")
        return

    print("\nDeixe o campo vazio para manter a informação atual.")

    nome = input("Novo nome (" + funcionario_encontrado["nome"] + "): ").strip()
    idade = input("Nova idade (" + funcionario_encontrado["idade"] + "): ").strip()
    cargo = input("Novo cargo (" + funcionario_encontrado["cargo"] + "): ").strip()
    email = input("Novo email (" + funcionario_encontrado["email"] + "): ").strip()

    if nome:
        funcionario_encontrado["nome"] = nome

    if idade:
        funcionario_encontrado["idade"] = idade

    if cargo:
        funcionario_encontrado["cargo"] = cargo

    if email:
        for funcionario in funcionarios:
            if funcionario["id"] != id_funcionario and funcionario["email"].lower() == email.lower():
                print("\nEsse email já está cadastrado!")
                return

        funcionario_encontrado["email"] = email

    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(funcionarios, arquivo, ensure_ascii=False, indent=4)

    print("\nFuncionário atualizado com sucesso!")
