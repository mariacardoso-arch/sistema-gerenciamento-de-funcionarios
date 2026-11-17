import json
from pathlib import Path

ARQUIVO_DADOS = Path(__file__).resolve().parent.parent / "data" / "funcionarios.json"


def consultar_funcionarios():
    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
        funcionarios = json.load(arquivo)

    print("\n FUNCIONÁRIOS CADASTRADOS ")

    if len(funcionarios) == 0:
        print("Nenhum funcionário cadastrado.")
    else:
        for funcionario in funcionarios:
            print("-------------------------")
            print("ID:", funcionario["id"])
            print("Nome:", funcionario["nome"])
            print("Idade:", funcionario["idade"])
            print("Cargo:", funcionario["cargo"])
            print("Email:", funcionario["email"])
