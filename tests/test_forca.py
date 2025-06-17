import unittest
import sys
import os

# Caminho absoluto para a pasta 'jogo_da_forca/cod'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'jogo_da_forca', 'cod')))

from cod.forc import exibir_palavra, escolher_palavra
ARQUIVO_PALAVRAS = os.path.join(os.path.dirname(__file__), "palavras.txt")

def carregar_palavras_txt(caminho=ARQUIVO_PALAVRAS):
    with open(caminho, 'r', encoding='utf-8') as f:
        return [linha.strip().lower() for linha in f if linha.strip()]

class TestForca(unittest.TestCase):

    def setUp(self):
        self.frutas = carregar_palavras_txt()

    def test_exibir_palavra(self):
        palavra = "banana"
        letras = {'a', 'n'}
        resultado = exibir_palavra(palavra, letras)
        self.assertEqual(resultado, "_anana")

    def test_escolher_palavra_retorna_string(self):
        palavra = escolher_palavra(self.frutas)
        self.assertIn(palavra, self.frutas)

    def test_escolher_palavra_retorna_palavra_minuscula(self):
        palavra = escolher_palavra(self.frutas)
        self.assertEqual(palavra, palavra.lower())

    def test_escolher_palavra_retorna_palavra_valida(self):
        palavra = escolher_palavra(self.frutas)
        self.assertTrue(palavra.isalpha())

    def test_escolher_palavra_lista_vazia(self):
        with self.assertRaises(IndexError):
            escolher_palavra([])

if __name__ == "__main__":
    unittest.main() 