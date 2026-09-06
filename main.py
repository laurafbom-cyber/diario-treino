import json
import os

ARQUIVO = "treinos.json"


def carregar_treinos():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []


def salvar_treinos(treinos):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(treinos, arquivo, ensure_ascii=False, indent=4)


def cadastrar_treino():
    print("\n=== CADASTRO DE TREINO ===")

    data = input("Data do treino: ")
    modalidade = input("Modalidade (Muay Thai/Musculação): ")
    duracao = input("Duração do treino (minutos): ")

    # Validação da intensidade
    while True:
        intensidade = input("Intensidade (1 a 10): ")

        if intensidade.isdigit() and 1 <= int(intensidade) <= 10:
            break

        print("Digite uma intensidade válida entre 1 e 10.")

    observacoes = input("Observações: ")

    novo_treino = {
        "data": data,
        "modalidade": modalidade,
        "duracao": duracao,
        "intensidade": intensidade,
        "observacoes": observacoes
    }

    treinos = carregar_treinos()
    treinos.append(novo_treino)
    salvar_treinos(treinos)

    print("\nTreino cadastrado com sucesso!")


def listar_treinos():
    treinos = carregar_treinos()

    print("\n=== MEUS TREINOS ===")

    if not treinos:
        print("Nenhum treino cadastrado.")
        return

    for numero, treino in enumerate(treinos, start=1):
        print(f"\nTreino {numero}")
        print(f"Data: {treino['data']}")
        print(f"Modalidade: {treino['modalidade']}")
        print(f"Duração: {treino['duracao']} minutos")
        print(f"Intensidade: {treino['intensidade']}/10")
        print(f"Observações: {treino['observacoes']}")


def menu():
    while True:
        print("\n=== DIÁRIO DE TREINO ===")
        print("1 - Cadastrar treino")
        print("2 - Listar treinos")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_treino()
        elif opcao == "2":
            listar_treinos()
        elif opcao == "0":
            print("Até o próximo treino!")
            break
        else:
            print("Opção inválida.")


menu()