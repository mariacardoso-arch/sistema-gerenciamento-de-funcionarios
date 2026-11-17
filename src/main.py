from funcionarios import cadastrar_funcionario
from consultas import consultar_funcionarios
from atualizacoes import atualizar_funcionario
from exclusoes import excluir_funcionario


def menu():
    while True:
        print("\n===== SISTEMA DE GERENCIAMENTO DE FUNCIONÁRIOS =====")
        print("1 - Cadastrar funcionário")
        print("2 - Consultar funcionários")
        print("3 - Atualizar funcionário")
        print("4 - Excluir funcionário")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_funcionario()

        elif opcao == "2":
            consultar_funcionarios()

        elif opcao == "3":
            atualizar_funcionario()

        elif opcao == "4":
            excluir_funcionario()

        elif opcao == "0":
            print("\nEncerrando o sistema...")
            break

        else:
            print("\nOpção inválida! Tente novamente.")


menu()