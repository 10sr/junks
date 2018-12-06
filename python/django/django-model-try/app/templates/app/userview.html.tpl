{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<p>Userinfo: {{ user.str }}</p>


<a href="{% url 'app:user' user.username %}">This page</a>
<a href="{% url 'app:index' %}">Top</a>

