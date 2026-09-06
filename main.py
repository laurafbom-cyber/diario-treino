import json
import os

print("=== DIÁRIO DE TREINO ===")

data = input("Data do treino: ")
modalidade = input("Modalidade (Muay Thai/Musculação): ")
duracao = input("Duração do treino (minutos): ")
intensidade = input("Intensidade (1 a 10): ")
observacoes = input("Observações: ")

novo_treino = {
    "data": data,
    "modalidade": modalidade,
    "duracao": duracao,
    "intensidade": intensidade,
    "observacoes": observacoes
}

arquivo = "treinos.json"

if os.path.exists(arquivo):
    with open(arquivo, "r", encoding="utf-8") as f:
        treinos = json.load(f)
else:
    treinos = []

treinos.append(novo_treino)

with open(arquivo, "w", encoding="utf-8") as f:
    json.dump(treinos, f, ensure_ascii=False, indent=4)

print("\n=== TREINO REGISTRADO COM SUCESSO! ===")
print(f"Data: {data}")
print(f"Modalidade: {modalidade}")
print(f"Duração: {duracao} minutos")
print(f"Intensidade: {intensidade}/10")
print(f"Observações: {observacoes}")
