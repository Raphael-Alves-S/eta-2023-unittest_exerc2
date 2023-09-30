from unittest import TestCase

from src.phonebook import Phonebook


class TestPhonebook(TestCase):

    def test_add_successful(self):
        phonebook = Phonebook()
        response = phonebook.add("Ana", "(11)9999-8888")
        self.assertEqual('Registro adicionado', response)

    def test_add_invalid_number(self):
        phonebook = Phonebook()
        response = phonebook.add("Julia", "")
        self.assertEqual('Número invalido', response)

    def test_add_none_number(self):
        phonebook = Phonebook()
        response = phonebook.add("Julia", None)
        self.assertEqual('Nome ou número não é um valor válido', response)

    def test_add_invalid_name(self):
        phonebook = Phonebook()
        response = phonebook.add("@", "(11)9999-8888")
        self.assertEqual('Nome invalido', response)

    def test_add_none_name(self):
        phonebook = Phonebook()
        response = phonebook.add(None, "(11)9999-8888")
        self.assertEqual('Nome ou número não é um valor válido', response)

    def test_lookup_name_valid(self):
        phonebook = Phonebook()
        phonebook.add("Marta", "(11)9999-8888")
        response = phonebook.lookup("Marta")
        self.assertEqual("Marta: (11)9999-8888", response)

    def test_lookup_name_invalid_string(self):
        phonebook = Phonebook()
        phonebook.add("Marta", "(11)9999-8888")
        response = phonebook.lookup("#")
        self.assertEqual("Nome invalido", response)

    def test_lookup_name_none(self):
        phonebook = Phonebook()
        phonebook.add("Marta", "(11)9999-8888")
        response = phonebook.lookup(None)
        self.assertEqual("Nome não é um valor válido", response)

    def test_lookup_nonexistent_name(self):
        phonebook = Phonebook()
        phonebook.add("Marta", "(11)9999-8888")
        response = phonebook.lookup("Joao")
        self.assertEqual("Registro não encontrado", response)

    def test_get_names_default(self):
        phonebook = Phonebook()
        response = phonebook.get_names()
        self.assertEqual(['POLICIA', 'BOMBEIRO'], response)

    def test_get_names_empty(self):
        phonebook = Phonebook()
        phonebook.clear()
        response = phonebook.get_names()
        self.assertEqual("Phonebook não possui registro", response)

    def test_get_names_add_new_user(self):
        phonebook = Phonebook()
        phonebook.add("Marta", "(11)9999-8888")
        response = phonebook.get_names()
        self.assertListEqual(['POLICIA', 'BOMBEIRO', 'Marta'], response)

    def test_get_numbers_default(self):
        phonebook = Phonebook()
        response = phonebook.get_numbers()
        self.assertListEqual(['190', '193'], response)

    def test_get_numbers_empty(self):
        phonebook = Phonebook()
        phonebook.clear()
        response = phonebook.get_numbers()
        self.assertEqual("Phonebook não possui registro", response)

    def test_get_numbers_add_new_user(self):
        phonebook = Phonebook()
        phonebook.add("Marta", "(11)9999-8888")
        response = phonebook.get_numbers()
        self.assertListEqual(['190', '193', '(11)9999-8888'], response)

    def test_clear_user(self):
        phonebook = Phonebook()
        phonebook.add("Maria", "(12)9999-8888")
        response = phonebook.clear()
        self.assertEqual('Dados do phonebook foram limpos', response)

    def test_clear_phonebook_isempty(self):
        phonebook = Phonebook()
        phonebook.clear()
        response = phonebook.clear()
        self.assertEqual('O phonebook está vazio', response)

    def test_search_name_exist(self):
        phonebook = Phonebook()
        response = phonebook.search('BOMBEIRO')
        self.assertEqual("Registro encontrado: BOMBEIRO: 193", response)

    def test_search_name_notexist(self):
        phonebook = Phonebook()
        response = phonebook.search('Joao')
        self.assertEqual("Registro não encontrado", response)

    def test_phonebook_sorted(self):
        phonebook = Phonebook()
        phonebook.add("Maria", "(13)9999-99999")
        response = phonebook.get_phonebook_sorted()
        self.assertEqual([['BOMBEIRO', '193'], ['Maria', '(13)9999-99999'], ['POLICIA', '190']], response)

    def test_phonebook_reverse(self):
        phonebook = Phonebook()
        phonebook.add("Maria", "(13)9999-99999")
        response = phonebook.get_phonebook_reverse()
        self.assertEqual([['POLICIA', '190'], ['Maria', '(13)9999-99999'], ['BOMBEIRO', '193']], response)
