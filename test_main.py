import unittest
import json
import os
import tempfile
from unittest.mock import patch

import main


class TestDiarioTreino(unittest.TestCase):

    def test_carregar_treinos_arquivo_existente(self):
        dados = [{"data": "21/09/2026", "modalidade": "Muay Thai"}]

        with tempfile.NamedTemporaryFile(
            mode="w", delete=False, encoding="utf-8"
        ) as arquivo:
            json.dump(dados, arquivo)
            caminho = arquivo.name

        try:
            with patch.object(main, "ARQUIVO", caminho):
                resultado = main.carregar_treinos()

            self.assertEqual(resultado, dados)
        finally:
            os.remove(caminho)

    def test_carregar_treinos_arquivo_inexistente(self):
        with patch.object(main, "ARQUIVO", "arquivo_que_nao_existe.json"):
            resultado = main.carregar_treinos()

        self.assertEqual(resultado, [])

    def test_salvar_e_carregar_treinos(self):
        dados = [
            {
                "data": "21/09/2026",
                "modalidade": "Muay Thai",
                "duracao": "60",
                "intensidade": "8",
                "observacoes": "Sparring"
            }
        ]

        with tempfile.NamedTemporaryFile(delete=False) as arquivo:
            caminho = arquivo.name

        try:
            with patch.object(main, "ARQUIVO", caminho):
                main.salvar_treinos(dados)
                resultado = main.carregar_treinos()

            self.assertEqual(resultado, dados)
        finally:
            os.remove(caminho)

    @patch("builtins.input", side_effect=[
        "21/09/2026",
        "Muay Thai",
        "60",
        "8",
        "Treino forte"
    ])
    @patch("builtins.print")
    def test_cadastrar_treino(self, mock_print, mock_input):
        with patch.object(main, "ARQUIVO", "test_treinos.json"):
            main.cadastrar_treino()

            treinos = main.carregar_treinos()

        self.assertEqual(len(treinos), 1)
        self.assertEqual(treinos[0]["modalidade"], "Muay Thai")
        self.assertEqual(treinos[0]["intensidade"], "8")

        if os.path.exists("test_treinos.json"):
            os.remove("test_treinos.json")

    @patch("builtins.print")
    def test_listar_treinos_vazio(self, mock_print):
        with patch.object(main, "ARQUIVO", "arquivo_que_nao_existe.json"):
            main.listar_treinos()

        mock_print.assert_any_call("Nenhum treino cadastrado.")


if __name__ == "__main__":
    unittest.main()