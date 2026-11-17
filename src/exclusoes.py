import json
from pathlib import Path

ARQUIVO_DADOS = Path(__file__).resolve().parent.parent / "data" / "funcionarios.json"


def excluir_funcionario():
    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
        funcionarios = json.load(arquivo)

    if len(funcionarios) == 0:
        print("\nNenhum funcionário cadastrado.")
        return

    print("\n EXCLUSÃO DE FUNCIONÁRIO ")

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

    print("\nFuncionário encontrado:")
    print("Nome:", funcionario_encontrado["nome"])
    print("Email:", funcionario_encontrado["email"])

    confirmacao = input("\nDeseja realmente excluir? (s/n): ").strip().lower()

    if confirmacao == "s":
        funcionarios.remove(funcionario_encontrado)

        with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
            json.dump(funcionarios, arquivo, ensure_ascii=False, indent=4)

        print("\nFuncionário excluído com sucesso!")
    else:
        print("\nExclusão cancelada.")
