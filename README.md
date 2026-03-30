# PetFriends API — автоматическое тестирование

Проект содержит 16 автоматических тестов для REST API сервиса PetFriends.

## Структура проекта

- petfriends_10_tests/
  - tests/
    - images/
      - pet_photo.jpg
    - test_pet_friends.py
  - api.py
  - settings.py
  - .env
  - .gitignore
  - README.md

## Быстрый старт

1. Установи зависимости:
   pip install pytest requests python-dotenv

2. Настрой данные:
   Создай файл .env в корне проекта:
   EMAIL=твой_email@
   PASSWORD=твой_пароль
   BASE_URL=https://petfriends.skillfactory.ru/

3. Добавь фото:
   Положи любое фото в папку tests/images/ и назови pet_photo.jpg

4. Запусти тесты:
   pytest tests/ -v -s

## Тесты (16 штук)

Позитивные (6)
1. test_get_api_key — получение ключа
2. test_get_my_pets — список питомцев
3. test_add_new_pet_simple — добавление питомца
4. test_update_pet — обновление питомца
5. test_delete_pet — удаление питомца
6. test_add_new_pet_with_photo — добавление с фото

Негативные (10)
7. test_get_api_key_invalid_email — неверный email
8. test_get_api_key_invalid_password — неверный пароль
9. test_add_new_pet_simple_empty_name — пустое имя
10. test_add_new_pet_simple_very_long_name — длинное имя
11. test_add_new_pet_simple_negative_age — отрицательный возраст
12. test_add_new_pet_simple_age_zero — возраст 0
13. test_add_new_pet_simple_age_very_high — возраст 999
14. test_add_new_pet_special_characters — спецсимволы
15. test_get_my_pets_without_auth_key — без авторизации
16. test_delete_pet_wrong_id — неверный ID

## Ожидаемый результат
16 passed

## Примечание
Файл .env содержит персональные данные. Он добавлен в .gitignore и не загружается на GitHub. В репозитории хранится только пример заполнения.

Автор: Антон Мороз
Дата: Март 2026
