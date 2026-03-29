"""Библиотека для взаимодействия с PetFriends API"""

import requests
import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("BASE_URL", "https://petfriends.skillfactory.ru/")


class PetFriends:
    """Класс для работы с API PetFriends"""

    def __init__(self):
        self.base_url = BASE_URL

    def get_api_key(self, email: str, password: str) -> dict:
        """Получение API ключа для авторизации"""
        headers = {'email': email, 'password': password}
        response = requests.get(self.base_url + 'api/key', headers=headers)

        # Если статус не 200 (ошибка), возвращаем пустой словарь
        if response.status_code != 200:
            return {}

        try:
            return response.json()
        except:
            return {}

    def get_list_of_pets(self, auth_key: dict, filter: str = '') -> dict:
        """Получение списка питомцев (filter: 'my_pets' или '')"""
        # Безопасно получаем ключ
        key = auth_key.get('key', '') if isinstance(auth_key, dict) else ''
        headers = {'auth_key': key}
        params = {'filter': filter}
        response = requests.get(self.base_url + 'api/pets', headers=headers, params=params)

        # Если статус не 200 (ошибка), возвращаем пустой словарь
        if response.status_code != 200:
            return {}

        try:
            return response.json()
        except:
            return {}

    def add_new_pet_simple(self, auth_key: dict, name: str, animal_type: str, age: str) -> dict:
        """Добавление питомца без фото"""
        key = auth_key.get('key', '') if isinstance(auth_key, dict) else ''
        data = {'name': name, 'animal_type': animal_type, 'age': age}
        headers = {'auth_key': key}
        response = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, json=data)
        return response.json()

    def add_new_pet(self, auth_key: dict, name: str, animal_type: str, age: str, pet_photo: str) -> dict:
        """Добавление питомца с фото"""
        key = auth_key.get('key', '') if isinstance(auth_key, dict) else ''
        data = {'name': name, 'animal_type': animal_type, 'age': age}
        headers = {'auth_key': key}
        with open(pet_photo, 'rb') as f:
            file = {'pet_photo': (pet_photo, f, 'image/jpeg')}
            response = requests.post(self.base_url + 'api/pets', headers=headers, data=data, files=file)
        return response.json()

    def update_pet(self, auth_key: dict, pet_id: str, name: str, animal_type: str, age: str) -> dict:
        """Обновление информации о питомце"""
        key = auth_key.get('key', '') if isinstance(auth_key, dict) else ''
        data = {'name': name, 'animal_type': animal_type, 'age': age}
        headers = {'auth_key': key}
        response = requests.put(self.base_url + f'api/pets/{pet_id}', headers=headers, data=data)
        return response.json()

    def delete_pet(self, auth_key: dict, pet_id: str) -> dict:
        """Удаление питомца по ID"""
        key = auth_key.get('key', '') if isinstance(auth_key, dict) else ''
        headers = {'auth_key': key}
        response = requests.delete(self.base_url + f'api/pets/{pet_id}', headers=headers)
        if response.text == "":
            return {}
        return response.json()