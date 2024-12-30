---
layout: default.md
title: Team
---

# Meet our amazing team!

<div class="team-container">
  {% for member in team.members -%}
    <div class="team-member">
      {% if member.photo %}
        <img src="{{ member.photo }}" alt="{{ member.name }}">
      {% else %}
        <div class="placeholder-photo"><i class="fas fa-user-astronaut"></i></div>
      {% endif %}
      <h3>{{ member.name }}</h3>
      <p>{{ member.role }}</p>
      <div class="team-member-links">
        {% if member.linkedin %}
          <a href="{{ member.linkedin }}" target="_blank" aria-label="LinkedIn"><i class="fab fa-linkedin"></i></a>
        {% endif %}
        {% if member.bluesky %}
          <a href="{{ member.bluesky }}" target="_blank" aria-label="Bluesky"><i class="fab fa-bluesky"></i></a>
        {% endif %}
        {% if member.x %}
          <a href="{{ member.x }}" target="_blank" aria-label="Twitter"><i class="fab fa-x-twitter"></i></a>
        {% endif %}
        {% if member.github %}
          <a href="{{ member.github }}" target="_blank" aria-label="GitHub"><i class="fab fa-github"></i></a>
        {% endif %}
        {% if member.homepage %}
          <a href="{{ member.homepage }}" target="_blank" aria-label="Homepage"><i class="fa-solid fa-home"></i></a>
        {% endif %}
      </div>
    </div>
  {%- endfor %}
</div>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
