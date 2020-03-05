## Подключение базового шаблона
    {% extends 'base.html' %}

## Подключение статических файлов (css, js, img, fonts, ...)
    {% load static %}
    {% static 'path/name.format' %}
    
## Подключение css, js вне base.html
    {% block css %} <link href="{% static 'css/name.css' %}" /> {% endblock %}
    {% block js %} <script href="{% static 'js/name.js' %}" /> {% endblock %}
    
## < title>Имя страницы< /title>
    {% block title %} Имя страницы {% endblock %}

## Импорт в основной шаблон
    {% block content %}
        html код
    {% endblock %}

## Для импорта html - часть кода
    {% include 'name.html' %}

## Пример цикла товаров
    {% for article in articles %}
        {{ article.title }}
    {% endfor %}
##
## Если что то не понятно будет, спрашивай. Если будут сложности, могу сам написать - не страшно.