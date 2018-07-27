1. Импорт данных
  1.1. Готовим проект 
  - Создание проекта на github
  - Создание виртуальной машины для разработки
  - Первый push на github по ssh
  - pip, virtualenv и requirements.txt
  - Создание проекта Django
  1.2 Импорт словарных статей
  - Management-команды в Django
  - Работа с OxfordDictionary API, requests
  - Реализация команды сохраняющей словарные статьи в файловую систему
  - Извлечение данных в несколько потоков
  - Преимущества и недостатки pypy, как еще ускорить программу
  1.3 Импорт "произношений"
  - Разбор данных с внешних сайтов
  - Импорт "тяжелых" данных
  - Абузоустойчивость программы
  1.4 Тестирование приложений
  - Django testing framework
  - Unit-тесты для management-команд
2. Модель данных
  - Работа с базами данных в Django, миграции
  - Сущность User и заменяемая модель в django.contrib.auth
  - Проектируем модель DictionaryItem
  - Проектируем модель Word
  - django_admin, удобное отображение данных, виджеты, вопросы производительности
4. Перенос данных в модель
  - Фикстуры и эффективный импорт данных
  - Юнит-тестирование моделей
5. Пользовательский интерфейс
  - Представления в виде функций и CBV
  - Шаблонизатор django, подключаемые шаблонизаторы
  - Авторизация и аутентификация
  - Работа со статикой в django, frontend hell, сборка статики внешними инструментами
  - Собираем клиентское приложение из готовых запчастей
  - Тестирование клиентской части
6. Релиз
  - Деплой приложения на Linux-системе
  - Автоматизация задач деплоя
  - Контроль за работоспособностью приложения
