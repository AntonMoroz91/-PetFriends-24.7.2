# PetFriends API — автоматическое тестирование

## О проекте

Проект содержит 16 автоматических тестов для REST API сервиса PetFriends.

## Быстрый старт

### 1. Установи зависимости

pip install pytest requests python-dotenv

### 2. Настрой данные

Создай файл .env в корне проекта:

EMAIL=antonmoroz1004@yandex.ru
PASSWORD=Zentpiter1925!
BASE_URL=https://petfriends.skillfactory.ru/

### 3. Добавь фото

Положи любое фото в папку tests/images/ и назови pet_photo.jpg

### 4. Запусти тесты

pytest tests/ -v -s

## Структура проекта

petfriends_10_tests/
├── tests/
│   ├── images/
│   │   └── pet_photo.jpg
│   └── test_pet_friends.py
├── api.py
├── settings.py
├── .env
├── .gitignore
└── README.md

## Тесты (16 штук)

### Позитивные (6)

1. test_get_api_key - Получение ключа
2. test_get_my_pets - Список питомцев
3. test_add_new_pet_simple - Добавление питомца
4. test_update_pet - Обновление питомца
5. test_delete_pet - Удаление питомца
6. test_add_new_pet_with_photo - Добавление с фото

### Негативные (10)

7. test_get_api_key_invalid_email - Неверный email
8. test_get_api_key_invalid_password - Неверный пароль
9. test_add_new_pet_simple_empty_name - Пустое имя
10. test_add_new_pet_simple_very_long_name - Длинное имя
11. test_add_new_pet_simple_negative_age - Отрицательный возраст
12. test_add_new_pet_simple_age_zero - Возраст 0
13. test_add_new_pet_simple_age_very_high - Возраст 999
14. test_add_new_pet_special_characters - Спецсимволы
15. test_get_my_pets_without_auth_key - Без авторизации
16. test_delete_pet_wrong_id - Неверный ID

## Ожидаемый результат

16 passed

## Безопасность

Файл .env в .gitignore - пароль не попадёт на GitHub.

## Автор: Антон Мороз
## Дата: Март 2026