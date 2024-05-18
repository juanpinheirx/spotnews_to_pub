{% extends 'base.html' %}
{% load static %}

{% block title %}Página de Detalhes da Notícia{% endblock %}
{% block content %}
    <h1 class='news-title'>{{news.title}}</h1>
    <p class='news-content'>{{news.content}}</p>

{% for category in news.categories.all %}
    <span class='news-categories'>{{ category.name }}</span>
{% endfor %}

    <span class='news-author'>{{news.author}}</span>
    <img src="{% static news.image.url %}">
    <span>{{news.created_at|date:"d/m/Y"}}</span>

{% endblock %}