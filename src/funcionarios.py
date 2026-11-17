import json
from pathlib import Path

ARQUIVO_DADOS = Path(__file__).resolve().parent.parent / "data" / "funcionarios.json"


def cadastrar_funcionario():
    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
        funcionarios = json.load(arquivo)

    print("\nOlá! Para realizar seu cadastro, preencha o formulário:")

    nome = input("Digite seu nome completo: ").strip()
    idade = input("Digite sua idade: ").strip()
    cargo = input("Digite seu cargo: ").strip()
    email = input("Digite seu email: ").strip()

    if not nome or not idade or not cargo or not email:
        print("\nErro: Todos os campos são obrigatórios!")
        return

    for funcionario in funcionarios:
        if funcionario["email"].lower() == email.lower():
            print("\nEsse email já está cadastrado!")
            return

    proximo_id = max(
        [funcionario["id"] for funcionario in funcionarios],
        default=0
    ) + 1

    funcionario = {
        "id": proximo_id,
        "nome": nome,
        "idade": idade,
        "cargo": cargo,
        "email": email
    }

    funcionarios.append(funcionario)

    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(funcionarios, arquivo, ensure_ascii=False, indent=4)

    print("\nFuncionário cadastrado com sucesso!")
