{% load static %}

<link rel="stylesheet" type="text/css" href="{% static 'app/style.css' %}" />

{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<p>Userinfo: {{ user.str }}</p>

{% if sleeps %}
<ul>
    {% for sleep in sleeps %}
    <li>{{ sleep.str }}</li>
    {% endfor %}
</ul>
{% else %}
<p>No sleep record found.</p>
{% endif %}

<form action="{% url 'app:user_addneru' user.username %}" method="post">
    {% csrf_token %}
    <input type="text" name="note" />
    <input type="submit" value="AddNeru" />
</form>

<a href="{% url 'app:user' user.username %}">This page</a>
<a href="{% url 'app:index' %}">Top</a>

