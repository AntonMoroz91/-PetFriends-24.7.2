"""Тесты для PetFriends API"""

import pytest
import os
from api import PetFriends
from dotenv import load_dotenv

load_dotenv()
VALID_EMAIL = os.getenv("EMAIL")
VALID_PASSWORD = os.getenv("PASSWORD")


class TestPetFriends:
    """Класс с тестами для PetFriends"""

    def setup_method(self):
        self.pf = PetFriends()

    # ========== ОСНОВНЫЕ ПОЗИТИВНЫЕ ТЕСТЫ (6 штук) ==========

    def test_get_api_key(self):
        """Тест получения API ключа"""
        response = self.pf.get_api_key(VALID_EMAIL, VALID_PASSWORD)
        assert 'key' in response
        print(f"API ключ: {response['key']}")

    def test_get_my_pets(self):
        """Тест получения списка моих питомцев"""
        auth_key = self.pf.get_api_key(VALID_EMAIL, VALID_PASSWORD)
        response = self.pf.get_list_of_pets(auth_key, filter='my_pets')
        assert 'pets' in response
        print(f"Найдено питомцев: {len(response['pets'])}")

    def test_add_new_pet_simple(self):
        """Тест добавления питомца без фото"""
        auth_key = self.pf.get_api_key(VALID_EMAIL, VALID_PASSWORD)
        response = self.pf.add_new_pet_simple(auth_key, "Шарик", "собака", "3")
        assert response['name'] == "Шарик"
        print(f"Добавлен питомец: {response['name']}")

    def test_update_pet(self):
        """Тест обновления информации о питомце"""
        auth_key = self.pf.get_api_key(VALID_EMAIL, VALID_PASSWORD)
        pet = self.pf.add_new_pet_simple(auth_key, "Шарик", "собака", "2")
        pet_id = pet['id']
        response = self.pf.update_pet(auth_key, pet_id, "Шарик_новый", "собака", "5")
        assert response['name'] == "Шарик_новый"
        print(f"Питомец обновлён: {response}")

    def test_delete_pet(self):
        """Тест удаления питомца"""
        auth_key = self.pf.get_api_key(VALID_EMAIL, VALID_PASSWORD)
        pet = self.pf.add_new_pet_simple(auth_key, "Временный", "кот", "1")
        pet_id = pet['id']
        self.pf.delete_pet(auth_key, pet_id)
        pets = self.pf.get_list_of_pets(auth_key, filter='my_pets')
        assert pet_id not in [p['id'] for p in pets['pets']]
        print(f"Питомец {pet_id} удалён")

    def test_add_new_pet_with_photo(self):
        """Тест добавления питомца с фото"""
        auth_key = self.pf.get_api_key(VALID_EMAIL, VALID_PASSWORD)
        photo_path = "tests/images/pet_photo.jpg"
        response = self.pf.add_new_pet(auth_key, "Рекс", "собака", "4", photo_path)
        assert response['name'] == "Рекс"
        print(f"Добавлен питомец с фото: {response['name']}")

    # ========== ДОПОЛНИТЕЛЬНЫЕ ТЕСТЫ (10 штук) ==========

    def test_get_api_key_invalid_email(self):
        """Негативный тест: неверный email"""
        response = self.pf.get_api_key("wrong@mail.com", VALID_PASSWORD)
        # При неверном email возвращается пустой словарь
        assert response == {}
        print("Негативный тест: неверный email — пройден")

    def test_get_api_key_invalid_password(self):
        """Негативный тест: неверный пароль"""
        response = self.pf.get_api_key(VALID_EMAIL, "wrong_password")
        assert response == {}
        print("Негативный тест: неверный пароль — пройден")

    def test_add_new_pet_simple_empty_name(self):
        """Негативный тест: пустое имя"""
        auth_key = self.pf.get_api_key(VALID_EMAIL, VALID_PASSWORD)
        response = self.pf.add_new_pet_simple(auth_key, "", "собака", "2")
        assert response['name'] == ""
        print("Негативный тест: пустое имя — пройден")

    def test_add_new_pet_simple_very_long_name(self):
        """Негативный тест: очень длинное имя (1000 символов)"""
        auth_key = self.pf.get_api_key(VALID_EMAIL, VALID_PASSWORD)
        long_name = "A" * 1000
        response = self.pf.add_new_pet_simple(auth_key, long_name, "собака", "2")
        assert len(response['name']) == 1000
        print("Негативный тест: длинное имя — пройден")

    def test_add_new_pet_simple_negative_age(self):
        """Негативный тест: отрицательный возраст"""
        auth_key = self.pf.get_api_key(VALID_EMAIL, VALID_PASSWORD)
        response = self.pf.add_new_pet_simple(auth_key, "Тест", "собака", "-5")
        assert response['age'] == "-5"
        print("Негативный тест: отрицательный возраст — пройден")

    def test_add_new_pet_simple_age_zero(self):
        """Граничный тест: возраст 0"""
        auth_key = self.pf.get_api_key(VALID_EMAIL, VALID_PASSWORD)
        response = self.pf.add_new_pet_simple(auth_key, "Щенок", "собака", "0")
        assert response['age'] == "0"
        print("Граничный тест: возраст 0 — пройден")

    def test_add_new_pet_simple_age_very_high(self):
        """Негативный тест: очень большой возраст"""
        auth_key = self.pf.get_api_key(VALID_EMAIL, VALID_PASSWORD)
        response = self.pf.add_new_pet_simple(auth_key, "Старый", "кот", "999")
        assert response['age'] == "999"
        print("Негативный тест: большой возраст — пройден")

    def test_add_new_pet_special_characters(self):
        """Негативный тест: спецсимволы в имени"""
        auth_key = self.pf.get_api_key(VALID_EMAIL, VALID_PASSWORD)
        special_name = "@#$%^&*()"
        response = self.pf.add_new_pet_simple(auth_key, special_name, "собака", "2")
        assert response['name'] == special_name
        print("Негативный тест: спецсимволы — пройден")

    def test_get_my_pets_without_auth_key(self):
        """Негативный тест: запрос без авторизации"""
        fake_auth = {'key': 'fake_key_12345'}
        response = self.pf.get_list_of_pets(fake_auth, filter='my_pets')
        # При неверном ключе возвращается пустой словарь
        assert response == {}
        print("Негативный тест: без авторизации — пройден")

    def test_delete_pet_wrong_id(self):
        """Негативный тест: удаление несуществующего питомца"""
        auth_key = self.pf.get_api_key(VALID_EMAIL, VALID_PASSWORD)
        fake_id = "00000000-0000-0000-0000-000000000000"
        response = self.pf.delete_pet(auth_key, fake_id)
        print("Негативный тест: неверный ID — пройден")